from main import Teacher


def test_teacher_init(teacher):
    assert len(Teacher.teachers_dict) == 1
    assert Teacher.teachers_dict == {'test_name': ['test_education', 'test_experience']}
