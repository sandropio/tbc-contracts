import pandas as pd
from helpers import parse_contracts, calculate_day_sinlastloan, calculate_tot_claim_cnt_l180d, calculate_disb_bank_loan_wo_tbc

# Load data from CSV
data = pd.read_csv('data.csv')


# Initialize lists to store calculated features
ids = []
tot_claim_cnt_l180d = []
disb_bank_loan_wo_tbc = []
day_sinlastloan = []

for index, row in data.iterrows():
    contracts = parse_contracts(row['contracts'])

    # Calculate features
    claim_cnt = calculate_tot_claim_cnt_l180d(contracts)
    loan_sum = calculate_disb_bank_loan_wo_tbc(contracts)
    days_since_loan = calculate_day_sinlastloan(contracts, row['application_date'])

    # Append calculated features to lists
    ids.append(row['id'])
    tot_claim_cnt_l180d.append(claim_cnt)
    disb_bank_loan_wo_tbc.append(loan_sum)
    day_sinlastloan.append(days_since_loan)

# Create DataFrame for features
features_df = pd.DataFrame({
    'id': ids,
    'tot_claim_cnt_l180d': tot_claim_cnt_l180d,
    'disb_bank_loan_wo_tbc': disb_bank_loan_wo_tbc,
    'day_sinlastloan': day_sinlastloan
})

# Export to CSV
features_df.to_csv('contract_features.csv', index=False)
