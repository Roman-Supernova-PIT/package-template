.. _minimal:

Minimal package layout
======================

To start off, we will take a look at the minimal set of files you will need to
create an installable Python package. Once you have set these up, your package
directory should look like::

    ├── LICENCE
    ├── my_package
    │   └── __init__.py
    ├── pyproject.toml
    ├── setup.py
    ├── MANIFEST.in
    └── README.rst

where ``my_package`` is the name of your package. We will now take a look at all of
these files in turn.

.. _license:

``LICENSE``
-----------

Assuming that you are planning to make your package open source, the most
important file you will need to add to your package is an open source license.
Many packages in the scientific Python ecosystem use the `3-clause BSD license
<https://opensource.org/licenses/BSD-3-Clause>`_ and the packages maintained by
the Roman Supernova PIT group will too. If you have a good reason not to, please
contact one of the software admins for the PIT.

The BSD 3-Clause license is included as part of the package template and will
be created when you generate a new package.

.. _readme:

``README.rst``
--------------

Another important file to include is a README file, which briefly tells users
what the package is, and either gives some information about how to install/use
it or links to more extensive documentation. We recommend using the
`reStructuredText (rst) <http://docutils.sourceforge.net/rst.html>`_ format for
your README as this will ensure that the README gets rendered well online, e.g.
on `GitHub <https://github.com>`_ or  `PyPI <https://pypi.org>`_.

.. _package_init:

``my_package/__init__.py``
--------------------------

Python code for your package should live in a sub-directory that has the name
of the Python module you want your users to import. This module name should
be a valid Python variable name, so cannot start with numbers and cannot include
hyphens. Valid package names are ``example`` or ``my_package``. For the rest
of this guide, we will assume the name of the module is ``my_package``.

A directory structure built from this package template will have a
``__init__.py`` file all in place that may well be all that you need.
If you know that you need additional things in your ``__init__.py``, add
those things to the one the package template gives you.

Among other things, the package template will set it up so that once
your package is properly installed, your module will have a
`__version__` property that is pulled from tags in the git archive.


.. _pyproject:

``pyproject.toml``
------------------

The ``pyproject.toml`` file is where we will define the metadata about the package.
At a minimum, this file should contain the ``[project]`` table (defined by
`PEP621 <https://peps.python.org/pep-0621/>`_) and the ``[build-system]`` table
(defined by `PEP518 <https://peps.python.org/pep-0518/>`__).

The ``pyproject.toml`` file provided by the package template will
provide most of what you need, so you will seed that much of what is
described below is already in place.  You may need to add some
dependencies to your package.


``[project]``
^^^^^^^^^^^^^

.. code-block:: toml

    [project]
    name = "my-package"
    description = "My package description"
    readme = "README.rst"
    authors = [
        { name = "Your Name", email = "your@email.com" }
    ]
    license = { text = "BSD 3-Clause License" }
    dependencies = [
        "numpy",
        "astropy>=3.2",
    ]
    dynamic = ["version"]

    [project.urls]
    homepage = "https://link-to-your-project"

The ``name`` field is the name your package will have on PyPI. It is not necessarily
the same as the module name, so in this case we've set the package name to
``my-package`` even though the module name is ``my_package``. However, aside from
the case where the package name has a hyphen and the module name has an underscore,
we strongly recommend making the package and the module name the same to avoid confusion.

Note that the version of the package is **not** explicitly defined in the file above,
(rather, defined as ``dynamic``), because we are using the
`setuptools_scm <https://pypi.org/project/setuptools-scm/>`_ package to automatically
retrieve the latest version from Git tags. 

The ``description`` should be a short one-line sentence that will appear next to your package name
on `PyPI <https://pypi.org>`_ when users search for packages. The ``readme``
defines the ``README.rst`` file, which will be rendered nicely on the PyPI page for the package.

Finally, the ``dependencies`` section is important since it is where you will
be declaring the dependencies for your package. The cleanest way to do this is
to specify one package per line, as shown above. You can optionally include version
restrictions if needed (as shown with ``astropy>=3.2`` above). If your package has no dependencies then you don't need this option.

A complete list of keywords in ``[project]`` can be found in the `Python packaging documentation <https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata>`_.

``[build-system]``
^^^^^^^^^^^^^^^^^^

In the previous section we discussed the ``dependencies`` which can
be used to declare run-time dependencies for the package, which are
dependencies that are needed for the package to import and run correctly.
However, your package may have dependencies that are needed to build the
package in the first place. For example, the :ref:`setup_py` file
will only run correctly if `setuptools <https://setuptools.readthedocs.io>`_
is installed.

The recommended way to specify build-time dependencies is to define the
``build-system`` table:

.. code-block:: toml

    [build-system]
    requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
    build-backend = 'setuptools.build_meta'

If your package has C extensions that interface with `Numpy <https://numpy.org>`_,
you may also need to add Numpy to the above list - see :ref:`extensions` for
more details.

A complete list of keywords in ``[build-system]`` can be found in `PEP518 <https://packaging.python.org/en/latest/specifications/declaring-build-dependencies/#declaring-build-dependencies>`__.

``[tool.setuptools]``
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: toml

    [tool.setuptools]
    zip_safe = false

    [tool.setuptools.packages.find]

The ``zip_safe`` option should be set to ``false`` unless you understand the
implications of setting it to ``true`` - this option is most relevant when
producing application bundles with Python packages.

The ``packages.find`` line can be left as-is - this will automatically determine the
Python modules to install based on the presence of ``__init__.py`` files.

A complete list of keywords in ``[tool.setuptools]`` can be found in the
`setuptools documentation <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html>`_.

