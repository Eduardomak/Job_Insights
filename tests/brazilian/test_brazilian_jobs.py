from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs(path="tests/mocks/brazilians_jobs.csv"):
    read_portuguese = read_brazilian_file(path)

    for job in read_portuguese:
        assert job.get("titulo") is None
        assert len(job.get("title")) != 0
        assert len(job.get("salary")) != 0
