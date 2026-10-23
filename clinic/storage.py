
"""Reading raw CSV data and writing clean outputs (Module 8 skills)."""

import csv
import json
from pathlib import Path

from clinic.models import Patient
from clinic.validators import InvalidRecordError


def load_patients(csv_path: Path) -> tuple[list[Patient], list[str]]:
    """Read the raw CSV and return (clean_patients, error_messages)."""
    patients: list[Patient] = []
    errors: list[str] = []
    seen_ids: set[str] = set()

    with csv_path.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for line_number, row in enumerate(reader, start=2):
            try:
                patient = Patient.from_csv_row(row)
            except InvalidRecordError as exc:
                errors.append(f"line {line_number}: {exc}")
                continue

            patient_id = str(patient.patient_id)

            if patient_id in seen_ids:
                errors.append(
                    f"line {line_number}: duplicate patient_id {patient_id}"
                )
                continue

            seen_ids.add(patient_id)
            patients.append(patient)

    return patients, errors


def write_clean_json(patients: list[Patient], out_path: Path) -> None:
    """Save validated records as human-readable JSON."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(
            [patient.to_dict() for patient in patients],
            f,
            indent=2,
            ensure_ascii=False,
        )


def write_summary(
    patients: list[Patient],
    errors: list[str],
    out_path: Path,
) -> dict:
    """Compute and save the business summary."""
    revenue_by_department: dict[str, float] = {}

    for patient in patients:
        department = patient.department
        revenue_by_department[department] = (
            revenue_by_department.get(department, 0.0) + patient.consultation_fee
        )

    revenue_by_department = {
        department: round(total, 2)
        for department, total in revenue_by_department.items()
    }

    summary = {
        "valid_records": len(patients),
        "rejected_rows": len(errors),
        "total_revenue": round(sum(p.consultation_fee for p in patients), 2),
        "revenue_by_department": revenue_by_department,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    return summary
