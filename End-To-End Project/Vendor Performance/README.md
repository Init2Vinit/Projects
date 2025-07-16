# Vendor Performance Analysis: End-to-End Project

This project delivers a comprehensive data solution for optimising vendor relationships by providing actionable insights into their performance.

## 🎯 Project Goal

To build an end-to-end analytics pipeline that identifies high-performing and underperforming vendors, enabling data-driven procurement and supply chain decisions.

## ✨ Key Features & Deliverables

* **Database Integration:** Scripted data ingestion from a database source.
* **Robust Data Analysis:** Comprehensive Exploratory Data Analysis (EDA) and performance metric calculation.
* **Custom Reporting:** Python script for generating vendor sales summaries.
* **Actionable Insights:** Identified key performance trends and areas for strategic improvement.

## 🛠️ Technologies Used

* **Python:** Pandas, NumPy, Matplotlib, Seaborn, `sqlite3`
* **Jupyter Notebooks:** For detailed analysis and documentation.
* **SQL:** Demonstrated through database ingestion.

## 📂 Project Files

* `Exploratory Data Analysis.ipynb`: Initial data understanding and visualisation.
* `Vendor Performance Analysis.ipynb`: Core analysis, KPI calculation, and insights generation.
* `ingestion_db.py`: Python script for database data ingestion.
* `get_vendor_summary.py`: Python script to process and summarise vendor sales data.
* `vendor_sales_summary.csv`: The primary dataset used for analysis.
* `Untitled-1.ipynb`: (Please rename this to reflect its content, e.g., `Data Preprocessing.ipynb`)

## 🚀 How to Run

1.  Clone this repository.
2.  Ensure you have Python installed.
3.  Install dependencies (if you create a `requirements.txt`): `pip install -r requirements.txt`
4.  Run `ingestion_db.py` to simulate data loading (or connect to your actual database if applicable).
5.  Execute notebooks sequentially: `Exploratory Data Analysis.ipynb`, then `Vendor Performance Analysis.ipynb`.
6.  Run `get_vendor_summary.py` to generate specific reports.
