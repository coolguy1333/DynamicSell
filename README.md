# DynamicSell

DynamicSell is an addon-oriented dynamic pricing toolkit that can be embedded into economy or shop plugins.

## Features

- Deterministic pricing engine based on stock pressure.
- Python package + CLI for simulation and balancing.
- Semantic versioning with a single source-of-truth version file.
- GitHub release artifacts (wheel + source tarball + checksums).
- Unit tests and CI workflow.

## Install

From source:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

From a tagged GitHub release artifact:

```bash
pip install https://github.com/example/DynamicSell/releases/download/v0.1.1/dynamicsell-0.1.1-py3-none-any.whl
```

## Quick usage

Calculate a price from the command line:

```bash
dynamicsell 100 15 50 --elasticity 0.4
```

Example output:

```text
price=128.0 multiplier=1.280 pressure=0.700
```

## Project layout

- `src/dynamicsell/engine.py` - core pricing logic.
- `src/dynamicsell/cli.py` - command-line interface.
- `src/dynamicsell/_version.py` - package version source of truth.
- `tests/` - automated tests.
- `docs/overview.md` - concept docs.
- `docs/releasing.md` - release process.

## Release process

1. Update `src/dynamicsell/_version.py` and `CHANGELOG.md`.
2. Commit changes and create tag (example: `v0.1.1`).
3. Push branch and tag to GitHub.
4. The `Release` workflow builds artifacts and publishes a GitHub release.

See `docs/releasing.md` for details.

## License

MIT. See `LICENSE`.
