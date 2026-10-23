# MediCare Patient Records Manager

A Python-based patient records management system that validates and cleans CSV data, rejects invalid and duplicate records, generates clean JSON reports, and summarizes consultation revenue by department.

## Project Overview

The MediCare Patient Records Manager processes raw patient visit data exported from a clinic. It cleans inconsistent names, validates ages and consultation fees, checks required fields, detects duplicate patient IDs, and produces structured reports for further analysis.

## Features

- **Data validation:** Validates patient names, ages, departments, and consultation fees.
- **Data cleaning:** Standardizes patient names and department names.
- **Error handling:** Identifies invalid records and records rejection reasons.
- **Duplicate detection:** Prevents duplicate patient IDs from being processed.
- **JSON output:** Exports validated patient records to JSON.
- **Revenue analysis:** Calculates total consultation revenue and revenue by department.
- **Input protection:** Preserves the original CSV input data.

## Technologies Used

- Python
- CSV data processing
- JSON
- Object-oriented programming
- `tabulate` for terminal tables

## Project Structure

```text
medicare-records-starter/
├── clinic/
│   ├── __init__.py
│   ├── validators.py
│   ├── models.py
│   └── storage.py
├── data/
│   └── patients_raw.csv
├── reports/
│   ├── patients_clean.json
│   └── summary.json
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

The `reports/` directory is generated when the program runs and is excluded from Git tracking.

## Requirements

- Python 3.13 or a compatible Python version
- `uv` or `pip`

## Installation

Clone the repository:

```bash
git clone https://github.com/Mohammed2776/medicare-records-starter.git
cd medicare-records-starter
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, if you use `uv` and have configured your virtual environment, run the project with the Python interpreter from that environment.

## Run the Project

```bash
python main.py
```

The program reads the raw CSV data, validates the records, displays a patient table, and generates clean JSON output and a revenue summary.

## Generated Reports

- `reports/patients_clean.json` — validated patient records.
- `reports/summary.json` — valid record count, rejected row count, total revenue, and revenue grouped by department.

## Validation Rules

The application checks that patient IDs and visit dates are present, ages are within the accepted range, consultation fees are non-negative, and required text fields are valid. Duplicate patient IDs are rejected.

## Future Improvements

- Add automated unit tests with `pytest`.
- Validate visit dates.
- Export rejected records with explanations.
- Add department-based filtering.
- Improve terminal output with richer formatting.

## Data Privacy

Use only synthetic or anonymized patient data in this repository. Never publish real patient records, credentials, or other confidential information.

## License

This project is distributed under the license included in the repository.