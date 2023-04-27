from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    list = []
    with open(path, encoding="utf-8") as file:
        archive = csv.DictReader(file)
        for row in archive:
            list.append(row)
    return list


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    job_types = []
    for row in data:
        job_types.append(row["job_type"])
    unique_job_types = list(set(job_types))
    return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
