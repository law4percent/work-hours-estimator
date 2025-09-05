# work-hours-estimator

📌 README.md
# Work Hours Estimator (Python)

This project provides two Python scripts to help calculate **working hours and dates** while excluding weekends (Saturday & Sunday).  
The system assumes **2 days = 15.0 hours**, or **7.5 hours per working day**.

---

## 📂 Files

### 1. `estimate_hours.py`
- **Input:** Start date, End date  
- **Output:** Estimated working hours and equivalent days  

**Example:**
```bash
python estimate_hours.py


Output:

Estimated Hours from 2025-09-01 to 2025-09-02: 15.00 hr == 2.00 days

2. estimate_end_date.py

Input: Start date, Estimated hours

Output: The computed end date

Example:

python estimate_end_date.py


Output:

Start: 2025-09-01, Hours: 18.0 -> End Date: 2025-09-03

⚡ Features

Excludes Saturdays and Sundays automatically

Flexible date range calculations

Supports inclusive start & end date counting

🛠 Requirements

Python 3.8+ (uses datetime and timedelta modules only)

📌 Author

Developed by Lawrence P. Roble (2025) 🚀


---

Do you also want me to **merge both versions into a single CLI tool** (with options `--mode hours` or `--mode enddate`) so you can just run one file instead of two?
