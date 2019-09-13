import datetime


def calculate_annual_pension(age: int, salary: int, years_teaching: int, app_date: datetime.date):
    if app_date < datetime.date(2010, 6, 11) or salary == 0:
        return 0
    if age >= 63:
        multiplier = 1.016
    elif age + years_teaching >= 80:
        multiplier = 1.0155
    else:
        return 0
    adjusted_salary = salary * multiplier if salary <= 90000 else (90000 * multiplier) + (salary - 90000 * 1.015)
    result = (years_teaching / 100) * adjusted_salary
    print(result)
    return result
