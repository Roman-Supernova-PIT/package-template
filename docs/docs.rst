.. _documentation:

Documenting your Package
========================

There are two main ways to document your project, both of
which are essential: :ref:`docstrings` and :ref:`narrative`.

.. _docstrings:

Docstrings
----------

First, public functions, methods, and classes
in your package should include *docstrings*, which are strings
attached to those objects which the user can access interactively
using e.g. ``help()`` and which can also be retrieved by automated
tools. See `PEP 257 - Docstring Conventions <https://www.python.org/dev/peps/pep-0257/>`_
for a high-level overview of what docstrings are. We recommend adopting
the `numpydoc <https://numpydoc.readthedocs.io/en/latest/format.html>`_
format for docstrings. An example of such a docstring is::

    def foo(var, long_var_name='hi'):
        """A one-line summary that does not use variable names.

        Several sentences providing an extended description. Refer to
        variables using back-ticks, e.g. `var`.

        Parameters
        ----------
        var : int
            The type above can either refer to an actual Python type
            (e.g. ``int``), or describe the type of the variable in more
            detail, e.g. ``(N,) ndarray`` or ``array_like``.
        long_var_name : {'hi', 'ho'}, optional
            Choices in brackets, default first when optional.

        Returns
        -------
        out : type
            Explanation of `out`.
        """

These docstrings should be included in the Python files alongside the Python
objects they document.

.. _narrative:

Narrative Documentation
-----------------------

Second, you should write a set of narrative documentation which functions as a
user guide, such as http://docs.astropy.org or http://docs.sunpy.org.
This package template will create the basis for this.  You will find
that in the ``docs`` directory under the top level of your repo.  You
will want to edit the following files to make them correct for your
package:

* ``installation.rst`` -- with luck, the stuff that is there already is
  sufficient, but you should review it.

* ``usage.rst`` -- This is where you will write your main documentation.

* ``index.rst`` -- This one may be OK as is, but you will need to edit
  it if your documentation is long (see below).

If your documentation is short enough, you can write it all on the
``usage.rst`` page.  If it's long, you might want to divide it into
sections.  Give each section its own ``.rst`` file.  Then, list the
files you've added underneath the ``..tocktree::`` directive in the file
``index.rst``.

All of these files are in `Sphinx reStructuredText format
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.
If you haven't used Sphinx before, you maybe interested in their
`Getting Started <http://www.sphinx-doc.org/en/master/usage/quickstart.html>`_ guide.

Seeing your documentation
*************************

**NOTE TO MEGAN** this is currently broken for me.  ``make html`` works
for me in the package template, However, when I make a new package
straight from the package template and try this, I get a lot of errors.
I was able to get it to work in ``snpit_utils`` by also doing ``pip
install -e .`` in my venv, so that it could find that module.  However,
it didn't automatically include the docstrings in the created html
documentation.

The package template includes much (perhaps everything) of what you need
to build the packages locally.  First, unless you are sure you already
have everything for building the docs in your python environment, make
yourself a virtual environment (either with conda or python venv) to
work in.  In that environment, and at the top level of your repo
checkout, run::

  pip install -e ".[docs]"

then in the `docs` directory run::

  make html

That will create a subdirectory ``_build/html`` underneath the ``docs``
directory.  Open the file ``index.html`` in that subdirectory in your
web browser, and you should see a preview of your documentation.


.. _automodapi:

Including docstrings in the narrative documentation
---------------------------------------------------

As part of the narrative documentation, it is also common practice to include an
Application programming interface (API) page which lists the available classes,
methods, and functions in your package. Thankfully, if you've defined your docstrings
as described in :ref:`docstrings`, then this can be automated using the
`sphinx-automodapi <https://sphinx-automodapi.readthedocs.io>`_
package. See the documentation of that package for more details, but a
repo created from this package template should already be set up to
automatically include this.




briefly,
you will need to add ``'sphinx_automodapi.automodapi'`` to the ``extensions``
variable in your ``conf.py`` file:

.. code-block:: python

    extensions = ['sphinx_automodapi.automodapi']

In addition, if you use the numpydoc format for your docstrings, as recommended in :ref:`docstrings`,
you will need to include either ``'numpydoc'`` or ``'sphinx.ext.napoleon'`` in
the list of ``extensions`` (both packages provide a way to parse numpydoc-style
docstrings). If you use the numpydoc package, you will need to also include:

.. code-block:: python

    numpydoc_show_class_members = False

in your ``conf.py`` file.

Declaring dependencies for documentation
----------------------------------------

To make it easier for contributors to get set up with the dependencies
required to build the documentation, as well as to make it easier to
configure automated builds (whether for :ref:`ReadTheDocs <readthedocs>`
or :ref:`tox <tox>`), you should define an ``[project.optional-dependencies]`` section in
your ``pyproject.toml`` file named ``docs`` which lists the dependencies
required to build the documentation (not including dependencies already
mentioned in ``dependencies``):

.. code-block:: toml

    [project.optional-dependencies]
    docs = [
        "sphinx",
        "sphinx-automodapi",
        "numpydoc",
    ]

This will then allow contributors to type::

    pip install -e .[docs]

to install the package in developer/editable mode along with the documentation
dependencies.

.. _readthedocs:

Setting up ReadTheDocs
----------------------

**NOTE FOR MEGAN** : isn't this section out of date?  I thought we
weren't going to use readthedocs.

`ReadTheDocs <http://readthedocs.org/>`__ is a platform that will build
documentation with sphinx and will then host it, and is used by many of
the Scientific Python packages. The easiest way to configure the build
is to add a file called ``.readthedocs.yml`` to your package, and we
recommend starting off with:

.. code-block:: yaml

    version: 2

    build:
      image: latest
      tools:
        python: 3.9

    python:
      install:
          - method: pip
          path: .
          extra_requirements:
              - docs

Once you have added this to your repository, you can then import your
package into ReadTheDocs as described in `this guide
<https://docs.readthedocs.io/en/stable/intro/import-guide.html>`_.

.. _plot_directive:

Add plots to your documentation
-------------------------------

A plot is worth *many* words, and sometimes documentation
can demonstrate the uses and advantages of using a given
package much more efficiently than narrative docs. Matplotlib,
for example, has made this quite straightforward with the
`plot directive <https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html>`_.

To add a plot to your Sphinx documentation, add the following string to the
``extensions`` list in your ``docs/conf.py`` file:

.. code-block:: python

    extensions = [
        ...  # preserve your other extensions here, then add:
        "matplotlib.sphinxext.plot_directive"
    ]

To make use of this extension, you will also need to add ``matplotlib`` to your
``tox.ini`` file:

.. code-block:: ini

    deps =
       # preserve your other deps here, then add:
       matplotlib

Now you can add plots to your Sphinx docs by adding a block like
the following to your narrative docs:

.. code-block:: rst

    Here's a plot:

    .. plot::

        import matplotlib.pyplot as plt

        x, y = [1, 2, 3], [4, 5, 6]

        plt.figure()
        plt.plot(x, y)

By default, sphinx and matplotlib will render the figure defined by the
Python code in the ``.. plot::`` block, without the source code. Full documentation
for the configuration settings for the plot directive can be found in the
`matplotlib docs <https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html>`_.
