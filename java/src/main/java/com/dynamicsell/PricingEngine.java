package com.dynamicsell;

public final class PricingEngine {
    private PricingEngine() {
    }

    public static PriceResult calculatePrice(PriceInputs inputs) {
        double pressure = (double) (inputs.targetStock() - inputs.stock()) / inputs.targetStock();
        double multiplier = 1 + (pressure * inputs.elasticity());
        multiplier = clamp(multiplier, inputs.minMultiplier(), inputs.maxMultiplier());
        double price = round2(inputs.basePrice() * multiplier);

        return new PriceResult(price, multiplier, pressure);
    }

    private static double clamp(double value, double lower, double upper) {
        return Math.max(lower, Math.min(value, upper));
    }

    private static double round2(double value) {
        return Math.round(value * 100.0) / 100.0;
    }
}
