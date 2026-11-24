from abc import ABC, abstractmethod


class AcademicTask(ABC):
    def __init__(self, title: str, max_points: int, is_graded: bool = True):
        self.title: str = title
        self.max_points: int = max_points
        self.is_graded: bool = is_graded

    @abstractmethod
    def submit_work(self):
        pass

    @abstractmethod
    def grade_work(self):
        pass

    @abstractmethod
    def get_details(self):
        pass