``[tool.setuptools_scm]``
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: toml

    [tool.setuptools_scm]
    version_file = "my_package/_version.py"

The ``[tool.setuptools_scm]`` table indicates that we want to use the `setuptools_scm
<https://pypi.org/project/setuptools-scm/>`_ package to set the version
automatically based on git tags, which will produce version strings such as
``0.13`` for a stable release, or ``0.16.0.dev113+g3d1a8747`` for a developer
version. 

.. _setup_py:

``setup.py``
------------

The ``setup.py`` file used to be where project metadata was defined, before the
advent of ``setup.cfg`` and then PEP621 and PEP517 (``pyproject.toml``).
It is no longer necessary to include a ``setup.py`` file in your project,
unless you are building C extensions in your code.
However, it can increase compatibility with old versions of pip and other packaging tools.

The minimal ``setup.py`` file is very simple:

.. code-block:: python

    from setuptools import setup

    setup()

.. _manifest:

``MANIFEST.in``
---------------

The last file needed for a minimal set-up is the ``MANIFEST.in`` file,
which declares which files should be included when you release your
package (see :ref:`releasing` for more details about how to do this).

This file is simplified by using ``setuptools_scm``, as **everything** that is
git versioned will be included **by default**.  There are likely to be things
you want to exclude, such as files generated by the documentation, to do this
add::

    prune <folder or files>

For example a minimal ``MANIFEST.in`` file for a package using ``setuptools_scm`` might look like

.. code-block:: text

    prune build
    prune docs/_build
    prune docs/api
    global-exclude *.pyc *.o

which would exclude the autogenerated documentation folders and other build files from the distributions.

If you have chosen not to use ``setuptools_scm``, then this file needs to list
files not in the module directory and other non-standard files.
So given the files we've seen above you would need to include::

    include LICENSE
    include README.rst
    include pyproject.toml

You can find out more about the syntax of this file in
`Specifying the files to distribute <https://docs.python.org/3.8/distutils/sourcedist.html#specifying-the-files-to-distribute>`_
in the Python documentation.


Trying out your package
-----------------------

Once you have committed all of the above files to your repository, you
can test out the package by running

.. code-block:: shell

    pip install -e .

from the root of the package. Once you have done this, you should be able to
start a Python session from a different directory and type e.g.::

    >>> import my_package
    >>> my_package.__version__
    0.1.dev1+g25976ae

.. TODO: mention about adding more files to package with functionality


Adding your package to github
------------------------------

TODO: instructions about creating a github archive and all that?  Probably no need to repeat that here, you can find that elsewhere.

When you use the template, the file `.github/CODEOWNERS` will declare that the github group "Roman-Supernova-PIT/software-admins" is one of the owners of your repo.  In PRs, you will notice an error message if this group does not in fact have access to your repo.  So, unless you have a reason not to, give them access.  To do this, go to your repo's main page on github, and click on "Settings" (next to the gear icon) in the header.  Near the top of the left sidebar, find "Collaborations and teams"; click on that.  If you don't already see "software admins" as having access, click "Add teams".  Find "Roman-Supernova-PIT/software-admins" in the list of teams, and click on it.  On the page that comes up, give the software-admins team an appropriate role; given the name, you should probably just go ahead and let that group have the "Admin" role, so that if you go away, we will still be able to fully work with your github archive.  Click "Add Selection" once you've chosen the role.


.. _adding-tests-to-github-workflow:
   
Adding tests to github workflow
-------------------------------

.. |snpit_utils| replace:: ``snpit_utils``
.. _snpit_utils: https://github.com/Roman-Supernova-PIT/snpit_utils
.. |snpit_utils/tests| replace:: ``snpit_utils/tests``
.. _snpit_utils/tests: https://github.com/Roman-Supernova-PIT/snpit_utils/tree/main/snpit_utils/tests
.. |snpit_utils/.github/workflows| replace:: ``snipit_utils/.github/workflows``
.. _snpit_utils/.github/workflows: https://github.com/Roman-Supernova-PIT/snpit_utils/tree/main/.github/workflows

If you want the tests in ``<package_name>/tests`` to automatically run on pull requests, you can add a file to `.github/workflows` that defines these tests.  If needed, contact one of the pipeline managers (including, but not limited to, Megan and Rob) for help with this.We recommend that you write the workflow to run tests within the `SN PIT environment <https://github.com/Roman-Supernova-PIT/environment>`_.

You can find an example in the |snpit_utils|_ repository.  There, look in the |snpit_utils/tests|_ subdirectory.  The files ``test_config.py`` and ``test_logger.py`` (at least) were written to test code in this repo.  The file ``docker-compose.py`` sets up a standard ``snpit`` docker environment to run the tests.  You may be able to adapt this ``docker-compose.py`` file, changing only the directory names (which may be as simple as replacing ``snpit_utils`` with the directory names for your repo).

If you have a working ``docker-compose.py`` file in the ``tests`` directory of your repo, in that directory try running::

  docker compose run runtests

After a delay to pull down the ``snpit`` docker image, if you don't already have it on your system, you will see if your tests pass or fail... or if the whole process fails to run.  After you run your tests, clean up your system with::

  docker compose down -v

Once this is working, you need to add the actual github workflow file.  You can find an example of this file in the
|snpit_utils/.github/workflows|_ subdirectory of the ``snpit_utils`` package.  Look at the file ``run_snpit_utils.tests.yml``.  Once again, it's possible that you can adapt this to your project by simply finding all instances of ``snpit_utils`` and replacing it with your module name.

If you need help with the docker compose file, or with the github workflow file for running your tests in the snpit docker image, talk to Rob, who wrote these things for ``snpit_utils``.
