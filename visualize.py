# Step 5: Use matplotlib and seaborn libraries to create visualizations of the data and the predictions, such as charts, graphs, maps, tables, etc.

# Import the necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the database into a pandas DataFrame
df = pd.read_sql("SELECT * FROM predictor_cyberattack", "sqlite:///db.sqlite3")

# Convert the date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Load the prediction model from a file
model = tf.keras.models.load_model("cyberattack_model.h5")

# Predict the impact scores for the entire data
X = df[["date", "country", "region", "type", "source", "target"]]
y = df["impact"]
X["country"] = le.transform(X["country"])
X["region"] = le.transform(X["region"])
X["type"] = le.transform(X["type"])
X["source"] = le.transform(X["source"])
X["target"] = le.transform(X["target"])
X = ohe.transform(X)
X = sc.transform(X)
y_pred = model.predict(X)
y_pred = np.argmax(y_pred, axis=1) + 1

# Add the prediction column to the DataFrame
df["prediction"] = y_pred

# Plot a bar chart of the number of attacks per country
plt.figure(figsize=(10, 6))
sns.countplot(x="country", data=df, order=df["country"].value_counts().index)
plt.title("Number of cyberattacks per country")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.show()

# Plot a pie chart of the number of attacks per type
plt.figure(figsize=(10, 6))
sns.countplot(x="type", data=df, order=df["type"].value_counts().index)
plt.title("Number of cyberattacks per type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.show()

# Plot a line chart of the number of attacks per month
plt.figure(figsize=(10, 6))
sns.lineplot(x=df["date"].dt.month, y="id", data=df, estimator="count")
plt.title("Number of cyberattacks per month")
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()

# Plot a scatter plot of the actual vs predicted impact scores
plt.figure(figsize=(10, 6))
sns.scatterplot(x="impact", y="prediction", data=df)
plt.title("Actual vs predicted impact scores")
plt.xlabel("Actual impact score")
plt.ylabel("Predicted impact score")
plt.show()

# Plot a heatmap of the confusion matrix
plt.figure(figsize=(10, 6))
sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt="d", cmap="Blues")
plt.title("Confusion matrix")
plt.xlabel("Predicted impact score")
plt.ylabel("Actual impact score")
plt.show()
