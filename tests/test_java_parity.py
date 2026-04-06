import os
import subprocess

import pytest

from dynamicsell.engine import PriceInputs, calculate_price


@pytest.mark.parametrize(
    ("base_price", "stock", "target_stock", "elasticity", "min_multiplier", "max_multiplier"),
    [
        (10.0, 10, 100, 0.35, 0.5, 2.5),
        (10.0, 140, 100, 0.35, 0.5, 2.5),
        (100.0, 15, 50, 0.4, 0.5, 2.5),
        (55.0, 0, 100, 2.0, 0.5, 2.0),
    ],
)
def test_java_cli_matches_python_engine(
    base_price: float,
    stock: int,
    target_stock: int,
    elasticity: float,
    min_multiplier: float,
    max_multiplier: float,
) -> None:
    jar_path = os.environ.get("DYNAMICSELL_JAR")
    if not jar_path:
        pytest.skip("DYNAMICSELL_JAR not set; skipping java parity check")

    py_result = calculate_price(
        PriceInputs(
            base_price=base_price,
            stock=stock,
            target_stock=target_stock,
            elasticity=elasticity,
            min_multiplier=min_multiplier,
            max_multiplier=max_multiplier,
        )
    )

    completed = subprocess.run(
        [
            "java",
            "-jar",
            jar_path,
            str(base_price),
            str(stock),
            str(target_stock),
            str(elasticity),
            str(min_multiplier),
            str(max_multiplier),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    output = completed.stdout.strip()

    fields = dict(item.split("=") for item in output.split())
    java_price = float(fields["price"])
    java_multiplier = float(fields["multiplier"])
    java_pressure = float(fields["pressure"])

    assert java_price == py_result.price
    assert java_multiplier == pytest.approx(py_result.multiplier, rel=1e-3, abs=1e-3)
    assert java_pressure == pytest.approx(py_result.pressure, rel=1e-3, abs=1e-3)
