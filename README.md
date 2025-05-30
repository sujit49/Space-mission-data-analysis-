🚀 Space Missions Data Analysis
Analyze and visualize historical space mission data to gain insights into mission trends, success rates, companies involved, and more using Python.

📁 Project Structure
bash
Copy
Edit
space_missions_analysis/
│
├── space_missions.csv              # Raw dataset
├── processed_space_missions.csv    # Cleaned and enriched dataset (output)
├── space_missions_analysis.py      # Main Python analysis script
└── README.md                       # Documentation
💾 Installation Requirements
Before running the project, ensure you have the following Python libraries installed:

nginx
Copy
Edit
pip install pandas matplotlib seaborn
If you're using additional features (like OCR, audio, or NLP), you might also need:

nginx
Copy
Edit
pip install PyPDF2 pytesseract pdf2image gTTS pygame transformers
📊 Exploratory Data Analysis (EDA) & Insights
This project performs a thorough analysis of global space missions. Key operations include:

Data Cleaning:

Fixes column names by removing line breaks.

Converts Date to datetime format and extracts Year and Month.

Cleans Price values and converts them to numeric for analysis.

Visualizations:

Number of Missions Over Time – Bar plot of mission count per year.

Mission Status Distribution – Bar chart showing counts of Success, Failure, etc.

Success Rate Over Time – Line graph showing yearly success rate (%).

Top 10 Companies by Number of Missions – Most active space companies.

Average Mission Cost Over Time – Yearly trend in mission prices (if data available).

Rocket Status Distribution – Pie chart of active vs retired rockets.

Top 10 Launch Locations – Bar plot of most used launchpads worldwide.

Summary Output (in terminal):

Total number of missions.

Overall success rate.

Average mission cost (if available).

Output File:

Cleaned dataset is saved as processed_space_missions.csv.

✅ How to Run
Ensure space_missions.csv is in the project folder.

Open your terminal or IDE and run:

nginx
Copy
Edit
python space_missions_analysis.py
🛰️ Credits
Dataset Source: [UCI / Kaggle / Public Domain Dataset]
Developed by: Your Name
