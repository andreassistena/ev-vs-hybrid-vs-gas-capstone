# ev-vs-hybrid-vs-gas-capstone
The goal is to compare EVs to Gas Cars to find best pricing options
EV vs Hybrid vs Gasoline Vehicles: A Data-Driven Comparison
 Project Overview
This project analyzes and compares electric vehicles (EVs), hybrid vehicles, and gasoline-powered vehicles using multiple datasets from government sources and Kaggle. The analysis examines fuel efficiency, energy costs, environmental impact, and petroleum usage trends in the United States.

The project includes:

Data cleaning and preprocessing

Exploratory data analysis (EDA)

Visualizations with Seaborn and Matplotlib

Trend analysis of fuel prices, petroleum production/consumption, and EV charging patterns

 Repository Structure
bash
Copy
Edit
.
├── data/                     # Raw and cleaned datasets
├── epa-capstone/
│   ├── main.py               # Main script
│   ├── modeling.py           # Modeling and analysis functions
│   ├── preprocess.py         # Data cleaning and preprocessing functions
├── notebooks/
│   ├── eda_analysis.ipynb    # Jupyter notebook with EDA and visualizations
├── README.md                 # This file
└── requirements.txt          # Python dependencies
 Installation
Requirements:

Python 3.8+

pip

Setup:

bash
Copy
Edit
# Clone the repository
git clone https://github.com/andreassistena/ev-vs-hybrid-vs-gas-capstone.git

# Navigate into the project folder
cd ev-vs-hybrid-vs-gas-capstone

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Ubuntu/Mac
.venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
 Usage
To run the main analysis:

bash
Copy
Edit
python epa-capstone/main.py
To explore the EDA notebook:

bash
Copy
Edit
jupyter notebook notebooks/eda_analysis.ipynb
Datasets Used
Downloadable Fuel Economy Data – FuelEconomy.gov
https://www.fueleconomy.gov/feg/download.shtml
Electricity Cost Prediction Dataset – Kaggle
https://www.kaggle.com/datasets/shalmamuji/electricity-cost-prediction-dataset
Electric Vehicle Charging Patterns – Kaggle
https://afdc.energy.gov/data/10324
U.S. Production, Consumption, and Trade of Petroleum Products – AFDC
https://afdc.energy.gov/data/10326
Average Retail Fuel Prices in the United States – AFDC
https://afdc.energy.gov/data/10460
Consumption of Natural Gas in the United States – AFDC

Key Insights
EVs show significantly higher MPGe compared to MPG for gasoline vehicles, although direct comparison requires caution due to differing measurement methods.

U.S. petroleum consumption exceeds production, suggesting upward pressure on gasoline prices over time.

Electricity prices have generally declined since the late 20th century, potentially driven by increased renewable energy adoption.

Industrial electricity costs are the highest on average, followed by residential, commercial, and mixed-use.

 References
U.S. Department of Energy – Alternative Fuels Data Center.

FuelEconomy.gov – U.S. Environmental Protection Agency.

Kaggle – Electric Vehicle Charging Patterns dataset.

Kaggle – Electricity Cost Prediction dataset.

 License
This project is released under the MIT License.

 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.
