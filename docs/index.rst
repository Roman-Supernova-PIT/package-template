Roman SNPIT Template and Packaging
==================================

This guide is intended to explain how to use the Roman SNPIT Package template to create a github repositoriy for a package to be used as part of the ROMAN SNPIT pipelines.

.. toctree::
   :maxdepth: 2

   minimal
   docs
   tests
   checklist
   tox
   extensions
   releasing
   scripts
   data
   ci
   advanced/index

.. _using-the-template:

Using the Template
==================

With this guide is a `cookiecutter <https://cookiecutter.readthedocs.io/>`__ template which allows you to get started quickly with a package as described in this guide.

Creating a New Package
----------------------

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

Once your package is created, it will have the structure defined in :ref:`minimal`.  You will place your python code in the ``<modulename>`` subdirectory of your repo; you should see there is already an ``__init__.py`` file there.  You may also need to edit the ``pyproject.toml`` file, e.g. to add authors or maintainers, to change the project development status as it gets further along, and (most importantly) to update the ``dependeencies`` of the package.


Updating your repo to pull in package template changes
------------------------------------------------------

Cruft is built on cookiecutter, and enables the updating of the template from the source.  This takes the form of pull requests to the repository that the new package is pushed to.  If a package already has a cookiecutter template (which it will if you used the procedure above to create your repo), it can be linked to the parent repository using ``cruft link url-to-template``.

To manually check whether the current environment matches with the template then ``cruft check`` will tell you what the current status is.

If you want to update your package, first make a branch in which to do the updating.  Check out that branch and run::

  cruft update

to manually trigger the update.  Do a ``git status`` after the update, and look at the changes that have been made on your branch relative to ``main`` to make sure that any customizations you've made to your package haven't been lost, and that you understand what is happening to your package.  Once you're satisfied, commit the branch, do a pull request, and get the branch merged into ``main`` as usual.

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


Working with your repo and package
===================================

Trying out your package
-----------------------

Once you've committed all the files created from the package template to your repository, and (optionally) written some actual code for your package, you can test out the package with ``pip-install``.  We recommend doing this in a virtual environment you've created just for this testing, until you know what you're doing and know that you want to import a dynamic package into an environment that you usually use.  Create a virtual environment with::

  python -mvenv venv

That will create a directory ``venv`` under your current directory.  Go into that virtual environoment with::

  source venv/bin/activate

Later, to leave your environment just run ``decativate``.  You can see if you are in your virtual environment by running::

  which python

The executable it gives you should be underneat the ``venv`` directory you created above.

Once in your environment, do a "editable" install with

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

If you have a working ``docker-compose.yaml`` file in the ``tests`` directory of your repo, in that directory try running::

  docker compose run runtests

After a delay to pull down the ``snpit`` docker image, if you don't already have it on your system, you will see if your tests pass or fail... or if the whole process fails to run.  After you run your tests, clean up your system with::

  docker compose down -v

Once this is working, you need to add the actual github workflow file.  You can find an example of this file in the
|snpit_utils/.github/workflows|_ subdirectory of the ``snpit_utils`` package.  Look at the file ``run_snpit_utils.tests.yml``.  Once again, it's possible that you can adapt this to your project by simply finding all instances of ``snpit_utils`` and replacing it with your module name.

If you need help with the docker compose file, or with the github workflow file for running your tests in the snpit docker image, talk to Rob, who wrote these things for ``snpit_utils``.
