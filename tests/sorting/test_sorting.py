from src.pre_built.sorting import sort_by

job_1 = {"min_salary": 1, "max_salary": 20, "date_posted": 2003-10-10}
job_2 = {"min_salary": 2, "max_salary": '', "date_posted": 2002-10-10}
job_3 = {"min_salary": '', "max_salary": 10, "date_posted": 2001-10-10}
job_4 = {"min_salary": 3, "max_salary": 30, "date_posted": ''}


MOCK_MAX = [job_1, job_2, job_3, job_4]
MOCK_MIN = [job_1, job_2, job_3, job_4]
MOCK_DATE = [job_1, job_2, job_3, job_4]

def test_sort_by_criteria():
    sort_by(MOCK_MAX, "max_salary")
    assert(MOCK_MAX) == [job_4,job_1,job_3,job_2]
    sort_by(MOCK_MIN, "min_salary")
    assert(MOCK_MIN) == [job_1,job_2,job_4,job_3]
    sort_by(MOCK_DATE, "date_posted")
    assert(MOCK_DATE) == [job_1,job_2,job_3,job_4]