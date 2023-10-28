# Step 3: Use pandas and numpy libraries to process and analyze the data and generate descriptive statistics and insights.

# Import the necessary modules
import pandas as pd
import numpy as np

# Load the data from the database into a pandas DataFrame
df = pd.read_sql("SELECT * FROM predictor_cyberattack", "sqlite:///db.sqlite3")

# Convert the date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Calculate the number of attacks per country
country_counts = df["country"].value_counts()

# Calculate the number of attacks per type
type_counts = df["type"].value_counts()

# Calculate the number of attacks per month
month_counts = df.groupby(df["date"].dt.month).size()

# Calculate the average impact score per country
# Assume that the impact column is a categorical variable with values from 1 (low) to 5 (high)
df["impact"] = df["impact"].astype("category")
df["impact"] = df["impact"].cat.reorder_categories(["1", "2", "3", "4", "5"], ordered=True)
df["impact"] = df["impact"].cat.codes + 1
country_impacts = df.groupby("country")["impact"].mean()

# Print some descriptive statistics and insights
print(f"The total number of cyberattacks reported is {len(df)}.")
print(f"The most affected country is {country_counts.idxmax()} with {country_counts.max()} attacks.")
print(f"The most common type of cyberattack is {type_counts.idxmax()} with {type_counts.max()} attacks.")
print(f"The month with the highest number of cyberattacks is {month_counts.idxmax()} with {month_counts.max()} attacks.")
print(f"The country with the highest average impact score is {country_impacts.idxmax()} with {country_impacts.max():.2f}.")
