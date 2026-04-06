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

## Implementations

- Python package (`src/dynamicsell`) for scripting and integration.
- Java package (`java/src/main/java/com/dynamicsell`) for JVM/plugin ecosystems.

Both implementations intentionally use the same formula and defaults, and parity is tested in CI.
