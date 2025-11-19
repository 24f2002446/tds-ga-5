# chart.py
# Generates a professional Seaborn barplot (512x512 PNG)
# Author: 24f2002446@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------
# Generate realistic business data
# ---------------------------
np.random.seed(42)

products = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
sales = np.random.randint(80, 180, size=len(products))
growth_rate = np.random.uniform(2.0, 12.0, size=len(products))

df = pd.DataFrame({
    "Product": products,
    "Quarterly Sales (k units)": sales,
    "Growth (%)": growth_rate
})

# ---------------------------
# Seaborn styling
# ---------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # professional presentation scale

# ---------------------------
# Create 512 × 512 px figure
# figsize=(8,8) with dpi=64 → 512px
# ---------------------------
plt.figure(figsize=(8, 8), dpi=64)

# ---------------------------
# Barplot
# ---------------------------
sns.barplot(
    data=df,
    x="Product",
    y="Quarterly Sales (k units)",
    palette="Blues_d",
    edgecolor="black"
)

# ---------------------------
# Professional labels & title
# ---------------------------
plt.title("Quarterly Product Performance — Sales Overview", fontsize=18, pad=15)
plt.xlabel("Product Line", fontsize=14)
plt.ylabel("Sales (in thousands of units)", fontsize=14)

# Annotate bars with values
for index, value in enumerate(df["Quarterly Sales (k units)"]):
    plt.text(
        index,
        value + 2,
        f"{value}",
        ha="center",
        fontsize=12
    )

# ---------------------------
# Save Export — EXACT 512x512
# ---------------------------
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("chart.png generated successfully (512x512 px)")
