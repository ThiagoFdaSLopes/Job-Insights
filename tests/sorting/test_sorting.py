from src.pre_built.sorting import sort_by
import pytest


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 1500, "min_salary": 1000, "date_posted": "2021-10-27"},
        {"max_salary": 2500, "min_salary": 1250, "date_posted": "2022-10-26"},
        {"max_salary": 3500, "min_salary": 1750, "date_posted": "2023-10-25"},
    ]

    SORT_MIN_SALARY = [jobs[0], jobs[1], jobs[2]]
    SORT_MAX_SALARY = [jobs[2], jobs[1], jobs[0]]
    SORT_DATE_POSTED = [jobs[2], jobs[1], jobs[0]]

    sort_by(jobs, "min_salary")
    assert jobs == SORT_MIN_SALARY
    sort_by(jobs, "max_salary")
    assert jobs == SORT_MAX_SALARY
    sort_by(jobs, "date_posted")
    assert jobs == SORT_DATE_POSTED
    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
