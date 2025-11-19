# employee_analysis.py
# Contact: 24f2002446@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------
# 1. LOAD DATA
# -----------------------------------------------

data = {
    "employee_id": ["EMP001","EMP002","EMP003","EMP004","EMP005","EMP006","EMP007","EMP008","EMP009","EMP010"],
    "department": ["Operations","R&D","Marketing","HR","Finance","R&D","R&D","HR","Marketing","Finance"],
    "region": ["Europe","Europe","Latin America","Middle East","Asia Pacific","Asia Pacific","Europe","Europe","Latin America","Middle East"],
    "performance_score": [94.3,73.92,61.99,66.32,84.44,79.1,82.4,69.5,72.3,88.9],
    "years_experience": [3,1,2,6,7,4,5,3,2,8],
    "satisfaction_rating": [3.7,3.2,3.9,4.4,3.3,4.1,4.0,3.6,3.8,4.2]
}

df = pd.DataFrame(data)

# -----------------------------------------------
# 2. FREQUENCY COUNT FOR "R&D"
# -----------------------------------------------

rd_count = (df["department"] == "R&D").sum()
print("Frequency count for R&D department:", rd_count)

# -----------------------------------------------
# 3. HISTOGRAM OF DEPARTMENTS
# -----------------------------------------------

plt.figure(figsize=(8, 6))
sns.countplot(x="department", data=df, palette="viridis")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("department_histogram.png")
plt.show()
