from datetime import date

import pytest

import pension


@pytest.mark.parametrize(
    'age, salary, years_teaching, app_date',
    [
        (63, 80000, 20, date(2019, 4, 4)),
    ],
)
def test_pension_result(age, salary, years_teaching, app_date):
    result = pension.calculate_annual_pension(age, salary, years_teaching, app_date)
    assert result > 0
