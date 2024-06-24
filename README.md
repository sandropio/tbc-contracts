# tbc-contracts

## Contents

- [Introduction](#introduction)
- [Data](#data)
- [Features](#features)
- [Requirements](#requirements)


## Introduction

This project involves parsing a dataset (`data.csv`) that contains three columns: `id`, `application_date`, and `contracts`. The `contracts` column is a JSON string that contains information about the contracts a customer has signed up for. The task is to parse this JSON string and calculate a set of features from it.

## Data

The `data.csv` file contains the following columns:
- `id`: The unique identifier for the row.
- `application_date`: The start date of the application.
- `contracts`: A JSON string that contains information about the contracts a customer has signed up for.

## Features

The following features are calculated from the `contracts` JSON string:

1. **tot_claim_cnt_l180d**: Number of claims for the last 180 days.
2. **disb_bank_loan_wo_tbc**: Sum of exposure of loans without TBC loans.
3. **day_sinlastloan**: Number of days since the last loan.

## Requirements

- Python 3.7 or higher
- pandas
- json


