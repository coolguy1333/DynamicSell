from dynamicsell.engine import PriceInputs, calculate_price


def test_original_example_output_regression() -> None:
    result = calculate_price(
        PriceInputs(base_price=100.0, stock=15, target_stock=50, elasticity=0.4)
    )
    assert result.price == 128.0
    assert round(result.multiplier, 3) == 1.28
    assert round(result.pressure, 3) == 0.7
