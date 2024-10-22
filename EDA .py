# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Set plotting configurations
plt.style.use('ggplot')
sns.set_palette('pastel')
plt.rcParams['figure.figsize'] = (10, 6)

# Load the dataset and inspect its structure (using your specific path)
data_path = 'C:/Users/ANIKET MISHRA/Desktop/python/Autoencoder/archive/creditcard.csv'
data = pd.read_csv(data_path)
print("First 5 records:")
print(data.head())
print("\nDataset Info:")
print(data.info())

# Check for missing values and display basic statistics
print("\nMissing values check:")
print(data.isnull().sum())
print("\nBasic statistics:")
print(data.describe())

# Categorize features into numerical and categorical
num_features = data.select_dtypes(include=['float64', 'int64']).columns
cat_features = data.select_dtypes(include=['object', 'category']).columns
print("\nNumerical Features:", num_features)
print("Categorical Features:", cat_features)

# Perform Exploratory Data Analysis (EDA)
# Pie chart for class distribution (Fraud vs Non-fraud)
fraud_dist = data['Class'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(fraud_dist, labels=['Non-Fraud', 'Fraud'], autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'red'])
plt.title('Fraud vs Non-Fraud Transactions')
plt.show()

# Heatmap for correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr(), annot=False, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Distribution plots for important numerical features
for col in ['V1', 'V2', 'V3', 'Amount']:
    plt.figure()
    sns.histplot(data[col], bins=50, kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# Scale numerical features and merge with categorical ones (No categorical features in this case, so just scaling)
scaler = StandardScaler()
scaled_num = pd.DataFrame(scaler.fit_transform(data[num_features]), columns=num_features)

# Prepare data for anomaly detection (Training & Testing Split)
X = scaled_num.drop(columns=['Class'])
y = data['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
print("\nTraining set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# Isolate genuine and fraud samples for training/testing
genuine_samples = data[data['Class'] == 0]
fraud_samples = data[data['Class'] == 1]

print("\nNumber of Genuine Samples (Class 0):", len(genuine_samples))
print("Number of Fraud Samples (Class 1):", len(fraud_samples))

# Print out all columns to verify the actual feature names
print("\nColumns in the dataset:")
print(data.columns)

# List of additional categorical features to plot
categorical_features = ['repeat_retailer', 'used_chip', 'used_pin_number', 'online_order']

# Loop through each categorical feature and plot if it exists
for feature in categorical_features:
    if feature in data.columns:
        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x=feature, hue='Class')
        plt.title(f'Distribution of {feature}')
        plt.show()
    else:
        print(f"Feature '{feature}' does not exist in the dataset.")
