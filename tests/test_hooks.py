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
        assert not (cj.project_path / ctx['package_name'] / afile).exists()


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
    ]

    if ctx['use_compiled_extensions'] == 'y':
        example_files.append("example_c.pyx")

    for afile in example_files:
        assert (cj.project_path / ctx['package_name'] / afile).exists()


@pytest.mark.parametrize("license, lfile", [
    ("BSD 3-Clause", "LICENSE")])
def test_licence(license, lfile, cookies):
    cj = cookies.bake(extra_context={'license': license})

    assert (cj.project_path / "licenses" / "LICENSE").exists()

    with open(cj.project_path / "licenses" / "LICENSE") as fobj:
        license_content = fobj.readlines()

    base_path = Path(".") / "{{ cookiecutter.package_name }}"
    base_path /= "licenses"
    base_path = base_path.resolve()
    with open(base_path / lfile) as fobj:
        expected_content = fobj.readlines()

    assert expected_content[1:] == license_content[1:]
