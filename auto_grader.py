class BatchGrader:
    """Grades a list of different academic tasks using polymorphism."""

    def process_grades(self, assignment_list, student_profile):
        """
        Grade each assignment and add its score to the student's total.

        Every assignment must provide get_details() and grade_work().
        The student profile must provide name, add_points(), and
        get_current_score().
        """
        print(f"Running Auto-Grader for {student_profile.name}...")

        for assignment in assignment_list:
            assignment.get_details()
            score = assignment.grade_work()
            student_profile.add_points(score)

        final_score = student_profile.get_current_score()
        print(f"Final Grade Processed! Total Score: {final_score}")

        return final_score
