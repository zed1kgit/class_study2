from main import Teacher


def test_teacher_init(teacher):
    assert len(Teacher.teachers_dict) == 1
    assert Teacher.teachers_dict == {'test_name': ['test_education', 'test_experience']}


def test_get_name(teacher):
    assert teacher.get_name() == 'test_name'


def test_get_education(teacher):
    assert teacher.get_education() == 'test_education'


def test_get_experience(teacher):
    assert teacher.get_experience() == 'test_experience'
