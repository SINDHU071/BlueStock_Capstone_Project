
-- 10 Analytical SQL Queries
-- BlueStock Mutual Fund Analytics

-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT strftime('%Y-%m', date) AS month,
       ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. SIP Transactions by Year
SELECT strftime('%Y', transaction_date) AS year,
       COUNT(*) AS sip_count,
       ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- 4. Transactions by State
SELECT state,
       COUNT(*) AS total_transactions,
       ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC
LIMIT 10;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

-- 6. Top 5 Funds by 3 Year Return
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 7. Transaction Count by Type
SELECT transaction_type,
       COUNT(*) AS count,
       ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Average NAV by Fund
SELECT amfi_code,
       ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC
LIMIT 5;

-- 9. KYC Verified vs Pending
SELECT kyc_status,
       COUNT(*) AS count
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Transactions by Age Group
SELECT age_group,
       COUNT(*) AS total_transactions,
       ROUND(AVG(amount_inr), 2) AS avg_amount
FROM fact_transactions
GROUP BY age_group
ORDER BY total_transactions DESC;
