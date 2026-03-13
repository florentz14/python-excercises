from settings import PROJECT_ROOT, PANDAS_DIR, DATABASES_DIR


def test_project_structure_exists() -> None:
    assert PROJECT_ROOT.exists()
    assert PANDAS_DIR.exists()
    assert DATABASES_DIR.exists()
