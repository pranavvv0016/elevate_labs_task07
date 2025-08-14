# 📊 Elevate Labs – Task 07: Basic Sales Summary from SQLite Database

This repository contains the solution for **Task 07** of the Data Analyst Internship at Elevate Labs.  
It demonstrates how to:
- Create and populate a small SQLite database (`sales_data.db`)
- Query total quantity sold and revenue per product using SQL inside Python
- Display results in the terminal
- Visualize revenue using a simple bar chart with `matplotlib`

---

## 📂 Project Structure
| File | Description |
|------|-------------|
| `T07.py` | Creates the SQLite database and inserts sample sales data |
| `T_07.py` | Connects to the database, runs SQL queries, prints results, and generates a bar chart |
| `sales_data.db` | SQLite database created by `T07.py` |
| `README.md` | Project documentation |

---

## 🛠 Tools & Libraries
- **Python** (3.8+)
- **sqlite3** – For database creation & querying
- **pandas** – For loading SQL results into a DataFrame
- **matplotlib** – For creating the bar chart

Install required Python packages:
```bash
pip install pandas matplotlib
```
🚀 How to Run
```
1️⃣ Step 1 – Create the Database

Run:

python T07.py


This will:

Create the sales table

Insert sample products (laptop, mouse, keyboard) with quantity & price
```

2️⃣ Step 2 – Query & Visualize Data
```
Run:

python T_07.py


This will:

Connect to sales_data.db
```

Run the SQL query
```
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
```
Print the summary table in the terminal

Display a bar chart of Total Revenue by Product

📸 Example Output

```
Terminal Output:

   product  total_qty  revenue
0  keyboard          3    225.0
1    laptop          3   3600.0
2     mouse          7    175.0
```
🎯 Learning Outcomes

```
By completing this task, you will:

Create and populate a SQLite database using Python

Write and run SQL queries inside Python

Use pandas to handle query results

Create visualizations with matplotlib
```
👤 Author
```
Pranav Narsingoju
GitHub: @pranavvv0016
```
