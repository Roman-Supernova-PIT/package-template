.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.package_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.package_name }}

This is the preferred method to install {{ cookiecutter.package_name }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.package_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git@github.com:{{ cookiecutter._pit_github_org }}/{{ cookiecutter.github_snpit_repo_name }}.git

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL {{ cookiecutter._project_url }}/{{ cookiecutter.github_snpit_repo_name }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ pip install .

If you would like to do an editable install:

.. code-block:: console

    $ pip install -e .
    $ pip install -e .[docs]  # install document build packages during install


.. _Github repo: {{ cookiecutter._project_url }}/{{ cookiecutter.github_snpit_repo_name }}
.. _tarball: {{ cookiecutter._project_url }}/{{ cookiecutter.github_snpit_repo_name }}/tarball/master
