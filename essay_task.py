from base_task import AcademicTask


class Essay(AcademicTask):
    def __init__(self, title: str, max_points: float, minimum_words: int):
        super().__init__(title, max_points)

        if minimum_words <= 0:
            raise ValueError("Minimum word count must be greater than zero.")

        self.__minimum_words = minimum_words
        self.word_count = 0

    def submit_work(self, word_count: int) -> None:
        if not isinstance(word_count, int):
            raise TypeError("Word count must be an integer.")

        if word_count < 0:
            raise ValueError("Word count cannot be negative.")

        self.word_count = word_count
        print(f"Essay submitted: {self.title}")

    def grade_work(self) -> float:
        self.is_graded = True

        if self.word_count >= self.__minimum_words:
            return float(self.max_points)

        return float(self.max_points) * 0.80

    def get_details(self) -> None:
        print(
            f"[ESSAY] {self.title} - Word Count: {self.word_count} | "
            f"Minimum Words: {self.__minimum_words} | "
            f"Max Points: {self.max_points}"
        )
