"""Pricing engine used by DynamicSell."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PriceInputs:
    """Input values used to compute item price updates."""

    base_price: float
    stock: int
    target_stock: int
    elasticity: float = 0.35
    min_multiplier: float = 0.5
    max_multiplier: float = 2.5


@dataclass(frozen=True)
class PriceResult:
    """Result of a DynamicSell price calculation."""

    price: float
    multiplier: float
    pressure: float


def _clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(value, upper))


def calculate_price(inputs: PriceInputs) -> PriceResult:
    """Calculate dynamic price from stock pressure.

    Higher stock than target decreases prices, while lower stock increases prices.
    """

    if inputs.base_price <= 0:
        raise ValueError("base_price must be > 0")
    if inputs.stock < 0 or inputs.target_stock <= 0:
        raise ValueError("stock must be >= 0 and target_stock must be > 0")
    if not 0 <= inputs.elasticity <= 2:
        raise ValueError("elasticity must be between 0 and 2")
    if inputs.min_multiplier <= 0 or inputs.max_multiplier < inputs.min_multiplier:
        raise ValueError("invalid multiplier bounds")

    pressure = (inputs.target_stock - inputs.stock) / inputs.target_stock
    multiplier = 1 + (pressure * inputs.elasticity)
    multiplier = _clamp(multiplier, inputs.min_multiplier, inputs.max_multiplier)
    price = round(inputs.base_price * multiplier, 2)

    return PriceResult(price=price, multiplier=multiplier, pressure=pressure)
