# 📊 Elevate Labs – Task 07: Basic Sales Summary from SQLite Database

This project is part of the **Data Analyst Internship** at Elevate Labs.  
It demonstrates how to connect Python to a SQLite database, run basic SQL queries, summarize sales data, and visualize the results using `matplotlib`.

---

## 🚀 Objective
Use SQL inside Python to pull simple sales info (like total quantity sold & total revenue) from a small SQLite database (`sales_data.db`) and display:
1. Results in the terminal.
2. A simple bar chart of revenue per product.

---

## 🛠 Tools & Libraries Used
- **Python** (3.8+)
- **sqlite3** – Database connection
- **pandas** – Data manipulation
- **matplotlib** – Data visualization

---

## 📂 Project Structure
| File | Description |
|------|-------------|
| `T07.py` | Main Python script for connecting to DB, running queries, and generating chart |
| `T_07.py` | Alternative version of the script |
| `sales_data.db` | SQLite database containing the sales table |
| `total_revenue.png` | Bar chart visualization of total revenue per product |
| `README.md` | Project documentation |

---

## 📊 SQL Query Used
```sql
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
📸 Output Example
Terminal Output: A table showing total quantity and revenue for each product.
```
Visualization:
```
⚙️ How to Run the Project
Clone the repository

bash
Copy
Edit
git clone https://github.com/pranavvv0016/elevate_labs_task07.git
cd elevate_labs_task07
Install required packages

bash
Copy
Edit
pip install pandas matplotlib
Run the script

bash
Copy
Edit
python T07.py
View Output

Results will print in the terminal.

Bar chart will be saved as total_revenue.png.
```
🎯 Learning Outcomes
```
By completing this task, you will:

Connect Python to a SQLite database

Write and execute basic SQL queries

Perform data aggregation with GROUP BY

Visualize results using matplotlib
```
📬 Contact
```
Author: Pranav Narsingoju
GitHub: @pranavvv0016
```
