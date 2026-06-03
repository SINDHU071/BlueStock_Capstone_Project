# Data Dictionary
## BlueStock Mutual Fund Analytics — Day 2

---

## Table: fact_nav
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique fund identifier from AMFI |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value in INR |

---

## Table: fact_transactions
| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Fund identifier |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | T30 or B30 city classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | UPI / Cheque / Mandate |
| kyc_status | TEXT | Verified or Pending |

---

## Table: fact_performance
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Fund identifier |
| scheme_name | TEXT | Full name of the scheme |
| fund_house | TEXT | AMC name |
| category | TEXT | Large Cap / Mid Cap / Small Cap etc |
| return_1yr_pct | REAL | 1 year return percentage |
| return_3yr_pct | REAL | 3 year return percentage |
| return_5yr_pct | REAL | 5 year return percentage |
| expense_ratio_pct | REAL | Annual expense ratio (0.1% to 2.5%) |
| aum_crore | INTEGER | Assets Under Management in crores |
| morningstar_rating | INTEGER | Rating from 1 to 5 |
| risk_grade | TEXT | Low / Moderate / High / Very High |

---

## Table: dim_fund
| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Primary key, unique fund ID |
| scheme_name | TEXT | Full scheme name |
| fund_house | TEXT | AMC / fund house name |
| category | TEXT | Fund category |
| plan | TEXT | Regular or Direct plan |

---

## Table: fact_aum
| Column | Type | Description |
|--------|------|-------------|
| fund_house | TEXT | AMC name |
| aum_crore | REAL | Total AUM in crores |

---

## Sources
- AMFI India (amfiindia.com)
- BlueStock Capstone Project datasets
