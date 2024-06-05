import pytest
from main import Teacher


@pytest.fixture
def teacher():
    Teacher.teachers_dict.clear()
    teacher = Teacher("test_name", "test_education", "test_experience")
    return teacher
