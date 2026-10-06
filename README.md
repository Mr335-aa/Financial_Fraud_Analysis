# Financial Fraud Analysis

## Overview

Financial Fraud Analysis is a Python-based application that analyzes transaction data and identifies potentially suspicious transactions using rule-based fraud detection.

The application validates and cleans transaction data, analyzes financial transactions, calculates fraud scores, assigns risk levels, and generates visual reports.

## Features

- Transaction data loading from CSV
- Data validation
- Data cleaning
- Basic transaction analysis
- Rule-based fraud detection
- Fraud risk scoring
- LOW, MEDIUM and HIGH risk classification
- Fraud analytics
- Suspicious transaction identification
- Data visualization
- Exception handling

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- CSV

## Project Structure

Financial_Fraud_Analysis/

├── data/
│   └── transactions.csv

├── main.py
├── data_loader.py
├── validator.py
├── fraud_detector.py
├── analyzer.py
├── visualizer.py
├── requirements.txt
└── README.md

## How It Works

Transaction Data
        ↓
Data Validation
        ↓
Data Cleaning
        ↓
Basic Analysis
        ↓
Fraud Detection
        ↓
Fraud Score
        ↓
Risk Level
        ↓
Fraud Analytics
        ↓
Charts and Report

## Fraud Detection

The application uses rule-based indicators such as:

- Very high transaction amount
- Large transfers
- High-value bank transfers

Transactions matching these conditions receive higher fraud scores.

## Risk Levels

- LOW: Low fraud risk
- MEDIUM: Moderate fraud risk
- HIGH: High fraud risk

## How to Run

Create a virtual environment:

python -m venv .venv

Activate the environment:

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py

## Disclaimer

This project is an academic demonstration of rule-based fraud analysis. It does not represent a production-level banking fraud detection system.