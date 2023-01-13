from src.pre_built.counter import count_ocurrences


def test_counter(path = "data/jobs.csv"):
    assert count_ocurrences(path, "python") == 1639
    assert count_ocurrences(path, "PYthOn") == 1639
    assert count_ocurrences(path, "javascript") == 122
    assert count_ocurrences(path, "marketing") == 1259
    assert count_ocurrences(path, "engineering") == 2666
    assert count_ocurrences(path, "node") == 38
    assert count_ocurrences(path, "full-time") == 726
    assert count_ocurrences(path, "part-time") == 175