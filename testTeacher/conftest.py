import pytest
from main import Teacher, DisciplineTeacher


@pytest.fixture
def teacher():
    Teacher.teachers_dict.clear()
    teacher = Teacher("test_name", "test_education", "test_experience")
    return teacher


@pytest.fixture
def dis_teacher():
    dis_teacher = DisciplineTeacher("test_name", "test_education", "test_experience",
                                    "test_discipline", "test_job_tittle")
    return dis_teacher
