Python Packaging Guide
======================

This guide is intended to explain modern Python packaging, it covers most of the core components of a modern package, and explains these components. It is broken up into the following sections:

.. toctree::
   :maxdepth: 2

   minimal
   docs
   checklist
   tests
   checklist
   tox
   extensions
   releasing
   scripts
   data
   ci
   advanced/index

Using the Template
==================

With this guide is a `cookiecutter <https://cookiecutter.readthedocs.io/>`__ template which allows you to get started quickly with a package as described in this guide.

To create a new package based on the template run:

.. code-block:: console

   $ pip install cookiecutter cruft
   $ cruft create https://github.com/Roman-Supernova-PIT/package-template

It will ask you several questions:

* *Select your package name* : This is the name your package will have on PyPi, and ``pip install <packagename>`` will be the command that somebody types in order to install it.  (It will also be the name of the directory that gets created, ready for you to start putting code into.)
* *Select your module name* : This is the name of the module.  To use your package in python, you will do ``import <modulename>``.  Ideally your module name is the same as your package name, and that's what it defaults to.  Making the two the same makes things simpler for everybody.  However, you may want to prefix your package (but not module) name with ``roman_snpit_``.  You may need to do this if your module name is too close to something that already exists on PyPi.
* *Name of repo on github underneath Roman-Supernova-PIT* : Your github repo will be at ``https://github.com/Roman-Supernova-PIT/<reponame>``.  Ideally, this is the same as your module name, and that's what it defaults to.
* *Short description of your package* : one-line description of your package.  Don't keep the default here, put something specific to your package in.
* *Author Name* : If you are mostly writing this yourself, put your own name in.  Otherwise, put in Roman Supernova PIT.
* *Author Email* : This is a contact person for this package.  Hopefully it will never get used, but somebody might need to ask about it.  Put the email of the person who should receive those questions here.
* *GitHub username* : Your github username, or the github username of the person who will be the primary owner of this package.
* *Select minimum python version* : Select 1 for 3.11 here if that's at all possible, as that's the environment we're using for the SN PIT.  Only pick a higher version if you *really* need it.
* *...non-python code that compiles*: If you've only written Python, leave this at 'n'.  If you have compiled extensions (e.g. C++ code that you link to Ptyhon with ``ctypes``), answer 'y' here.
* *include example code* : This option will fill your new package with some example functions to allow you to test it.  It defaults to 'y'.  Remember to remove the example code later if you don't really want it to be part of your package.
* *Include github workflow testing...* : Answer 'y' (the default) to include github workflows that will instruct github to automatically run tests on any pull request to your repo.  You probably want to leave this at 'y'.
* *install_requires* : Here you can list additional external packages that your package requires.  Don't worry if you miss some here, you will be able to add to that list later by editing a file the package template creates.

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

When running ``git add`` in your repo
-------------------------------------
You want to add everything created by the package template, and you probably want to do that the first time before you start adding your own files and customizing it.  However, if you created your clean environment in such a way that it created a new directory in your package directory, make sure *not* to import that environment into git!  (This will happen, for instance, if you run ``python -mvenv clean_environment``.  It will create a directory ``clean_environment`` under your current directory, which will end up with a lot of stuff you really don't want to track in git.)  As long as you didn't do that, you can probably just run ``git add .`` and trust the ``.gitignore`` file to not add most of the stuff you don't want.
