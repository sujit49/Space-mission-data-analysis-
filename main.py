# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'space_missions.csv'  # Update for your Colab file path
data = pd.read_csv(file_path, encoding='latin1')

# Fix column names (remove unnecessary spaces and duplicates)
data.columns = [col.strip().split('\n')[0] for col in data.columns]

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Extract year and month for time-based analysis
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month

# Convert 'Price' to numeric after cleaning (if applicable)
if 'Price' in data.columns:
    data['Price'] = data['Price'].str.replace('[^\d.]', '', regex=True).astype(float)

# Data Overview
print("Dataset Summary:")
print(data.info())
print("\nMissing Values:")
print(data.isnull().sum())

# 1. Number of Missions Over Time
plt.figure(figsize=(14, 7))
sns.countplot(x='Year', data=data, order=sorted(data['Year'].dropna().unique()))
plt.xticks(rotation=90)
plt.title("Number of Space Missions Over Time", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Missions", fontsize=12)
plt.tight_layout()
plt.show()

# 2. Mission Status Distribution
plt.figure(figsize=(8, 6))
status_counts = data['MissionStatus'].value_counts()
status_counts.plot(kind='bar', color='skyblue')
plt.title("Mission Status Distribution", fontsize=16)
plt.xlabel("Mission Status", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.tight_layout()
plt.show()

# 3. Success Rate Over Time
if 'MissionStatus' in data.columns:
    success = data[data['MissionStatus'] == 'Success'].groupby('Year').size()
    total = data.groupby('Year').size()
    success_rate = (success / total) * 100

    plt.figure(figsize=(14, 7))
    plt.plot(success_rate.index, success_rate.values, marker='o', color='green', label='Success Rate')
    plt.title("Mission Success Rate Over Time", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Success Rate (%)", fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# 4. Top 10 Companies by Number of Missions
if 'Company' in data.columns:
    top_companies = data['Company'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    top_companies.plot(kind='bar', color='orange')
    plt.title("Top 10 Companies by Number of Missions", fontsize=16)
    plt.xlabel("Company", fontsize=12)
    plt.ylabel("Number of Missions", fontsize=12)
    plt.tight_layout()
    plt.show()

# 5. Average Mission Cost Over Time (if Price column exists)
if 'Price' in data.columns:
    avg_price_by_year = data.groupby('Year')['Price'].mean()

    plt.figure(figsize=(14, 7))
    plt.plot(avg_price_by_year.index, avg_price_by_year.values, marker='o', color='purple')
    plt.title("Average Mission Cost Over Time", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Average Cost (in million $)", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 6. Rocket Status Distribution
if 'RocketStatus' in data.columns:
    plt.figure(figsize=(8, 6))
    rocket_status_counts = data['RocketStatus'].value_counts()
    rocket_status_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    plt.title("Rocket Status Distribution", fontsize=16)
    plt.ylabel("")  # Remove y-axis label for clarity
    plt.tight_layout()
    plt.show()

# 7. Launch Locations (Top 10)
if 'Location' in data.columns:
    top_locations = data['Location'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    top_locations.plot(kind='bar', color='teal')
    plt.title("Top 10 Launch Locations", fontsize=16)
    plt.xlabel("Location", fontsize=12)
    plt.ylabel("Number of Launches", fontsize=12)
    plt.tight_layout()
    plt.show()

# Insights Summary
print("\n--- Insights Summary ---")
print(f"Total Missions: {len(data)}")
if 'MissionStatus' in data.columns:
    success_count = len(data[data['MissionStatus'] == 'Success'])
    print(f"Success Rate: {success_count / len(data) * 100:.2f}%")
if 'Price' in data.columns:
    print(f"Average Mission Cost: {data['Price'].mean():,.2f} million $")

# Save the processed dataset
processed_file_path = '/content/processed_space_missions.csv'
data.to_csv(processed_file_path, index=False)
print(f"Processed file saved at: {processed_file_path}")
