"""
Estimate working hours between two dates (excluding weekends).
Reference: 2 days = 15.0 hours → 7.5 hours per day.
"""

from datetime import datetime, timedelta

def calculate_estimated_hours(start_date_str, end_date_str, inclusive=True):
    hours_per_day = 15.0 / 2.0  # 7.5 hrs/day

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    if end_date < start_date:
        raise ValueError("End date must be after or equal to start date")

    total_days = (end_date - start_date).days + (1 if inclusive else 0)

    working_days = 0
    for i in range(total_days):
        current_day = start_date + timedelta(days=i)
        if current_day.weekday() < 5:  # Mon–Fri
            working_days += 1

    estimated_hours = working_days * hours_per_day
    estimated_days = estimated_hours / hours_per_day
    return estimated_hours, estimated_days


# Example usage
if __name__ == "__main__":
    start = "2025-09-01"
    end = "2025-09-02"
    hours, days = calculate_estimated_hours(start, end)
    print(f"Estimated Hours from {start} to {end}: {hours:.2f} hr == {days:.2f} days")
