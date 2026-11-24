class StudentProfile:
    def __init__(self, name, student_id, class_max_points):
        self.name = name
        self.student_id = student_id
        self.class_max_points = class_max_points
        self.__total_score = 0

    def add_points(self, points_earned):
        if points_earned < 0:
            raise ValueError("Cannot add negative points!")

        if self.__total_score + points_earned > self.class_max_points:
            raise ValueError("Total score cannot exceed the class maximum!")

        self.__total_score += points_earned

    def get_current_score(self):
        return self.__total_score