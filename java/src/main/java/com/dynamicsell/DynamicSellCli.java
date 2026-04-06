package com.dynamicsell;

public final class DynamicSellCli {
    private DynamicSellCli() {
    }

    public static void main(String[] args) {
        if (args.length < 3 || args.length > 6) {
            System.err.println("Usage: java -jar dynamicsell.jar <basePrice> <stock> <targetStock> [elasticity] [minMultiplier] [maxMultiplier]");
            System.exit(2);
        }

        double basePrice = Double.parseDouble(args[0]);
        int stock = Integer.parseInt(args[1]);
        int targetStock = Integer.parseInt(args[2]);
        double elasticity = args.length >= 4 ? Double.parseDouble(args[3]) : 0.35;
        double minMultiplier = args.length >= 5 ? Double.parseDouble(args[4]) : 0.5;
        double maxMultiplier = args.length >= 6 ? Double.parseDouble(args[5]) : 2.5;

        PriceInputs inputs = new PriceInputs(basePrice, stock, targetStock, elasticity, minMultiplier, maxMultiplier);
        PriceResult result = PricingEngine.calculatePrice(inputs);

        System.out.printf("price=%.2f multiplier=%.3f pressure=%.3f%n", result.price(), result.multiplier(), result.pressure());
    }
}
