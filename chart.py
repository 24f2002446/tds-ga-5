# chart.py
# Generates a professional Seaborn barplot (exact 512x512 PNG)
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

df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

# ---------------------------
# Seaborn styling
# ---------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# ---------------------------
# Create EXACT 512×512 canvas
# figsize(8,8) with dpi=64 → 512 px
# ---------------------------
fig = plt.figure(figsize=(8, 8), dpi=64)

# ---------------------------
# Barplot
# ---------------------------
ax = sns.barplot(
    data=df,
    x="Product",
    y="Sales",
    palette="Blues_d",
    edgecolor="black"
)

# Title & labels
ax.set_title("Quarterly Product Sales", fontsize=18, pad=12)
ax.set_xlabel("Product", fontsize=14)
ax.set_ylabel("Sales (units)", fontsize=14)

# Annotate values
for i, val in enumerate(df["Sales"]):
    ax.text(i, val + 2, str(val), ha="center", fontsize=12)

# ---------------------------
# Force exact size (NO trimming)
# ---------------------------
plt.subplots_adjust(
    left=0.12,
    right=0.95,
    top=0.90,
    bottom=0.12
)

# ---------------------------
# Save EXACT 512x512
# ---------------------------
fig.savefig("chart.png", dpi=64)  # NO bbox_inches!

plt.close()

print("chart.png generated — EXACT 512×512 pixels")
