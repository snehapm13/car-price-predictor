import pickle
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Import the dataset
df = pd.read_csv("data/cars.csv")

# Step 2: Select input features
X = df[
    [
        "year",
        "km_driven",
        "engine"
    ]
]

# Step 3: Select the target
y = df["selling_price"]

# Step 4: Split the dataset
X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

# Step 5: Create the model
model = LinearRegression()

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Save the trained model
with open(
    "car_price_model.pkl",
    "wb"
) as file:
    pickle.dump(model, file)

print("Model training completed.")
print("car_price_model.pkl created.")