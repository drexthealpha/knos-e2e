# knos-e2e

A tiny repository used to rehearse Knos end to end on Solana devnet: an issue is funded with one comment, a pull
request is checked, merged and paid to its author's GitHub account. Nothing here is real money.

`slugify(title)` in `slug.py` turns a title into a URL slug: lowercase words joined by single hyphens, for example
`slugify("Hello World")` gives `hello-world`.

Run `pytest` from the repository root. The tests are in the `tests/` folder.

Contributions: open a pull request that closes an issue.

Checked on 3 Nov 2026: a pull request here runs knos-check.yml, which calls the published check.yml at 96b243f1.
