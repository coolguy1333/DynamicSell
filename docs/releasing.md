# Releasing DynamicSell

## Versioning

DynamicSell follows semantic versioning:

- `MAJOR`: breaking changes
- `MINOR`: backward-compatible features
- `PATCH`: bug fixes

The Python package version is stored in `src/dynamicsell/_version.py` and read dynamically by `pyproject.toml` during builds.

## Release flow

1. Update `CHANGELOG.md`.
2. Bump `__version__` in `src/dynamicsell/_version.py`.
3. Commit and tag: `git tag vX.Y.Z`.
4. Push branch and tag.
5. GitHub Actions builds wheel + source tarball + `dynamicsell.jar`, creates `checksums.txt`, and publishes a GitHub Release.
6. If `PYPI_API_TOKEN` is configured, Python artifacts are uploaded to PyPI.

## Conflict-safe workflow notes

- `ci.yml` always builds the jar and runs parity tests with `DYNAMICSELL_JAR=dist/dynamicsell.jar`.
- `release.yml` supports manual dry-runs via `workflow_dispatch`, but publishing is limited to semver tags.

## Download verification

Each release uploads a `checksums.txt` file so users can verify downloaded artifacts:

```bash
sha256sum -c checksums.txt
```

## Required GitHub secrets

- `PYPI_API_TOKEN` for publish job (optional if you only want GitHub Releases).
