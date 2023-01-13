from typing import List, Dict
from src.insights.jobs import read

def get_unique_industries(path: str) -> List[str]:
    file = read(path)
    file_list = []

    for industry in file:
        if len(industry["industry"]) != 0:
            file_list.append(industry["industry"])
    return set(file_list)
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
