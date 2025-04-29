def test_version_is_string():
    from {{ cookiecutter.module_name }} import __version__
    assert isinstance(__version__, str)