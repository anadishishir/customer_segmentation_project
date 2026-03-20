Retail Customer Segmentation Analysis
This project focuses on grouping customers of an online retail store based on their buying behavior. By identifying these segments, a business can better target its marketing and improve customer loyalty.

Project Goal
The main objective was to take raw transaction data and transform it into actionable insights using the RFM (Recency, Frequency, Monetary) model. This helps distinguish "loyal champions" from "at-risk customers."

Dataset Overview
The analysis uses a dataset of over 500,000 transactions from a UK-based online retailer.

Key features used: Invoice Date, Quantity, Unit Price, and Customer ID.

Cleaning steps: Removed missing Customer IDs, filtered out cancelled orders (negative quantities), and eliminated duplicate entries to ensure data quality.

Technical Workflow
1. Feature Engineering (RFM)
I engineered three specific metrics for every customer:

Recency: How many days since the last purchase.

Frequency: Total number of orders made.

Monetary: Total amount of money spent.

2. Data Preparation
Log Transformation: Applied to handle skewed data distributions.

Scaling: Used StandardScaler to bring all features to the same scale, which is essential for clustering algorithms.

3. Machine Learning
Algorithm: Used K-Means Clustering to group similar customers.

Optimization: Applied the "Elbow Method" and Silhouette Scoring (achieving a score of 0.60) to determine that 3-4 clusters provided the most meaningful separation.

Key Findings
Through the clusters, I identified distinct customer personas:

High-Value Customers: Frequent shoppers who spend the most.

New/Occasional Shoppers: Customers with recent but few purchases.

At-Risk Customers: Those who haven't purchased in a long time.

Tools Used
Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Model Storage: Joblib (for saving the segmentation pipeline)