
"""The Patient class — the OOP heart of the project."""

from clinic import validators


class Patient:
    """One validated patient visit record."""

    def __init__(
        self,
        patient_id: str,
        name: str,
        age: int,
        department: str,
        consultation_fee: float,
        visit_date: str,
    ):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.department = department
        self.consultation_fee = consultation_fee
        self.visit_date = visit_date

    @property
    def consultation_fee(self) -> float:
        return self._consultation_fee

    @consultation_fee.setter
    def consultation_fee(self, value: float):
        if value < 0:
            raise ValueError("consultation_fee cannot be negative")
        self._consultation_fee = value

    @classmethod
    def from_csv_row(cls, row: dict) -> "Patient":
        """Validate and convert one raw CSV row into a Patient."""
        patient_id = row.get("patient_id", "").strip()
        visit_date = row.get("visit_date", "").strip()

        if not patient_id:
            raise validators.InvalidRecordError("patient_id is missing")

        if not visit_date:
            raise validators.InvalidRecordError("visit_date is missing")

        name = validators.clean_name(row.get("name", ""))
        age = validators.parse_age(row.get("age", ""))
        department = validators.clean_department(
            row.get("department", "")
        )
        consultation_fee = validators.parse_fee(
            row.get("consultation_fee", row.get("fee", ""))
        )

        return cls(
            patient_id=patient_id,
            name=name,
            age=age,
            department=department,
            consultation_fee=consultation_fee,
            visit_date=visit_date,
        )

    def to_dict(self) -> dict:
        """Return the six fields needed by JSON and CSV writers."""
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "consultation_fee": self.consultation_fee,
            "visit_date": self.visit_date,
        }

    def __repr__(self) -> str:
        return (
            f"Patient({self.patient_id}, {self.name}, "
            f"{self.department})"
        )


if __name__ == "__main__":
    demo = Patient(
        "P999", "Test Person", 30, "General", 500.0, "2026-08-12"
    )
    print("Self-test:", demo)
