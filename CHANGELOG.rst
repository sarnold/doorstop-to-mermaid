Changelog
=========


0.2.0 (2025-07-31)
------------------

Changes
~~~~~~~
- Refactor create_diagram and move it from script to module. [Stephen L
  Arnold]

  * update script to use new import, refactor test
- Reset dogfood diagram for (re)rendering. [Stephen L Arnold]
- Add end-to-end diagram test, cleanup lint and mypy config. [Stephen L
  Arnold]

  * adjust expected results for test_gen_diagram on windows
- Revert readme format from markdown back to reStructuredText. [Stephen
  L Arnold]

  * cleanup tox dev env, docs sources, and test bits, remove README.md


0.1.1 (2025-07-31)
------------------

Changes
~~~~~~~
- Generate a changelog and add it to docs build. [Stephen L Arnold]


0.1.0 (2025-06-25)
------------------

New
~~~
- Complete initial caller script example, add diagram. [Stephen L
  Arnold]

  * update swd and readme docs, cleanup tox file
- Add SubGraph helper class and helper methods, update docs. [Stephen L
  Arnold]

  * add helper methods and tests for handling node and subgraph labels
  * update design and reqs items, add a new test item the above
- Add doorstop unittest doc, start linking to parent reqs. [Stephen L
  Arnold]

  * add generated doc sources, cleanup docs build
  * exclude docs/ from pre-commit end-of-file fixer
- Add mermaid subclass and convenience func with some tests. [Stephen L
  Arnold]

  * update project requirements and readme, add mypy config to expose
    python-to-mermaid type hints
  * cleanup tox cmds, uncomment doorstop REQ doc
- Add initial doorstop reqs, add md output to sphinx sources. [Stephen L
  Arnold]
- Add a helper func and a test, update readme and pytest cfg. [Stephen L
  Arnold]

  * switch to myst_parser and cleanup doc sources
  * add missing docs help to process md files in CI

Changes
~~~~~~~
- Cleanup deps, imports, and config exceptions. [Stephen L Arnold]

  * improve mypy analysis, ignore missing local package for pre-commit
    but include scripts dir in tox and pre-commit
- Cleanup docs build and pre-commit configs, update design stub.
  [Stephen L Arnold]

  * revert diagram directive to (re)render traceability diagram
- Remove old readme and update markdown version. [Stephen L Arnold]
- Revert extra class methods, add skeleton caller script. [Stephen L
  Arnold]

  * add scripts dir to tox envs, temporarily allow unused imports
    in script file
- Try some coverage env adjustments. [Stephen L Arnold]
- Add __iter__ methods to helper classes, make them generators. [Stephen
  L Arnold]

  * update requirements and design items
- Add subgraph loop diagram output, update tests and readme. [Stephen L
  Arnold]
- Update initial design doc, revert yaml dep to just munch. [Stephen L
  Arnold]
- Move doorstop from extras to (full) dependencies. [Stephen L Arnold]

  * make it an install dep since we already need it for runtime and
    several other workflows
  * revert diagram directive to force rerendering the svg
  * exclude swd items from pre-commit end-of-file fixer
- Add check for doorstop cmd and a test, add to test deps. [Stephen L
  Arnold]
- Revert graph so we can render it again, cleanup deps and docs.
  [Stephen L Arnold]
- Add another design doc stub with links and references. [Stephen L
  Arnold]
- Update and review some doorstop items, freshen links. [Stephen L
  Arnold]
- Add override version of to_mermaid, update tests. [Stephen L Arnold]
- Do not keep generated sources, move path deeper, ignore md files.
  [Stephen L Arnold]

  * treat doorstop docs just like api docs, clean instead of keep
  * reset diagram commit with thicker lines
- Add initial doorstop sw design doc, include source in sphinx. [Stephen
  L Arnold]

  * mermaid action parse error, this is a misleading error msg
  * this was due to missing asset directories in docs/ tree
- Convert readme to markdown, update pre-commit and docs. [Stephen L
  Arnold]
- Un-template the readme and prep for converting to markdown. [Stephen L
  Arnold]
- Cleanup workflow branch names, GH default is main, update readme.
  [Stephen L Arnold]

Fixes
~~~~~
- Cleanup design doc after pulling diagram workflow. [Stephen L Arnold]
- Cleanup markup and make virtualenv name safe for doorstop. [Stephen L
  Arnold]
- Rename test bits to avoid name clashes in doorstop docs. [Stephen L
  Arnold]


0.0.0 (2025-06-07)
------------------
- Initial commit. [Stephen L Arnold]
