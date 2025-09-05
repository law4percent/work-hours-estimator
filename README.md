# Work Hours Estimator (Python)

This project provides two Python scripts to help calculate **working hours and dates** while excluding weekends (Saturday & Sunday).  
The system assumes **2 days = 15.0 hours**, or **7.5 hours per working day**.

---

## 📂 Project Structure

```
work-hours-estimator/
├── estimate_hours.py       # Version 1: Start & End date → Hours + Days
├── estimate_end_date.py    # Version 2: Start date & Hours → End date
└── README.md               # Documentation
```

---

## 📌 Files

### 1. `estimate_hours.py`
- **Input:** Start date, End date  
- **Output:** Estimated working hours and equivalent days  

**Code:**
```python
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
```

**Example:**
```bash
python estimate_hours.py
```

Output:
```
Estimated Hours from 2025-09-01 to 2025-09-02: 15.00 hr == 2.00 days
```

### 2. `estimate_end_date.py`
- **Input:** Start date, Estimated hours
- **Output:** The computed end date

**Code:**
```python
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
```

**Example:**
```bash
python estimate_end_date.py
```

Output:
```
Start: 2025-09-01, Hours: 18.0 -> End Date: 2025-09-03
```

---

## ⚡ Features

- Excludes Saturdays and Sundays automatically
- Flexible date range calculations
- Supports inclusive start & end date counting

---

## 🛠 Requirements

- Python 3.8+ (uses `datetime` and `timedelta` modules only)

---

## 📌 Author

Developed by **Lawrence P. Roble** (2025) 🚀