📊 BlueStock Mutual Fund Analytics — Capstone Project

![GitHub last commit](https://img.shields.io/github/last-commit/SINDHU071/BlueStock_Capstone_Project)
![GitHub repo size](https://img.shields.io/github/repo-size/SINDHU071/BlueStock_Capstone_Project)

End-to-end mutual fund analytics platform covering data ingestion,
cleaning, SQL database design, performance metrics, advanced risk
analytics, and an interactive Power BI dashboard.

---

## 🗂️ Project Structure
BlueStock_Capstone_Project/

│

├── data/

│   ├── raw/                          # Original source CSV files

│   └── processed/                    # Cleaned, analysis-ready CSVs

│

├── notebooks/

│   ├── Day1_Data_Ingestion.ipynb

│   ├── Day_2_Cleaned_data_+_SQLite_DB_loaded.ipynb

│   ├── EDA_Analysis.ipynb

│   ├── Day4_Performance_Analytics.ipynb

│   ├── Advanced_Analytics.ipynb

│   └── bluestock_mf_dashboard.pbix

│

├── reports/

│   ├── charts/

│   ├── DASHBOARD1.png                # Industry Overview

│   ├── DASHBOARD2.png                # Fund Performance

│   ├── DASHBOARD3.png                # Investor Analytics

│   ├── DASHBOARD4.png                # SIP & Market Trends

│   ├── POWERBI_DASHBOARD.pdf         # Exported dashboard PDF

│   ├── Final_Report.pdf              # 15–20 page project report

│   ├── Bluestock_MF_Presentation.pptx  # 12-slide presentation

│   ├── fund_scorecard.csv

│   ├── alpha_beta.csv

│   ├── var_cvar_report.csv

│   ├── benchmark_comparison.png

│   └── chart_daily_return_dist.png

│

├── scripts/

│   ├── data_ingestion.py

│   ├── live_nav_fetch.py

│   └── recommender.py

│

├── bluestock_mf.db

├── schema.sql

├── queries.sql

└── data_dictionary.md

---

## 📋 Project Overview

This capstone analyzes **40 mutual fund schemes** across **10 Indian
fund houses** using 4 years of data (2022–2026).

| Metric | Value |
|--------|-------|
| Funds analyzed | 40 schemes |
| Fund houses | 10 AMCs |
| Data period | Jan 2022 – Apr 2026 |
| NAV records | 150,000+ rows |
| Investor transactions | 10,000+ records |
| Dashboard pages | 4 interactive pages |

### 🏆 Key Results

| Metric | Top Performer | Value |
|--------|--------------|-------|
| Best 3yr CAGR | Axis Midcap Fund | 35.11% |
| Best Sharpe Ratio | Mirae Asset Large Cap | 1.4483 |
| Composite Rank #1 | ICICI Pru Midcap | Score: 100/100 |
| Worst Max Drawdown | SBI Small Cap | −52.57% |

---

## 🛠️ Setup Instructions

### Requirements

- Python 3.9+
- Google Colab (recommended) or Jupyter Notebook
- Power BI Desktop — [Download free](https://powerbi.microsoft.com/desktop/)

### Install Dependencies

```bash
pip install pandas numpy scipy plotly sqlalchemy matplotlib
```

### Google Drive Folder Setup
MyDrive/

└── MutualFundAnalytics/

├── Data/

│   ├── Raw/        ← paste raw CSVs here

│   └── Processed/

└── Reports/

---

## ▶️ How to Run the ETL Pipeline

Run notebooks in this order in Google Colab:

| Step | Notebook | Output |
|------|----------|--------|
| 1 | Day1_Data_Ingestion.ipynb | Raw data loaded, explored |
| 2 | Day_2_Cleaned_data_+_SQLite_DB_loaded.ipynb | Clean CSVs + SQLite DB |
| 3 | EDA_Analysis.ipynb | Charts saved to reports/charts/ |
| 4 | Day4_Performance_Analytics.ipynb | fund_scorecard.csv, alpha_beta.csv |
| 5 | Advanced_Analytics.ipynb | var_cvar_report.csv |

---

## 📊 How to Open the Dashboard

### Power BI Desktop (Full Interactive)

1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/)
2. Open `notebooks/bluestock_mf_dashboard.pbix`
3. Navigate using bottom tabs:
   - **Industry Overview** → KPIs, AUM trend, AUM by AMC
   - **Fund Performance** → Risk-return scatter, scorecard table
   - **Investor Analytics** → State, age group, transaction patterns
   - **SIP & Market Trends** → SIP vs Nifty dual-axis, category heatmap

### Quick View (No install)

| Page | Screenshot |
|------|-----------|
| Industry Overview | `reports/DASHBOARD1.png` |
| Fund Performance | `reports/DASHBOARD2.png` |
| Investor Analytics | `reports/DASHBOARD3.png` |
| SIP & Market Trends | `reports/DASHBOARD4.png` |
| Full PDF | `reports/POWERBI_DASHBOARD.pdf` |

---

## 📁 Dataset Descriptions

| File | Description | Key Columns |
|------|-------------|-------------|
| raw/02_nav_history.csv | Daily NAV for 40 schemes | amfi_code, date, nav |
| raw/07_scheme_performance.csv | Fund metrics & ratings | return_3yr_pct, sharpe_ratio, risk_grade |
| raw/08_investor_transactions.csv | Investor transactions | transaction_type, amount_inr, state, age_group |
| raw/04_monthly_sip_inflows.csv | Monthly SIP inflows | month, sip_inflow_crore |
| raw/10_benchmark_indices.csv | NIFTY50 & NIFTY100 | index_name, date, close_value |
| reports/fund_scorecard.csv | Composite scorecard | amfi_code, score_100, final_rank |
| reports/alpha_beta.csv | OLS regression results | amfi_code, alpha, beta, r_squared |
| reports/var_cvar_report.csv | Risk metrics | amfi_code, var_95, cvar_95 |

---

## 📈 Performance Metrics Explained

| Metric | Formula | What it means |
|--------|---------|---------------|
| CAGR | (NAV_end/NAV_start)^(1/n) − 1 | Annualised growth rate |
| Sharpe | (Rp−Rf) / Std × √252 | Return per unit of total risk |
| Sortino | (Rp−Rf) / DownsideStd × √252 | Return per unit of downside risk |
| Alpha | OLS intercept × 252 | Excess return vs benchmark |
| Beta | OLS slope | Market sensitivity |
| Max Drawdown | min(NAV/peak − 1) | Worst peak-to-trough loss |
| VaR (95%) | 5th percentile of returns | Daily loss threshold |
| CVaR | Mean of returns below VaR | Expected loss on worst days |

---

## 🔧 Scripts

### recommender.py — Fund Recommendation Engine

```bash
python scripts/recommender.py
```
Enter risk appetite (Low / Moderate / High): Moderate
Top 3 Recommended Funds:

Mirae Asset Large Cap  — Sharpe: 1.45  Return: 16.2%
HDFC Top 100           — Sharpe: 1.21  Return: 14.8%
SBI Bluechip           — Sharpe: 0.88  Return: 12.4%


### live_nav_fetch.py — Live NAV Fetcher

```bash
python scripts/live_nav_fetch.py
```
Fetches current NAV for all 40 schemes from the AMFI public API.

### data_ingestion.py — Raw Data Loader

```bash
python scripts/data_ingestion.py
```
Loads and validates all raw CSVs, prints data quality summary.

---

## 🗄️ Database Schema

Star Schema with 5 tables:
fact_transactions ──→ dim_fund      (amfi_code)

──→ dim_investor  (investor_id)

──→ dim_date      (date)
fact_nav          ──→ dim_fund      (amfi_code)

──→ dim_benchmark (date)

- Full DDL → `schema.sql`
- Query library (10 queries) → `queries.sql`
- Column definitions → `data_dictionary.md`

---

## 📄 Deliverables

| Deliverable | Location | Status |
|-------------|----------|--------|
| Cleaned datasets | data/processed/ | ✅ |
| SQLite database | bluestock_mf.db | ✅ |
| SQL query library | queries.sql | ✅ |
| Performance Analytics notebook | notebooks/ | ✅ |
| Advanced Analytics notebook | notebooks/ | ✅ |
| Power BI Dashboard (.pbix) | notebooks/ | ✅ |
| Dashboard PDF | reports/POWERBI_DASHBOARD.pdf | ✅ |
| Fund Scorecard | reports/fund_scorecard.csv | ✅ |
| Alpha/Beta report | reports/alpha_beta.csv | ✅ |
| VaR/CVaR report | reports/var_cvar_report.csv | ✅ |
| Final Report (15–20 pages) | reports/Final_Report.pdf | ✅ |
| Presentation (12 slides) | reports/Bluestock_MF_Presentation.pptx | ✅ |

---

## 👤 Author

**SINDHU071**
BlueStock Fintech — Data Analytics Capstone
June 2026
