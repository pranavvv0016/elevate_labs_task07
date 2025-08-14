import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database file.
conn = sqlite3.connect("sales_data.db")

# Define the SQL query to calculate total quantity and revenue for each product.
# We use SUM() for aggregation and GROUP BY to group the results by product.
query = "SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales GROUP BY product"

# Use pandas to run the query and load the results into a DataFrame.
df = pd.read_sql_query(query, conn)

# Close the database connection.
conn.close()

# Print the resulting DataFrame to display the summary.
print(df)

# Create a simple bar chart from the DataFrame.
# The x-axis will be 'product' and the y-axis will be 'revenu
df.plot(kind='bar', x='product', y='revenue', title='Total Revenue by Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.xticks(rotation=0) # Keeps product names horizontal

# Show the plot.
plt.tight_layout()
plt.show()

# (Optional) Save the chart to a file.
# [cite_start]plt.savefig("sales_chart.png") [cite: 25]