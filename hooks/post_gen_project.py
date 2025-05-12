#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))

def copy_file(original_filepath, new_filepath):
    shutil.copyfile(os.path.join(PROJECT_DIRECTORY, original_filepath),
                    os.path.join(PROJECT_DIRECTORY, new_filepath))

def process_license():
    shutil.copyfile(os.path.join(PROJECT_DIRECTORY, 'licenses', "LICENSE"),
                    os.path.join(PROJECT_DIRECTORY, 'LICENSE'))

    remove_dir(os.path.join(PROJECT_DIRECTORY, 'licenses'))


def process_github_workflow(include_github_workflows):
    if include_github_workflows != "y":
        remove_dir(os.path.join(PROJECT_DIRECTORY,  '.github'))


if __name__ == '__main__':
    process_license()
    process_github_workflow('{{ cookiecutter.include_github_workflows }}')
    include_examples = '{{ cookiecutter.include_example_code }}' == 'y'
    use_compiled = '{{ cookiecutter.use_compiled_extensions }}' == 'y'

    if not(include_examples and use_compiled):
        remove_file('{{ cookiecutter.module_name }}/example_c.pyx')

    if not include_examples:
        print("Removing examples")
        remove_dir('{{ cookiecutter.module_name }}/example_subpkg/')
        remove_file('{{ cookiecutter.module_name }}/example_mod.py')
        remove_file('{{ cookiecutter.module_name }}/tests/test_example.py')
