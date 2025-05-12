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

* ``include_example_code``: This option will fill your new package with some example functions to allow you to test it.
* ``use_compiled_extensions``: This turns on the features needed to support compiled extensions

(This procedure was written by Rob Knop.  If you are confused about it, are (quite rationally) afraid of it, or want help with it, ping him on the SNPIT slack.)

If you already have a git repository and want to update it to use the Roman SN PIT template, some additional work is involved.  Suppose that your existing repo is named ``existing_repo``, and that you have a checkout in your current directory with that same name.

**Before you start**: make sure everything in your current repo is committed and pushed.  That way, if you screw something up, you can always start over by cloning your repo back from github.  This is a fiddly enough process that screwing something up is distressingly likely.  I also recommend doing this all on a new branch of your repo, which you can merge back to ``main`` when you're done.

Start in the directory that is the parent of where your existing repo is checked out.  (I.e. the directory in which you would do ``cd existing_repo`` in order to get to your checkout.)  Run:

.. code-block:: console

   $ pip install cookiecutter cruft
   $ cruft create https://github.com/Roman-Supernova-PIT/package-template --output_dir existing_repo_template

replacing ``existing_repo`` with the name of your package.  When asked for your package and module name, give it the name of your existing repo (``existing_repo`` in this example).  See above for answering the other various questions to you get.  This will create a directory ``existing_repo_template``, which in turn has a subdirectory ``existing_repo`` (again, as always, replacing ``existing_repo`` with the name of your package).

Next, some hand work is going to be required to make sure things are all in the right format.  In your existing repo (your checkout of which you have probably renamed— ``existing_repo_backup`` in this directory), do the following:

* If it's not there already, move (using ``git mv``) all the code that comprises the content of your package into a subdirectory with the same name as the repo (``existing_repo`` in this example— so, your code would now be in ``existing_repo/existing_repo`` relative to the directory where you clone stuff from github).

* In this subdirectory, if you have a file ``__init__.py``, rename it to ``__init__.py-BACKUP``.  (Don't do this with ``git mv``, just do a standard ``mv``.  Yes, you're making a mess out of your checkout, but you'll clean it up later.)

* If you have tests, make sure they are all in the ``existing_repo/tests`` subdirectory of your checkout.  (So, ``existing_repo/existing_repo/tests`` relative to the parent directory where you do your git clones.)  Again, if they're not already in the right place, move them with ``git mv``.

* In the ``tests`` subdirectory, if you have any of the following files, rename them to ``<filename>-BACKUP`` (again just with ``mv``, *not* with ``git mv``).
  * ``conftest.py``
  * ``__init__.py``

* ``cd`` back to the top level directory of your checkout (in this example, ``existing_repo`` underneath the directory where you run ``git clone``).

* Try running::
    rsync -n -a -v -i ../existing_repo_template/existing_repo/ ./

  as always replacing ``existing_repo`` with the name of your own repo.  This will not actually copy any files; the ``-n`` makes it a dry run.  This will tell you what will get copied from the package template to your current directory.  The output is a little bit byzantine, but the key is to look for lines that do *not* start with either ``.d..t......`` (which just indicates a directory), or ``>f+++++++++``.  Lines that start with the latter describe a file that does not exist in your current directory and that will be copied over from the template.  This is all good!  If there are any other lines that start with ``>f`` but do *not* have the row of plusses, then those are files that already exist in your current directory that will be overwritten when you import the template.  If you know what you're doing, you can just let this happen.  However, what you should probably do instead is rename that file from ``<filename>`` to ``<filename>-BACKUP`` so that you're current changes won't get overwritten.  (You will merge this later.)  When you've done this, run the above ``rsync`` command again to make sure everything in the output is either a directory, something you are very confident you want to overwrite, or something that starts with ``>f+++++++++``.

* Once you're confident you're not going to overwrite anything you don't want to, run::
    rsync -a -v -i ../existing_repo_template/existing_repl/ ./

  this actually *will* copy over files.

* Run the following command::
    find . -name "*-BACKUP" -print

  for every file listed in that command, you need to merge that file with the same file that does not have the ``-BACKUP` in the filename.  Do this manually, and carefully.  It might be painful.  I hope not.  The results of the merge should go into the file without ``-BACKUP`` in the name.  When you're done, delete the ``-BACKUP`` file.

* Do a ``git status`` in the top level of your repo.  You should see lots of files that were added by importing the template.  You will also see moved and modified files.  ``git add`` the appropriate files, ``git commit``, and ``git push``.
  
