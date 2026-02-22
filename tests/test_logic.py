import os
import pytest
import tempfile
from app import logic


@pytest.fixture
def temp_data_file(monkeypatch):
    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        temp_file = tmp.name

    # Override DATA_FILE in logic.py
    monkeypatch.setattr(logic, "DATA_FILE", temp_file)

    yield temp_file

    # Cleanup
    if os.path.exists(temp_file):
        os.remove(temp_file)


def test_add_expense(temp_data_file):
    logic.add_expense(100, "Food")
    expenses = logic.load_expenses()

    assert len(expenses) == 1
    assert expenses[0]["amount"] == 100
    assert expenses[0]["category"] == "Food"


def test_calculate_total(temp_data_file):
    logic.add_expense(100, "Food")
    logic.add_expense(200, "Travel")

    total = logic.calculate_total()
    assert total == 300


def test_negative_amount(temp_data_file):
    with pytest.raises(ValueError):
        logic.add_expense(-50, "Invalid")
