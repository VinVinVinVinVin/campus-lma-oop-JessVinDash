from base_task import AcademicTask


class Quiz(AcademicTask):
    def __init__(self, title: str, max_points: float, total_questions: int):
        super().__init__(title, max_points)

        if total_questions <= 0:
            raise ValueError("Total questions must be greater than zero.")

        self.__total_questions = total_questions
        self.correct_answers = 0

    def submit_work(self, correct_answers: int) -> None:
        if not isinstance(correct_answers, int):
            raise TypeError("Correct answers must be an integer.")

        if correct_answers < 0 or correct_answers > self.__total_questions:
            raise ValueError(
                "Correct answers must be between 0 and the total number of questions."
            )

        self.correct_answers = correct_answers
        print(f"Quiz submitted: {self.title}")

    def grade_work(self) -> float:
        self.is_graded = True
        return (
            self.correct_answers / self.__total_questions
        ) * self.max_points

    def get_details(self) -> None:
        print(
            f"[QUIZ] {self.title} - Questions: {self.__total_questions} | "
            f"Max Points: {self.max_points}"
        )
