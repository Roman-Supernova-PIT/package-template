<!-- If this PR closes a GitHub issue, reference it here by its number -->
Closes #

<!-- describe the changes included with this PR here -->
This PR addresses ...

<!-- if you can't perform these tasks due to permissions, please ask a maintainer to do them -->
## Tasks
- [ ] **request a review from someone specific**, to avoid making the maintainers review every PR
- [ ] Does this PR change user-facing code / API? (if not, label with `no-changelog-entry-needed`)
  - [ ] write news fragment(s) in `changes/`: `echo "changed something" > changes/<PR#>.<changetype>.rst` (see below for change types) 
  - [ ] update or add relevant tests
  - [ ] update relevant docstrings and / or `docs/` page
    - [ ] Do truth files need to be updated?

<details><summary>news fragment change types...</summary>

- ``changes/<PR#>.general.rst``: infrastructure or miscellaneous change
- ``changes/<PR#>.docs.rst``
</details>