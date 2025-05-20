.. _checklist:

Checklist for creating a PR
===========================

Make sure you have the right things in your environment
-------------------------------------------------------

Ideally, if you're using the standard SN PIT environment (either via Conda or in a Docker image), everything will already be there, and you can ignore this section.

You need to have

* ``towncrier``


Edit your code
--------------

Do what you would normally do in a pull request: add the new feature or bug fix to the forked repo or to the non-``main`` branch you're working in.

Add a news fragment
-------------------

``towncrier``, which is run as part of the standard github actions tests, requires all PRs to have at least one new "news fragment".  In the top level directory of your repo, run::

  towncrier create <PR#>.<extension>

where ``<PR#>`` is the number of your pull request.  There is a bit of a chicken-and-egg problem here in that you have to create the pull request before you know this number; in so doing, the tests will fail, because you won't have created the news fragment yet.  So, just accept that the tests will fail right after you create the PR.  Create it, and having done so figure out what the number of the PR is.

Next, you need to figure out the ``<extension>``.  This is *probably* the name of your repo; try that.  If it doesnt work, then to find out what extensions are legal, look at ``pyproject.toml`` in the top level of your checkout and find all the entries that start with ``[[tool.towncrier.type]]``.  The ``directory`` values in those blocks are the legal extensions.

Finally, run the command above.  This will create a new file ``changes/<PR#>.<extension>.rst``.  Edit that file and put in a short one-line desription of what you've done.  Perhaps reference any Issue numbers that you are addressing.  Add that file with ``git add`` and ``git commit``, and then ``git push`` again.  This step of the tests on github should now pass.  (No promises for any other tests.)

So, for example, if your package is ``guide``, and you know that you are doing pull request #42.  In this case, you would run ``towncrier create 42.guide``.  That will create a file ``changes/42.guide.rst``.  You might then edit that file and replace its contents with::

  added the answer (Issue #42)

You'd then run ``git add changes/42.guide.rst``, ``git commit``, and ``git push``.

After merging the PR to main — bump the version if appropriate
--------------------------------------------------------------

After all code reviews and modifications are done and you have merged to `main`, you most likely will need to bump the version of the software.  This will affect the version that is attached to the software if a pip package is built, for example.

Figure out what the current version of the package is by running::
  git pull -a
  git tag

That will list the tags that are currently defined for the repo.  Find the ones that look like `semantic versioning <https://semver.org/>`_ (you really only need to read the short "Summary" section on that link, but read the rest if you're morbidly curious).  Decide which numbers you need to change based on what changes are in this PR.  Once you've figured out what your new version is going to be, create a git tag with this new version.  So, for example, suppose the highest tagged version you found existing was `1.9.5`.  Suppose you've added new functionality, but in a backwards compatible manner.  (So, you have new functions or methods, but you didn't change anything so all code that uses your code will still work as-is.)  In this case, you would want to bump the minor version number, and your new version would be `1.10.0`.  You would then run::
  git checkout <branch_of_your_pr>
  git tag 1.10.0
  git push origin --tags

That will push the new tag you made to the `main` branch on the github archive.  Thereaftrer, if somebody builds a package from that commit of the git archive, that package will bake into it the version in the tag you just created.
