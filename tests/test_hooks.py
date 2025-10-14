from pathlib import Path
import pytest


def test_examples_removed(cookiejar_no_examples):
    cj = cookiejar_no_examples
    ctx = cj.context

    example_files = [
        "example_mod.py",
        "example_c.pyx",
        "example_subpkg/"
        "tests/"
    ]

    for afile in example_files:
        assert not (cj.project_path / ctx['package_name'] / ctx['module_name'] / afile).exists()


def test_examples_present(cookiejar_examples):
    cj = cookiejar_examples
    ctx = cj.context

    example_files = [
        "example_mod.py",
        "example_subpkg/",
        "example_subpkg/__init__.py",
        "example_subpkg/tests/__init__.py",
        "example_subpkg/data/.gitignore",
        "tests/",
        "tests/test_example.py",
        "tests/__init__.py",
        "tests/test_version_string.py"
    ]

    if ctx['use_compiled_extensions'] == 'y':
        example_files.append("example_c.pyx")

    for afile in example_files:
        assert (cj.project_path / ctx['package_name'] / afile).exists()


