from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    list
        List of unique job types
    """
    data = read(path)
    unique_jobs = []
    for job in data:
        if job["job_type"] not in unique_jobs and job["job_type"][0] != "2":
            unique_jobs.append(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
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
    filtered_job = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job.append(job)
    return filtered_job


def get_unique_industries(path):
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
    data = read(path)
    unique_industries = []
    for industry in data:
        if industry["industry"] not in unique_industries:
            if industry["industry"] != "":
                if not industry["industry"].isnumeric():
                    unique_industries.append(industry["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
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
    filtered_industries = []
    for farofa in jobs:
        if farofa["industry"] == industry:
            filtered_industries.append(farofa)
    return filtered_industries


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    salaries: list[int] = []
    max_salary: int = 0
    for salary in data:
        if salary["max_salary"] != "" and salary["max_salary"].isnumeric():
            salaries.append(int(salary["max_salary"]))
    for salary in salaries:
        if salary > max_salary:
            max_salary = salary
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)
    min_salary = set()
    for salary in data:
        if salary["min_salary"] != "" and salary["min_salary"].isnumeric():
            min_salary.add(int(salary["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if type(salary) != int:
        raise ValueError("deu ruim")

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("deu ruim")

    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("deu ruim")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("deu ruim")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
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
    valid_jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                valid_jobs_list.append(job)
        except ValueError:
            pass
    return valid_jobs_list
