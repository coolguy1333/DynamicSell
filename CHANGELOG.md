# Changelog

All notable changes to this project will be documented in this file.

## [0.1.3] - 2026-04-06
### Added
- Regression test locking the original pricing example output.
- Python/Java parity test to confirm the jar behavior matches the original Python engine.

### Changed
- CI now builds `dynamicsell.jar` and runs parity tests using the built jar.

## [0.1.2] - 2026-04-06
### Added
- Java implementation of the pricing engine and CLI.
- `scripts/build-jar.sh` to produce `dist/dynamicsell.jar`.
- Release workflow support for including jar artifacts.

### Changed
- Release docs and README now document jar build/run/download flow.

## [0.1.1] - 2026-04-05
### Added
- Single-source version module at `src/dynamicsell/_version.py`.
- Release checksum generation (`checksums.txt`) for downloadable artifact verification.

### Changed
- Build metadata now reads version dynamically from package source.
- Release docs and README now document exact version bump/tag/download flow.

## [0.1.0] - 2026-04-05
### Added
- Initial `dynamicsell` source package with price engine and CLI.
- Basic test suite.
- Release workflow and contributor documentation.
