from main import DisciplineTeacher


def test_teacher_init(dis_teacher):
    assert len(DisciplineTeacher.teachers_dict) == 1
