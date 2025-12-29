# 🏗️ Civil Engineering Automation Tools

A collection of Python scripts designed to automate repetitive tasks in construction management, focusing on **Quality Control (QC)** and **Cost Estimation**.

## 🚀 Projects Overview

### 1. Automated Steel Material Verification (QC)
Located in: `/01_Steel_Verification`
* **Objective:** Automate the verification of steel cross-sections and weights against TIS/ASTM standards.
* **Problem Solved:** Reduces human error in manual catalog lookup and prevents non-compliant material usage.
* **Key Features:**
    * Parses structural lists from Excel.
    * Cross-references with standard weight tables.
    * Flags anomalies (>5% tolerance) instantly.

### 2. Algorithmic Concrete & Material Estimation
Located in: `/02_Concrete_Estimation`
* **Objective:** Calculate precise concrete volumes and steel requirements based on construction activities (Flooring, Precast, Leveling).
* **Problem Solved:** Optimizes ordering schedules and minimizes material waste.
* **Key Features:**
    * Applies specific waste factors based on task type (e.g., 5% for flooring vs 2% for precast).
    * Generates summary reports by construction zone.

## 🛠️ Technologies
* **Language:** Python 3.9+
* **Libraries:** Pandas, NumPy, OpenPyXL

## ⚠️ Data Privacy Note
The Excel files provided in the `data_samples` folder contain **mock-up data** generated for demonstration purposes only. No actual project data or sensitive information from Sino-Thai / CPF is included.

---
*Developed by [ใส่ชื่อคุณตรงนี้]*
