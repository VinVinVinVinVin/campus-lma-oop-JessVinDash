class StudentProfile:
    def __init__(self, name, student_id, total_score=0):
        self.name = name
        self.student_id = student_id
        self.__total_score = total_score

    def add_points(self, points_earned):
        if points_earned < 0:
            raise ValueError("Cannot add negative points!")
        else:
            self.__total_score += points_earned

    def get_current_score(self):
        return self.__total_score