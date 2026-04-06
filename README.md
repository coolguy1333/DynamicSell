# DynamicSell

DynamicSell is an addon-oriented dynamic pricing toolkit that can be embedded into economy or shop plugins.

## Features

- Deterministic pricing engine based on stock pressure.
- Python package + CLI for simulation and balancing.
- Java CLI packaged as `dynamicsell.jar` for JVM plugin ecosystems.
- Semantic versioning with a single source-of-truth version file.
- GitHub release artifacts (wheel + source tarball + jar + checksums).
- Regression tests lock the original pricing behavior, with Python/Java parity checks.
- CI and release workflows aligned for parity + artifact publishing.

## Install

From source (Python):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

From a tagged GitHub release artifact:

```bash
pip install https://github.com/example/DynamicSell/releases/download/v0.1.4/dynamicsell-0.1.4-py3-none-any.whl
```

## Quick usage

Python CLI:

```bash
dynamicsell 100 15 50 --elasticity 0.4
```

Java JAR build + run:

```bash
./scripts/build-jar.sh
java -jar dist/dynamicsell.jar 100 15 50 0.4
```

Example output:

```text
price=128.00 multiplier=1.280 pressure=0.700
```

## Original behavior guarantee

- `tests/test_regression_original_behavior.py` locks the known original formula output.
- `tests/test_java_parity.py` compares jar output to Python engine output over multiple scenarios.

## Project layout

- `src/dynamicsell/engine.py` - core pricing logic.
- `src/dynamicsell/cli.py` - Python command-line interface.
- `src/dynamicsell/_version.py` - package version source of truth.
- `java/src/main/java/com/dynamicsell/` - Java implementation and jar entry point.
- `scripts/build-jar.sh` - jar build script.
- `tests/` - automated Python tests, including regression/parity coverage.
- `docs/overview.md` - concept docs.
- `docs/releasing.md` - release process.

## Release process

1. Update `src/dynamicsell/_version.py` and `CHANGELOG.md`.
2. Commit changes and create tag (example: `v0.1.4`).
3. Push branch and tag to GitHub.
4. The `Release` workflow builds Python artifacts and `dynamicsell.jar`, then publishes a GitHub release.

See `docs/releasing.md` for details.

## License

MIT. See `LICENSE`.
