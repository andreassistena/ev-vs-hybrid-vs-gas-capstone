import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample fuel economy data (you can replace this with your own CSV if desired)
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016],
    'EV_mpg_equivalent': [95, 98, 100, 102, 104, 106, 108],
    'Gasoline_mpg': [25, 26, 27, 27, 28, 28, 29]
}

# Load data into DataFrame
df = pd.DataFrame(data)

# Display the data
print("Sample Fuel Efficiency Data:\n")
print(df)

# Set plot style
sns.set(style="whitegrid")

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='EV_mpg_equivalent', label='EV MPGe', marker='o', color='green')
sns.lineplot(data=df, x='Year', y='Gasoline_mpg', label='Gasoline MPG', marker='o', color='red')
plt.title('Fuel Efficiency Comparison: EV vs Gasoline')
plt.xlabel('Year')
plt.ylabel('Miles Per Gallon (MPG / MPGe)')
plt.legend()
plt.tight_layout()
plt.savefig('fuel_efficiency_comparison.png')
plt.show()