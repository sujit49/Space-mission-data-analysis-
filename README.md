🚀 Space Missions Data Analysis using Python
This project performs a complete data analysis pipeline on historical space mission data. It explores trends in launches, success rates, launch costs, launch locations, and companies. It includes data cleaning, exploratory data analysis (EDA), visualizations, summary statistics, and saves the processed data for future use.

📌 Features
Data Loading & Cleaning:

Loads the space_missions.csv dataset.

Cleans the column names (e.g., removing newline characters, standardizing names).

Converts the Date column to datetime format and extracts Year and Month.

Cleans the Price column by removing non-numeric symbols and converting to float.

Exploratory Data Analysis (EDA):

Displays the first few rows and summary statistics of the dataset.

Shows the number of missions per year using a bar plot.

Visualizes the distribution of mission status (Success, Failure, etc.).

Displays success rate over time as a line chart.

Shows the top 10 companies by number of missions.

Analyzes rocket status distribution (Active vs Retired).

Shows the top 10 launch locations.

Plots the average mission cost per year (if data is available).

Data Output:

Saves a cleaned and enriched version of the dataset as processed_space_missions.csv.

📁 File Structure
space_missions.csv: Original raw dataset.

space_missions_analysis.py: Main script for analysis, visualization, and preprocessing.

processed_space_missions.csv: Output file with cleaned and enhanced data.

README.md: Project documentation file (you are reading it!).

📦 Prerequisites
Ensure the following libraries are installed before running the script:

bash
Copy
Edit
pip install pandas matplotlib seaborn
▶️ How to Run the Script
Make sure the file space_missions.csv is in the same directory as space_missions_analysis.py.

Open a terminal or command prompt and navigate to the project folder.

Run the script:

bash
Copy
Edit
python space_missions_analysis.py
The script will output:

Initial dataset preview and statistics.

Cleaned column names and new columns (Year, Month).

Visualizations (displayed in separate windows).

Total missions, overall success rate, and average mission cost.

A new file named processed_space_missions.csv will be saved with the cleaned data.

🔁 Workflow Overview
Load Data: Import the space mission dataset from CSV.

Clean Data:

Standardize column names.

Convert date to datetime and extract year/month.

Clean and convert cost data.

Explore & Visualize:

Plot number of missions per year.

Show mission success/failure distribution.

Plot success rate and mission costs over time.

Display top companies and launch locations.

Save Output:

Store cleaned data to processed_space_missions.csv.

💡 Potential Enhancements
Country-wise Analysis: Group mission data by country to analyze space race trends globally.

Predictive Modeling: Use ML models to predict mission success based on input features like company, location, price, etc.

Interactive Dashboard: Build a Streamlit or Plotly Dash web app for exploring the data interactively.

Hyperparameter Analysis: If extended to classification tasks, use GridSearchCV for tuning.

Time Series Forecasting: Predict future space missions or costs using historical trends.

🙌 Acknowledgments
Dataset Source: [Public Dataset — UCI / Kaggle / SpaceX / Wikipedia]

Developed by: Your Name
