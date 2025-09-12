## Query Analysis:
# R1 – Best-Selling Car Models: Global Summary

Top 5 models:

Diamante → 4,180 sales Silhouette → 4,110 sales Prizm → 4,110 sales Passat → 3,910 sales Ram Pickup → 3,830 sales

👉 This shows a strong concentration of sales around a few flagship models.

The distribution is very uneven:

The top models exceed 4,000 sales. Many “long tail” models don’t exceed 1,000 sales (e.g., Corolla 1,090, Altima 850, Elantra 650). Some very marginal models even drop below 200 sales (Mirage 190, Alero 180, Avalon 150, RX300 150, Sebring Conv. 100).

Diamante, Silhouette, and Prizm → clearly dominate the market in your dataset. 👉 These models are likely strategic for manufacturers (high demand or strong marketing strategies).

Catalog diversity:

More than 100 distinct models in your table. But a minority concentrates the majority of sales (Pareto principle → 20% of models ≈ 80% of sales).

# R2: Average Price by Model – Business Interpretation

Clear segmentation into 3 ranges:

Entry-level (< 20k) → e.g., Mirage, Escort, Sentra, Cavalier. 👉 Economical cars, likely for lower-income customers or popular markets.

Mid-range (20k – 35k) → majority of models (Accord, Corolla, Camry, Mustang, Passat, etc.). 👉 This is the core of the market.

High-end / Premium (> 40k) → DeVille, LS400, SC, Catera, Integra, etc. 👉 These models target high purchasing power customers.

Link with the first query:

Diamante, Silhouette, Prizm → in the top sellers but with a rather low average price (~22k – 29k). 👉 This confirms that high volumes mainly come from affordable models.

Catera → highest price (56k) but not in the top sellers. 👉 Typical example of a premium model sold in low volume.

# R3: Transmission Query – Interpretation

Fairly balanced distribution → ~53% Auto vs ~47% Manual. Indicates that manual cars are still very present.

# R4: Body Style Query – Interpretation

SUV + Hatchback = >50% of total market. Sedans are slightly less numerous, but with a higher average price (29.8k) → premium segment. Passenger and Hardtop = niche but still high-end (around 29k).

👉 Insight: SUVs dominate in volume → highly demanded. Sedans and Passenger cars generate more value → customers willing to pay more.

# R5: Dealer Region Query – Interpretation

Austin leads (41k sales, average price ~28.3k). Other regions are close (~31–38k sales each). Average prices are very homogeneous (~28k everywhere).

👉 This suggests that the difference comes more from sales volume than price positioning.

# R6: Monthly Sales Trend – Analysis

Growth 2022–2023:

Early 2022: sales range from 3–8k units per month. End of 2023: reaches 19k sales/month, nearly 6 times more than early 2022 → strong commercial expansion.

Seasonality:

Peaks in November–December (year-end, promotions, holidays). Lows in January–February (usual post-holiday dip).

Stable average price:

Average price fluctuates between 26.7k and 29k USD. Even when volumes surge (end of 2023), the price remains relatively stable → sign that demand doesn’t drive prices down (balanced market).

✅ Conclusion: The market is growing strongly with stable prices. Strategy to retain: intensify sales at year-end and consolidate offerings in Q1.

# R7: Number of Sales by Dealer – Key Observations

Top sellers:

Progressive Shippers Cooperative Association No → 13,180 sales Rabun Used Car Sales → 13,130 sales Race Car Help → 12,530 sales These companies clearly dominate the market in volume.

Average sales:

Between 12,400 and 6,300 sales for most companies. Shows a concentration of small and medium sellers after the leaders.

Low sales:

Classic Chevy, Diehl Motor CO Inc, Enterprise Rent A Car → around 6,200 sales. Probably smaller or specialized dealerships.

Equal volume:

Some companies have exactly the same number of sales (e.g., 12,490 for Star Enterprises Inc and Tri-State Mack Inc). This may indicate similar seasonal sales or groups of companies with equivalent capacity.

Revenue potential analysis:

Column 3 ranges from 27,000 to 28,700. A company with fewer sales may have a higher figure in column 3, suggesting a higher average price per vehicle.

Example: U-Haul CO → 12,470 sales but 28,769 in column 3 → likely more expensive vehicles or rentals.

# R8: Sales Trend Over Time (J) – Detailed Analysis

Clear growth: from 3,150 sales in January 2022 to 19,210 sales in December 2023 → a sixfold increase in 2 years.

Seasonal peaks:

Very strong in September 2022 (14,750), November 2022 (16,200), and December 2023 (19,210). Hypothesis: year-end promotions, new models released in September.

Stable average price:

Always around 27,500 – 28,500 USD → demand increases but prices don’t spike. Slight drop in March 2023 (26,751) → likely promotions or special discounts.

👉 Conclusion: Sales are rising sharply, with regular peaks at year-end. The market is expanding, but average prices remain relatively constant → volume strategy rather than price increase.

# R9: Customer Profile – Detailed Analysis

Customer distribution:

21% women (51k) 79% men (188k) → Market dominated by male buyers.

Average income:

Men: 851k (higher) Women: 755k (slightly lower) → Gap of about 12%.

Average price paid:

Women: 28,277 USD Men: 28,039 USD → Women pay slightly more despite lower income. → Possible interest in better-equipped or newer models.

👉 Conclusion: The market is mainly male, but women tend to buy slightly more expensive models, which may indicate different preferences.
