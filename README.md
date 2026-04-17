# customer-funnel-analysis
End-to-end customer funnel and revenue leakage analysis using SQL and Python

## 📌 Business Problem

Companies often lose revenue due to hidden drop-offs in the customer funnel 
(sign-up → engagement → conversion → purchase).

This project simulates a real-world digital product and analyzes:
- Where users drop out of the funnel
- Which acquisition channels perform best
- How much revenue is lost due to funnel inefficiencies

## 📊 Dataset

The dataset is **synthetically generated** to reflect real-world European user behavior.

### Data Characteristics
- ~2,000 users
- Multiple sessions per user
- Funnel events: visit → signup → add_to_cart → purchase
- Revenue in GBP (£)
- Dimensions:
  - Country (UK, DE, FR, NL, ES, IT)
  - Acquisition channel (organic, paid search, email, social, referral)
  - Device type (desktop, mobile, tablet)

The data is stored in a SQLite database:
data/raw/funnel.db

## 🛠️ Tech Stack

- **Python** (data generation & analysis)
- **SQLite** (relational database)
- **SQL** (funnel & revenue analysis)
- **Pandas** (data manipulation)
- **Jupyter Notebook** (analysis & visualization)
- **VS Code** (development)
- **Git & GitHub** (version control)

## 📁 Project Structure
customer-funnel-analysis/
├── notebooks/        # Python analysis notebook
├── sql/              # Funnel & revenue SQL queries
├── src/              # Data generation script
├── reports/          # Executive summary
├── data/
│   └── raw/           # SQLite database (funnel.db)
├── requirements.txt
└── README.md

## 🔍 Key Analysis

- Funnel conversion rates (visit → signup → purchase)
- Revenue leakage identification
- Channel-level performance comparison
- Country-level user behavior
- Device-based conversion trends

This analysis helps stakeholders identify high-impact optimization opportunities.

## 📈 Key Insights

- Organic traffic generated the highest number of users but lower conversion than paid search
- Paid search showed stronger purchase intent despite lower traffic volume
- Significant revenue leakage occurs between signup and add-to-cart stages
- Mobile users showed lower conversion compared to desktop users

## ▶️ How to Run

1. Create a virtual environment
2. Install dependencies: pip install -r requirements.txt
3. Generate the dataset: python src/generate_data.py
4. Open the notebook: notebooks/01_funnel_analysis.ipynb

## 📄 Executive Report

A business-friendly executive summary is available here:
➡️ [View Report](reports/report.md)

---

📌 **Note:**  
This project was designed to reflect real-world data analyst workflows used in European tech companies.




