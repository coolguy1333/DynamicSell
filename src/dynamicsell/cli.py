"""CLI entry-point for DynamicSell."""

from __future__ import annotations

import argparse

from .engine import PriceInputs, calculate_price


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Calculate DynamicSell prices")
    parser.add_argument("base_price", type=float, help="Base item price")
    parser.add_argument("stock", type=int, help="Current stock")
    parser.add_argument("target_stock", type=int, help="Target stock level")
    parser.add_argument("--elasticity", type=float, default=0.35)
    parser.add_argument("--min-multiplier", type=float, default=0.5)
    parser.add_argument("--max-multiplier", type=float, default=2.5)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = calculate_price(
        PriceInputs(
            base_price=args.base_price,
            stock=args.stock,
            target_stock=args.target_stock,
            elasticity=args.elasticity,
            min_multiplier=args.min_multiplier,
            max_multiplier=args.max_multiplier,
        )
    )
    print(f"price={result.price} multiplier={result.multiplier:.3f} pressure={result.pressure:.3f}")


if __name__ == "__main__":
    main()
