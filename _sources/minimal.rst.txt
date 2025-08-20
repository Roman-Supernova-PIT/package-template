.. _minimal:

Minimal package layout
======================

This chapter describes a minimal package layout.  If you created your repository using the instructions in :ref:`using-the-template`, then your package will already be as described on this page.  Read this only if you need to modify any of these files and/or want to understand the files that the template has placed in your repository.

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

Assuming that you are planning to make your package open source, the most important file you will need to add to your package is an open source license.  The Roman SNPIT uses 3-clause BSD license (which is used by may packages in the scientific Python echosystem), and that is already in the ``LICENSE`` file imported from the template.  If you have a good reason to want to use a different license, please contact one of the software admins for the PIT.

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
we recommend making the package and the module name the same to avoid confusion.  Sometimes this is impossible, as a package name may already be used on PyPI, or may otherwise be rejected by PyPI.  A good second option is to add a prefix of ``roman-snpit`` to the ``name`` field of your pckage.  This is done, for example, in the ``snappl`` package (`cf: the snappl pyproject.toml <https://github.com/Roman-Supernova-PIT/snappl/blob/main/pyproject.toml>`_).

Note that the version of the package is **not** explicitly defined in the file above,
(rather, defined as ``dynamic``), because we are using the
`setuptools_scm <https://pypi.org/project/setuptools-scm/>`_ package to automatically
retrieve the latest version from Git tags.  See :ref:`releasing` for more information.

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
