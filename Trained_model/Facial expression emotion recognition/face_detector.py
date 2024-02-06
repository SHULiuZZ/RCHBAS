# ---- coding: utf-8 ----

from abc import ABC, abstractmethod


class FaceDetector(ABC):
    @abstractmethod
    def detect_faces(self):
        pass
