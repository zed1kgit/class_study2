from main import DisciplineTeacher


def test_teacher_init(dis_teacher):
    assert len(DisciplineTeacher.teachers_dict) == 1


def test_get_discipline(dis_teacher):
    assert dis_teacher.get_discipline() == 'test_discipline'


def test_get_job_title(dis_teacher):
    assert dis_teacher.get_job_title() == 'test_job_tittle'


def test_set_job_title(dis_teacher):
    assert dis_teacher.set_job_title('test_job')
    assert dis_teacher.get_job_title() == 'test_job'


def test_get_teacher_data(dis_teacher):
    assert dis_teacher.get_teacher_data() == ('test_name, образование test_education, опыт работы test_experience.\n'
                                              'Предмет test_discipline, должность test_job_tittle')


def test_add_mark(dis_teacher):
    assert dis_teacher.add_mark("test", "5") == 'test_name поставил оценку 5 студенту test.\nПредмет test_discipline'


def test_remove_mark(dis_teacher):
    assert dis_teacher.remove_mark("test", "5") == 'test_name удалил оценку 5 студенту test.\nПредмет test_discipline'


def test_give_a_consultation(dis_teacher):
    assert dis_teacher.give_a_consultation('test_ed_class') == ('test_name провел консультацию в классе test_ed_class.'
                                                                '\nПо предмету test_discipline как test_job_tittle')
