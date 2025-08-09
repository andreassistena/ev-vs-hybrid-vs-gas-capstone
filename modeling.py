import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Generate sample dataset
np.random.seed(42)
n_samples = 100
X = np.random.rand(n_samples, 1) * 10  # Feature: e.g., vehicle weight in 1000s lbs
y = 50 - 2 * X + np.random.randn(n_samples, 1) * 2  # Target: e.g., MPG

# Convert to DataFrame for readability
df = pd.DataFrame({'Vehicle_Weight': X.flatten(), 'MPG': y.flatten()})
print("Sample of the generated dataset:")
print(df.head())

# Split the data
X_train, X_test, y_train, y_test = train_test_split(df[['Vehicle_Weight']], df['MPG'], test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Coefficients:")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Slope: {model.coef_[0]:.2f}")
print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual MPG')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted MPG')
plt.title('Linear Regression Model: MPG vs Vehicle Weight')
plt.xlabel('Vehicle Weight (in 1000s lbs)')
plt.ylabel('MPG')
plt.legend()
plt.tight_layout()
plt.savefig('linear_regression_model.png')
plt.show()