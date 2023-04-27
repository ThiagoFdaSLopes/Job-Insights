from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries = []
    for row in data:
        industry = row["industry"].strip()
        if industry:
            industries.append(row["industry"])
    unique_industries = list(set(industries))
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return list(filter(lambda job: job["industry"] == industry, jobs))
