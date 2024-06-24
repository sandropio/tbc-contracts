import pandas as pd
import json
from datetime import datetime


def parse_contracts(contracts_json):
    """Parse contracts JSON and handle NaN values gracefully."""
    if pd.isna(contracts_json):
        return []
    try:
        return json.loads(contracts_json)
    except json.JSONDecodeError:
        return []


def calculate_tot_claim_cnt_l180d(contracts):
    """Calculate the number of claims for the last 180 days."""
    count = 0
    for contract in contracts:
        if isinstance(contract, dict):
            claim_date = contract.get('claim_date')
            if claim_date:
                claim_date = pd.to_datetime(claim_date, format='%d.%m.%Y', errors='coerce')
                if claim_date and (datetime.utcnow() - claim_date).days <= 180:
                    count += 1
    return count if count > 0 else -3


def calculate_disb_bank_loan_wo_tbc(contracts):
    """Calculate the sum of exposure of loans without TBC loans."""
    total_sum = 0
    for contract in contracts:
        if isinstance(contract, dict):
            bank = contract.get('bank')
            loan_summa = contract.get('loan_summa')
            contract_date = contract.get('contract_date')

            if bank and bank not in ['LIZ', 'LOM', 'MKO', 'SUG', None] and loan_summa and contract_date:
                total_sum += int(loan_summa)
    return total_sum if total_sum > 0 else -1


def calculate_day_sinlastloan(contracts, application_date):
    """Calculate the number of days since the last loan."""
    last_loan_date = None
    for contract in contracts:
        if isinstance(contract, dict):
            loan_summa = contract.get('loan_summa')
            contract_date = contract.get('contract_date')
            if contract_date and loan_summa:
                contract_date = pd.to_datetime(contract_date, format='%d.%m.%Y', errors='coerce')
                if not pd.isnull(contract_date) and (not last_loan_date or contract_date > last_loan_date):
                    last_loan_date = contract_date

    if last_loan_date:
        # Convert application_date to datetime with UTC timezone if it's not already
        application_date = pd.to_datetime(application_date, utc=True)
        # Make last_loan_date timezone-aware in UTC
        last_loan_date = last_loan_date.tz_localize('UTC')
        days_since_last_loan = (application_date - last_loan_date).days
        return days_since_last_loan if days_since_last_loan >= 0 else -1
    return -1  # If no loans at all
