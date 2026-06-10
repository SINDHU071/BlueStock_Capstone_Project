"""
recommender.py — Simple Mutual Fund Recommender
Usage: python recommender.py
"""

import pandas as pd
import os

# ── Config ──────────────────────────────────────────────
DATA_PATH = '/content/drive/MyDrive/MutualFundAnalytics/Reports'
# For local use, change to your folder:
# DATA_PATH = r'C:\Users\YourName\MutualFundAnalytics\Reports'
# ────────────────────────────────────────────────────────


def load_data(path: str) -> pd.DataFrame:
    csv = os.path.join(path, 'clean_scheme_performance.csv')
    if not os.path.exists(csv):
        raise FileNotFoundError(f'File not found: {csv}')
    return pd.read_csv(csv)


def recommend_funds(performance: pd.DataFrame, risk_appetite: str) -> pd.DataFrame:
    """
    Input : risk_appetite — 'Low', 'Moderate', or 'High'
    Output: Top 3 funds by Sharpe ratio within matching risk_grade
    """
    risk_appetite = risk_appetite.strip().title()

    risk_map = {
        'Low'      : ['Low', 'Low to Moderate'],
        'Moderate' : ['Moderate', 'Moderately High'],
        'High'     : ['High', 'Very High', 'Moderately High']
    }

    if risk_appetite not in risk_map:
        print('❌ Invalid input. Choose from: Low, Moderate, High')
        return pd.DataFrame()

    grades   = risk_map[risk_appetite]
    filtered = performance[performance['risk_grade'].isin(grades)].copy()

    # Fallback: partial string match
    if filtered.empty:
        filtered = performance[
            performance['risk_grade'].str.contains(risk_appetite, case=False, na=False)
        ].copy()

    if filtered.empty:
        print(f'⚠️  No funds found for risk grade: {risk_appetite}')
        return pd.DataFrame()

    top3 = filtered.sort_values('sharpe_ratio', ascending=False).head(3)
    result = top3[[
        'scheme_name', 'category', 'risk_grade',
        'sharpe_ratio', 'return_3yr_pct',
        'expense_ratio_pct', 'aum_crore'
    ]].reset_index(drop=True)
    result.index += 1
    return result


def main():
    print('=' * 60)
    print('   Mutual Fund Recommender — Bluestock Fintech')
    print('=' * 60)

    try:
        performance = load_data(DATA_PATH)
        print(f'✅ Loaded {len(performance)} funds\n')
    except FileNotFoundError as e:
        print(f'❌ {e}')
        print('   Update DATA_PATH in this script to your folder.')
        return

    while True:
        print('\nEnter risk appetite (Low / Moderate / High) or "quit" to exit:')
        user_input = input('>>> ').strip()

        if user_input.lower() in ('quit', 'exit', 'q'):
            print('Goodbye!')
            break

        result = recommend_funds(performance, user_input)
        if not result.empty:
            print(f'\n📌 Top 3 Recommended Funds for {user_input.title()} Risk:\n')
            print(result.to_string())
            print()


if __name__ == '__main__':
    main()
