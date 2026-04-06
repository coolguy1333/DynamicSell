from dynamicsell.engine import PriceInputs, calculate_price


def test_price_increases_when_stock_is_low() -> None:
    result = calculate_price(PriceInputs(base_price=10, stock=10, target_stock=100))
    assert result.price > 10


def test_price_decreases_when_stock_is_high() -> None:
    result = calculate_price(PriceInputs(base_price=10, stock=140, target_stock=100))
    assert result.price < 10


def test_price_clamps_to_bounds() -> None:
    result = calculate_price(
        PriceInputs(
            base_price=10,
            stock=0,
            target_stock=100,
            elasticity=2,
            max_multiplier=2,
        )
    )
    assert result.multiplier == 2
    assert result.price == 20
