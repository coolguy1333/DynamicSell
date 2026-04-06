# DynamicSell Overview

DynamicSell is a lightweight dynamic-pricing engine for shop systems.

## Goal

Help servers balance buy/sell activity by making prices react to stock pressure:

- **Low stock** -> price increases.
- **High stock** -> price decreases.

## Core model

`pressure = (target_stock - stock) / target_stock`

`multiplier = 1 + pressure * elasticity`

Final price = `base_price * clamp(multiplier, min_multiplier, max_multiplier)`.

## Where to start

- Read `README.md` for setup.
- Use the CLI for quick tests.
- Import `dynamicsell.engine.calculate_price` in plugin adapters.
