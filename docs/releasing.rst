.. _releasing:

Releasing Your Package
======================

In this section we will describe how to take your package and publish a release to PyPI.

Incrementing Version Numbers
----------------------------

See :ref:`incrementing-version` in the :ref:`checklist` for information on specifying the version number of the package you want to relese.


Building Source Distributions
-----------------------------

Now you have tagged your release, you need to build what is called a "source
distribution" to upload to `PyPI <https://pypi.org/>`__ or the Python Package
Index. This is the place where tools like ``pip`` download packages from and is
the primary place people will search for installable Python packages.

The source distribution is a tarball of all the files needed by your package,
which includes everything in your ``my_package`` directory as well as everything
specified in your :ref:`manifest` file.

As we have setup a package with a :ref:`pyproject` file, we recommend you use the
`build <https://pypa-build.readthedocs.io/en/latest/>`__ package to build your
source  distribution in the isolated environment specified in :ref:`pyproject`.
You can do this with:

.. code-block:: console

   $ pip install build
   $ python -m build --sdist --outdir dist .

This is equivalent to running the legacy ``python setup.py sdist`` but ensures
that the state of your local environment does not affect the generated package.

Publishing to PyPI
------------------

Now you have created the sdist to be uploaded to PyPI you can upload it with the
`twine <https://pypi.org/project/twine/>`__ package:

.. code-block:: console

   $ pip install twine
   $ twine upload dist/my_package*.tar.gz

This should ask you for your PyPI account details, and will create your project
on PyPI if it doesn't already exist.

Releasing from Branches
-----------------------

WARNING : this section is probably not correct for the SNPIT.  Review it before using it.

If your project is larger, you might want to create branches for each of your
major release versions to make it easy to continue to support those releases
with bug fixes while continuing development of your master branch.

If you follow this pattern for your releases you will have to perform one extra
step when using ``setuptools_scm``, which is to also increment the version with
a tag on the master branch to indicate you have started to develop a new version
on your master branch. To do this at the point where you branch for your
upcoming release push a tag for ``vX.Ydev`` where ``X.Y`` is the version number
of the next major release e.g. if you just branched for 1.1 you would create a
``v1.2dev`` tag.
