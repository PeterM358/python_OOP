from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.first_student = Student('Koki')

    def test_init__when_no_courses__expect_empty_courses(self):
        self.assertEqual('Koki', self.first_student.name)
        self.assertEqual({}, self.first_student.courses)

    def test_enroll__when_first_time_course_and_notes__expect_added_courses_notes(self):
        result = self.first_student.enroll('Python', ['Linux', 'Database'])
        self.assertEqual(1, len(self.first_student.courses))
        self.assertEquals(2, len(self.first_student.courses['Python']))
        self.assertEqual('Course and course notes have been added.', result)

    def test_enroll__when_course_and_notes__expect_not_added_course_notes(self):
        result = self.first_student.enroll('Python', ['Linux', 'Database'], 'N')
        self.assertEqual(1, len(self.first_student.courses))
        self.assertEqual(0, len(self.first_student.courses['Python']))
        self.assertEqual('Course has been added.', result)

    def test_enroll__when_old_course__expect_to_update_notes(self):
        result = self.first_student.enroll('Python', ['Linux', 'Database'])
        self.assertEqual(1, len(self.first_student.courses))
        self.assertEquals(2, len(self.first_student.courses['Python']))
        self.assertEqual('Course and course notes have been added.', result)

        result = self.first_student.enroll('Python', ['ly notes', 'data notes'])
        self.assertEqual(1, len(self.first_student.courses))
        self.assertEquals(4, len(self.first_student.courses['Python']))
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_add_notes__when_unavailable_course__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.first_student.add_notes('Linux', 'ly web')
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_add_notes__when_available_course__expect_added_notes(self):
        result = self.first_student.enroll('Python', ['Linux', 'Database'])
        self.assertEqual(1, len(self.first_student.courses))
        self.assertEquals(2, len(self.first_student.courses['Python']))
        self.assertEqual('Course and course notes have been added.', result)

        result = self.first_student.add_notes('Python', 'ly notes')
        self.assertEqual('Notes have been updated', result)
        self.assertEqual(3, len(self.first_student.courses['Python']))
        self.assertIn('ly notes', self.first_student.courses['Python'])

    def test_leave_curse__when_available_course__expect_to_remove(self):
        result = self.first_student.enroll('Python', ['Linux', 'Database'])
        self.assertEqual(1, len(self.first_student.courses))
        result = self.first_student.leave_course('Python')
        self.assertEqual(0, len(self.first_student.courses))
        self.assertEqual('Course has been removed', result)

    def test_leave_curse__when_not_available_course__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.first_student.leave_course('Linux')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == '__main__':
    main()