from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salarys = []
    for row in data:
        salary = row["max_salary"].strip()
        if salary.isdigit():
            max_salarys.append(int(salary))
    unique_salary = max(max_salarys)
    return unique_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salarys = []
    for row in data:
        salary = row["min_salary"].strip()
        if salary.isdigit():
            min_salarys.append(int(salary))
    unique_salary = min(min_salarys)
    return unique_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        if min_salary > max_salary:
            raise ValueError
        return min_salary <= int(salary) <= max_salary
    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
