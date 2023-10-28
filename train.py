# Step 4: Use sklearn and tensorflow libraries to build and train a machine learning model that can predict the future trends and risks of cyberattacks based on the data.

# Import the necessary modules
import pandas as pd
import numpy as np
import sklearn
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load the data from the database into a pandas DataFrame
df = pd.read_sql("SELECT * FROM predictor_cyberattack", "sqlite:///db.sqlite3")

# Convert the date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Extract the features and the target from the DataFrame
X = df[["date", "country", "region", "type", "source", "target"]]
y = df["impact"]

# Encode the categorical features using LabelEncoder and OneHotEncoder
le = LabelEncoder()
ohe = OneHotEncoder(sparse=False)
X["country"] = le.fit_transform(X["country"])
X["region"] = le.fit_transform(X["region"])
X["type"] = le.fit_transform(X["type"])
X["source"] = le.fit_transform(X["source"])
X["target"] = le.fit_transform(X["target"])
X = ohe.fit_transform(X)

# Scale the features using StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a neural network model using tensorflow.keras
model = Sequential()
model.add(Dense(64, activation="relu", input_shape=(X.shape[1],)))
model.add(Dropout(0.2))
model.add(Dense(32, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(16, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(5, activation="softmax"))

# Compile the model with loss, optimizer, and metrics
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the model with the train set
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate the model with the test set
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)
print(f"Test accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Confusion matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"Classification report:\n{classification_report(y_test, y_pred)}")
