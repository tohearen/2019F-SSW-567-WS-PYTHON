from datetime import date

import pytest
from prettytable import PrettyTable

import pension

table = PrettyTable()


def setup_module(module):
    table.field_names = ["Age", "Salary", "Years Teaching", "Retirement Application Date",
                         "Eligible For Incentive", "Annual Pension", "Retirement"]


def teardown_module(module):
    print(table)
    open("pension_table.html", "w").write(table.get_html_string())


@pytest.mark.parametrize(
    'age, salary, years_teaching, app_date',
    [
        (63, 80000, 20, date(2008, 4, 4)),
        (63, 80000, 40, date(2008, 4, 4)),
        (70, 75000, 30, date(2011, 4, 4)),
        (73, 90000, 40, date(2008, 4, 4)),
        (60, 95000, 36, date(2008, 4, 5)),
        (50, 110000, 22, date(2008, 4, 5)),
        (55, 100000, 30, date(2007, 4, 5)),
        (55, 75000, 30, date(2007, 4, 5)),
        (45, 75000, 20, date(2007, 4, 5)),
        (66, 110000, 45, date(2007, 4, 5)),
        (66, 90000, 40, date(2007, 4, 5)),
        (66, 100000, 35, date(2007, 4, 5)),
        (66, 100000, 35, date(2011, 4, 5)),
        (60, 100000, 35, date(2002, 4, 5)),
        (60, 160000, 45, date(2011, 4, 5)),
        (80, 60000, 50, date(2002, 4, 5)),
        (80, 160000, 50, date(2002, 4, 5)),
        (80, 170000, 55, date(2002, 4, 5)),
    ],
)
def test_pension_decision_table(age, salary, years_teaching, app_date):
    annual_pension = pension.calculate_annual_pension(age, salary, years_teaching, app_date)
    recommendation = pension.get_retirement_recommendation(annual_pension)
    eligible_for_incentive = pension.eligible_for_incentive(app_date)
    table.add_row([age, salary, years_teaching, app_date, eligible_for_incentive, annual_pension, recommendation])
