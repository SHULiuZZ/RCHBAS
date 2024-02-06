# ---- coding: utf-8 ----

import numpy as np
from zwork.emotion_analyzer.emotion_detector_base import EmotionDetectorBase
from zwork.emotion_analyzer.exceptions import InvalidImage, ModelFileMissing, NoFaceDetected
from zwork.emotion_analyzer.logger import LoggerFactory
from zwork.emotion_analyzer.face_detection_dlib import FaceDetectorDlib
from zwork.emotion_analyzer.face_detection_mtcnn import FaceDetectorMTCNN
from zwork.emotion_analyzer.face_detection_opencv import FaceDetectorOpenCV
import sys
import os
import cv2
import dlib
from decimal import Decimal
from zwork.emotion_analyzer.media_utils import get_facial_ROI
from zwork.emotion_analyzer.model_utils import define_model, load_model_weights
from zwork.emotion_analyzer.validators import is_valid_img, path_exists

# Load the custom logger
logger = None
try:
    logger_ob = LoggerFactory(logger_name=__name__)
    logger = logger_ob.get_logger()
    logger.info("{} loaded...".format(__name__))
    # set exception hook for uncaught exceptions
    sys.excepthook = logger_ob.uncaught_exception_hook

except Exception as exc:
    raise exc


class EmotionDetector(EmotionDetectorBase):
    model_weights_filename = "weights.h5"
    keypoints_model_path = "shape_predictor_5_face_landmarks.dat"

    def __init__(self, 
        model_loc: str='models',
        face_detection_threshold: int = 0.99,
        face_detector: str = "dlib",) -> None:

        # construct the model weights path
        model_weights_path = os.path.join(model_loc, EmotionDetector.model_weights_filename)
        # model path for facial keypoint detector, needed for dlib face detection        
        keypoints_model_path = os.path.join(
            model_loc, EmotionDetector.keypoints_model_path
        )
        
        if not (
            path_exists(keypoints_model_path) or path_exists(model_weights_path)
        ):
            raise ModelFileMissing

        # load emotion model
        self.model = define_model()
        self.model = load_model_weights(self.model, model_weights_path)

        # select and load face detection model
        if face_detector == "opencv":
            self.face_detector = FaceDetectorOpenCV(
                model_loc=model_loc, crop_forehead=True, shrink_ratio=0.2
            )
        elif face_detector == "mtcnn":
            self.face_detector = FaceDetectorMTCNN(crop_forehead=True, shrink_ratio=0.2)
        else:
            self.face_detector = FaceDetectorDlib()
        self.face_detection_threshold = face_detection_threshold

        self.keypoints_detector = dlib.shape_predictor(keypoints_model_path)


    def detect_emotion(self, img):
        """Detects emotion from faces in an image

            Img -> detect faces -> for each face: detect emotion
        Args:
            img (numpy matrix): input image

        Raises:
            InvalidImage: 
            NoFaceDetected: 

        Returns:
            str: emotion label
        """
        # Check if image is valid

        image = img.copy()

        emotions = []        
        try:
            bboxes = self.face_detector.detect_faces(image=image)
            if bboxes is None or len(bboxes) == 0:
                return emotions
            
            for bbox in bboxes:
                # extract the current face from image and run emotion detection
                face = get_facial_ROI(image, bbox)
                emotion, emotion_conf = self.detect_facial_emotion(face)
                facial_data = { "bbox": bbox, "emotion": emotion, "confidence_scores": emotion_conf}
                emotions.append(facial_data)
        
        except Exception as excep:
            raise excep

        return emotions


    def detect_facial_emotion(self, face) -> str:
        """Emotion detection on a assumed image of a facial region

        Args:
            face (numpy matrix): input image

        Raises:
            InvalidImage:

        Returns:
            emotion (str): detected emotion 
            emotion_confidence (numpy array): prediction confidence of all the labels 
        """
        if not is_valid_img(face):
            raise InvalidImage

        # list of given emotions
        EMOTIONS = ['Angry', 'Disgusted', 'Fearful',
                    'Happy', 'Sad', 'Surprised', 'Neutral']
        
        # detect emotion
        # resize image for the model
        face = cv2.resize(cv2.cvtColor(face, cv2.COLOR_BGR2GRAY), (48, 48))
        face = np.reshape(face, (1, 48, 48, 1))
        
        model_output = self.model.predict(face)
        detected_emotion = EMOTIONS[np.argmax(model_output[0])]

        # confidence for each emotion predication
        emotion_confidence = {}
        # Sum of all emotion confidence values
        total_sum = np.sum(model_output[0])

        for index, emotion in enumerate(EMOTIONS):
            confidence = round(Decimal(model_output[0][index] / total_sum * 100), 2)
            emotion_confidence[emotion] = confidence

        return detected_emotion, emotion_confidence


if __name__ == "__main__":
    # SAMPLE USAGE
    from zwork.emotion_analyzer.media_utils import load_image_path

    ob = EmotionDetector(
         model_loc="models",
         face_detector="dlib",
     )
    img1 = load_image_path("data/sample/1.jpg")
    emotion, emotion_conf = ob.detect_facial_emotion(img1)
    print(emotion_conf)

    emotions = ob.detect_emotion(img1)
    print(emotions)
    #pass
    '''import video_main

    # You can pick a face detector depending on Acc/speed requirements
    emotion_recognizer = video_main.EmotionAnalysisVideo(
        face_detector="dlib",
        model_loc="models",
        face_detection_threshold=0.0,
    )
    emotion_recognizer.emotion_analysis_video(
        video_path='data/sample/test.mp4',
        detection_interval=1,
        save_output=False,
        preview=True,
        output_path="data/output.mp4",
        resize_scale=0.5,
    )'''