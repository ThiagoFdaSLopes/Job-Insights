from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    list_english = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert "title" in list_english[0]
    assert "salary" in list_english[0]
    assert "type" in list_english[0]
