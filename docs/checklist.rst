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

Bump your version number if necessary
-------------------------------------

In :ref:`minimal` it suggests that you should be pulling version numbers from git tags, but I haven't yet figured out how this works.  You can manage version numbers manually as described there.  Briefly, Remove the line ``dynamic = ["version"]`` from your ``pyproject.toml`` file, and replace it with ``version = 0.0.1``, replacing ``0.0.1`` with the actual version.  Decide which numbers should be changed by thinking about `semantic versioning <https://semver.org`.  (You can get most of what you need to know from that page by reading the short "Summary" section.)

Add a news fragment
-------------------

``towncrier``, which is run as part of the standard github actions tests, requires all PRs to have at least one new "news fragment".  In the top level directory of your repo, run::

  towncrier create <Issue#>.<extension>

The Issue # should be the repo's Issue # that this PR addresses.  (If there isn't an issue on github, make one; if that seems excessive, then you can use any text string in place of ``<Issue#>``, but it can't be something that already exists.  Using something like ``yyyy-mm-dd_hh-mm-ss``, substituting in the date and time, is probably the safest.)    The ``extension`` should either ``docs`` or the name of your package (cf: :ref:`minimal`), based on whether you made changes to the actual code, or just to the docs.  (If you did both, use your package name.)  This will create a file ``changes/<Issue#>.<extension>.rst``.  Edit that file and put in a short one-line desription of what you've done.  (TODO: describe issue reference.)

So, for example, if your package is ``guide``, and you have created an Issue in the github repo that is Issue #42 ("adding a new feature that provides the answer to the ultimate question of life, the universe, and everything"), then you should run ``towncrier create 42.guide``.  That will create a file ``changes/42.guide.rst``.  You might then edit that file and replace its contents with::

  added the answer (Issue #42)


