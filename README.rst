Roman Supernova PIT Packaging Guide
===================================

The `Roman Supernova PIT Python Packaging Guide <https://Roman-Supernova-PIT.github.io/package-template/>`__ is based on the OpenAstronomy package template and contains an embedded `cookiecutter <https://cookiecutter.readthedocs.io/>`__ template.


Using the Template
==================

With this template and guide is a `cookiecutter <https://cookiecutter.readthedocs.io/>`__ template which allows you to get started quickly with a package as described in this guide.

To create a new package based on the template run:

.. code-block:: console

   $ pip install cookiecutter cruft
   $ cruft create https://github.com/Roman-Supernova-PIT/package-template


and go through the steps offered in the cli naming your package and filling in your details.
Cruft is built on cookiecutter, and enables the updating of the template from the source.
This takes the form of pull requests to the repository that the new package is pushed to.
If a package already has a cookiecutter template, it can be linked to the parent repository using ``cruft link url-to-template``.

To manually check whether the current environment matches with the template then ``cruft check`` will tell you what the current status is.
``cruft update`` will manually trigger an updating of the package to the template.

If you would like to stick to simply the cookiecutter approach, the template still supports that functionality thusly:

.. code-block:: console

   $ pip install cookiecutter
   $ cookiecutter gh:Roman-Supernova-PIT/package-template -o ./output_directory

This will create a new directory in your current directory named the same as the value of "packagename" you supplied. Change into this directory and run ``git init`` to make it into a git repository, and make an initial commit. Then pip install into a clean environment and try building docs:

.. code-block:: console

   $ cd <your package name>
   $ git init -b main
   $ pip install -e ".[docs,test]"
   $ cd docs
   $ make html


This is required in order to have software versioning working for your package, and to test creating docs.

The goal of the template is to quickly get you setup with the files described in the guide.
The template currently implements the following optional flags:

* ``use_compiled_extensions``: If you've only written Python, leave this at 'n'.  If you have compiled extensions (e.g. C++ code that you link to Ptyhon with ``ctypes``), answer 'y' here.
* ``include_example_code``: This option will fill your new package with some example functions to allow you to test it.  It defaults to 'y'.  Remember to remove the example code later if you don't really want it to be part of your package.
* ``include_github_workflows``: Answer 'y' (the default) to include github workflows that will instruct github to automatically run tests on any pull request to your repo.  You probably want to leave this at 'y'.
* ``install_requires``: Megan, what is this?

When ``git add``ing files to your repo
--------------------------------------
You want to add everything created by the package template, and you probably want to do that the first time before you start adding your own files and customizing it.  However, if you created your clean environment in such a way that it created a new directory in your package directory, make sure *not* to import that environment into git!  (This will happen, for instance, if you run ``python -mvenv clean_environment``.  It will create a directory ``clean_environment`` under your current directory, which will end up with a lot of stuff you really don't want to track in git.)  As long as you didn't do that, you can probably just run ``git add .`` and trust the ``.gitignore`` file to not add most of the stuff you don't want.
