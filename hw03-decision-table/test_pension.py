from datetime import date

import pytest

import pension

fileName = "result_table.txt"

def setup_module(module):
    table = open(fileName, "w")
    table.writelines("age | salary | years_teaching | app_date\n")


@pytest.mark.parametrize(
    'age, salary, years_teaching, app_date',
    [
        (63, 80000, 20, date(2019, 4, 4)),
    ],
)
def test_pension_result(age, salary, years_teaching, app_date):
    result = pension.calculate_annual_pension(age, salary, years_teaching, app_date)
    table = open(fileName, "a")
    table.write("{} | {} | {} | {} |\n".format(age, salary, years_teaching, age))
