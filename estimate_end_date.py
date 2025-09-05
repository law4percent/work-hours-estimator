"""
Calculate the end date given a start date and estimated hours.
Excludes weekends (Sat & Sun).
Reference: 2 days = 15.0 hours → 7.5 hours per day.
"""

from datetime import datetime, timedelta

def calculate_end_date(start_date_str, estimated_hours):
    hours_per_day = 15.0 / 2.0  # 7.5 hrs/day

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    full_days = int(estimated_hours // hours_per_day)
    remaining_hours = estimated_hours % hours_per_day

    current_date = start_date
    days_counted = 0

    while days_counted < full_days:
        if current_date.weekday() < 5:  # Mon–Fri
            days_counted += 1
        if days_counted < full_days:
            current_date += timedelta(days=1)

    if remaining_hours > 0:
        while current_date.weekday() >= 5:  # Skip Sat & Sun
            current_date += timedelta(days=1)
        current_date += timedelta(days=1)

    return current_date


# Example usage
if __name__ == "__main__":
    start = "2025-09-01"
    hours = 18.0
    end_date = calculate_end_date(start, hours)
    print(f"Start: {start}, Hours: {hours} -> End Date: {end_date.strftime('%Y-%m-%d')}")
