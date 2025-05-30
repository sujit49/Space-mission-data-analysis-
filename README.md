# 🚀 Space Missions Data Analysis using Python

This project performs a complete data analysis pipeline on historical space mission data. It explores trends in launches, success rates, launch costs, launch locations, and companies. It includes data cleaning, exploratory data analysis (EDA), visualizations, summary statistics, and saves the processed data for future use.

---

## 📌 Features

* **Data Loading & Cleaning:**

  * Loads the `space_missions.csv` dataset.
  * Cleans the column names (e.g., removing newline characters, standardizing names).
  * Converts the `Date` column to datetime format and extracts `Year` and `Month`.
  * Cleans the `Price` column by removing non-numeric symbols and converting to float.

* **Exploratory Data Analysis (EDA):**

  * Displays the first few rows and summary statistics of the dataset.
  * Shows the number of missions per year using a bar plot.
  * Visualizes the distribution of mission status (Success, Failure, etc.).
  * Displays success rate over time as a line chart.
  * Shows the top 10 companies by number of missions.
  * Analyzes rocket status distribution (Active vs Retired).
  * Shows the top 10 launch locations.
  * Plots the average mission cost per year (if data is available).

* **Data Output:**

  * Saves a cleaned and enriched version of the dataset as `processed_space_missions.csv`.

---

## 📁 File Structure

* `space_missions.csv`: Original raw dataset
* `space_missions_analysis.py`: Main script for analysis, visualization, and preprocessing
* `processed_space_missions.csv`: Output file with cleaned and enhanced data
* `README.md`: Project documentation (this file)

---

## 📦 Prerequisites

Ensure the following libraries are installed:

```bash
pip install pandas matplotlib seaborn
```

---

## ▶️ How to Run the Script

1. Make sure the file `space_missions.csv` is in the same directory as `space_missions_analysis.py`.

2. Open a terminal or command prompt and navigate to the project folder.

3. Run the script:

```bash
python space_missions_analysis.py
```

4. The script will output:

   * Initial dataset preview and statistics
   * Cleaned column names and new columns (`Year`, `Month`)
   * Visualizations (displayed in separate windows)
   * Total missions, overall success rate, and average mission cost
   * A new file named `processed_space_missions.csv` will be saved

---

## 🔁 Workflow Overview

1. **Load Data:** Import the space mission dataset from CSV.

2. **Clean Data:**

   * Standardize column names.
   * Convert date to datetime and extract year/month.
   * Clean and convert cost data.

3. **Explore & Visualize:**

   * Plot number of missions per year.
   * Show mission success/failure distribution.
   * Plot success rate and mission costs over time.
   * Display top companies and launch locations.

4. **Save Output:** Store cleaned data to `processed_space_missions.csv`.

---

## 💡 Potential Enhancements

* **Country-wise Analysis:** Group mission data by country to analyze global trends.
* **Predictive Modeling:** Predict mission success based on company, location, cost, etc.
* **Interactive Dashboard:** Use Streamlit or Dash for web-based interactive exploration.
* **More Charts:** Add pie charts, stacked bars, and time series visualizations.
* **Time Series Forecasting:** Predict future launches or budgets using past data.

---

## 🙌 Acknowledgments

* **Dataset Source:** \[Public Dataset – UCI / Kaggle / Wikipedia / SpaceX]
* **Developed by:** *Your Name Here*
