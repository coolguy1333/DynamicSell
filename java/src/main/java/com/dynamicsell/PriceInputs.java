package com.dynamicsell;

public record PriceInputs(
        double basePrice,
        int stock,
        int targetStock,
        double elasticity,
        double minMultiplier,
        double maxMultiplier
) {
    public PriceInputs {
        if (basePrice <= 0) {
            throw new IllegalArgumentException("basePrice must be > 0");
        }
        if (stock < 0 || targetStock <= 0) {
            throw new IllegalArgumentException("stock must be >= 0 and targetStock must be > 0");
        }
        if (elasticity < 0 || elasticity > 2) {
            throw new IllegalArgumentException("elasticity must be between 0 and 2");
        }
        if (minMultiplier <= 0 || maxMultiplier < minMultiplier) {
            throw new IllegalArgumentException("invalid multiplier bounds");
        }
    }

    public PriceInputs(double basePrice, int stock, int targetStock) {
        this(basePrice, stock, targetStock, 0.35, 0.5, 2.5);
    }
}
