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


def test_set_experience(teacher):
    assert teacher.set_experience("test_exp1")
    assert teacher.teachers_dict['test_name'][1] == 'test_exp1'


def test_get_teacher_data(teacher):
    assert teacher.get_teacher_data() == 'test_name, образование test_education, опыт работы test_experience'


def test_add_mark(teacher):
    assert teacher.add_mark("test", "5") == 'test_name поставил оценку 5 студенту test'


def test_remove_mark(teacher):
    assert teacher.remove_mark("test", "5") == 'test_name удалил оценку 5 студенту test'
