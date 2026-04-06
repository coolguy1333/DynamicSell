import re

from dynamicsell import __version__


def test_version_is_semver_like() -> None:
    assert re.match(r"^\d+\.\d+\.\d+$", __version__)
