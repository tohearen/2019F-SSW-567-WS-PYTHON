import datetime

incentive_cutoff_date = datetime.date(2010, 6, 11)


def eligible_for_incentive(app_date: datetime.date):
    return app_date < datetime.date(2010, 6, 11)


def calculate_annual_pension(age: int, salary: int, years_teaching: int, app_date: datetime.date):
    active_incentive = eligible_for_incentive(app_date)

    if age >= 63:
        base_multiplier = 1.016 if active_incentive else 1
    elif age + years_teaching >= 80:
        base_multiplier = 1.0155 if active_incentive else 1
    else:
        return 0

    if salary <= 90000:
        adjusted_salary = salary * base_multiplier
    else:
        adjusted_salary = (90000 * base_multiplier) + (salary - 90000 * 1.015 if active_incentive else 1)
    return round((years_teaching / 100) * adjusted_salary, 2)


def get_retirement_recommendation(annual_pension: int):
    if annual_pension < 15000:
        return 'BAD'
    elif annual_pension < 25000:
        return 'WEAK'
    elif annual_pension < 35000:
        return 'FAIR'
    elif annual_pension < 45000:
        return 'GOOD'
    else:
        return 'GREAT'
