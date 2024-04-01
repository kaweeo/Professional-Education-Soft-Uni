
from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student_wo_notes = Student("course_wo_notes")
        self.student_with_notes = Student("student_with_notes", {"science": ["g=9.81"]})

    def test_correct_init(self):
        self.assertEqual("course_wo_notes", self.student_wo_notes.name)
        self.assertEqual("student_with_notes", self.student_with_notes.name)
        self.assertEqual({}, self.student_wo_notes.courses)
        self.assertEqual({"science": ["g=9.81"]}, self.student_with_notes.courses)

    def test_enroll_course_already_enrolled_and_update_notes(self):
        result = self.student_with_notes.enroll("science", ["v=m*s"])
        expected_notes = ["g=9.81", "v=m*s"]

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(expected_notes, self.student_with_notes.courses["science"])

    def test_enroll_method_course_add_notes_and_adding_course(self):
        result = self.student_with_notes.enroll("physics", ["f=m*g", "m=f/g"], "Y")
        self.assertEqual("Course and course notes have been added.", result)

        expected_course = {'physics': ['f=m*g', 'm=f/g'], 'science': ['g=9.81']}
        self.assertEqual(expected_course, self.student_with_notes.courses)

    def test_enroll_courses_wo_notes(self):
        result = self.student_wo_notes.enroll("Test_course_name", "test_note", "n")
        self.assertEqual("Course has been added.", result)

        self.assertEqual(
            {"Test_course_name": []},
            self.student_wo_notes.courses
        )

    def test_add_notes_if_course_in_courses(self):
        # self.student_with_notes = Student("student_with_notes", {"science": ["g=9.81"]})
        result = self.student_with_notes.add_notes("science", "2g=g**g")
        self.assertEqual("Notes have been updated", result)

        all_notes = ["g=9.81", "2g=g**g"]
        self.assertEqual(all_notes, self.student_with_notes.courses["science"])

    def test_add_notes_exception_raised(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_notes.add_notes("Biology", "Bacterial division")

        self.assertEqual(
            "Cannot add notes. Course not found.",
            str(ex.exception)
        )

    def test_leave_course_exception_raising(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_notes.leave_course("Chemistry")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_method_working_correctly(self):
        result = self.student_with_notes.leave_course("science")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_notes.courses)

if __name__ == "__main__":
    main()