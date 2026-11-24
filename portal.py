
class CoursePortal:
    """Controls whether students may submit work to a course."""

    def __init__(self, course_name):
        self.course_name = course_name
        self.__is_locked = False

    def lock_portal(self):
        """Close the submission portal."""
        self.__is_locked = True
        print("Deadline passed. Portal locked.")

    def accept_submission(self, student_name):
        """Accept a submission while open; reject it when locked."""
        if self.__is_locked:
            raise ValueError("Deadline has passed! Submission rejected.")

        print(f"Submission accepted for {student_name}.")
