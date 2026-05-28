# Sales ETL Pipeline

## 📌 Project Overview

This project is an end-to-end ETL pipeline built using Python, pandas, SQL, and SQLite.

The pipeline extracts sales data from CSV/API sources, performs data cleaning and transformation, and loads the processed data into a SQL database for analytics.

---

# 🚀 Technologies Used

* Python
* pandas
* SQL
* SQLite
* requests
* Logging
* CSV / JSON

---

# 🏗️ Project Architecture

```text
CSV/API
↓
Extract
↓
Transform
↓
Processed CSV/JSON
↓
SQLite Database
↓
SQL Analytics
```

---

# 📂 Folder Structure

```text
sales-etl-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── api_extract.py
│
├── sql/
│   ├── schema.sql
│   └── analytics.sql
│
├── logs/
│   └── pipeline.log
│
├── README.md
├── requirements.txt
├── main.py
└── sales.db
```

---

# 🔥 Features

* ETL Pipeline
* CSV Data Extraction
* API Data Extraction
* Data Cleaning
* Null Handling
* Duplicate Removal
* SQL Analytics
* Logging
* Error Handling
* Processed CSV & JSON Generation

---

# 🔄 ETL Flow

## 1. Extract

Data extracted from:

* CSV files
* APIs

---

## 2. Transform

Transformations performed:

* Null value handling
* Duplicate removal
* Bonus calculation
* Date formatting

---

## 3. Load

Processed data loaded into SQLite database for analytics.

---

# 📊 Sample SQL Analytics

## Total Sales by Category

```sql
SELECT category,
       SUM(amount) AS total_sales
FROM sales
GROUP BY category;
```

---

## Top Customers

```sql
SELECT customer_name,
       SUM(amount) AS total_amount
FROM sales
GROUP BY customer_name
ORDER BY total_amount DESC;
```

---

# ▶️ How to Run the Project

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Pipeline

```bash
python main.py
```

---

# 📸 Screenshots

## Pipeline Output

![Pipeline Output](screenshots/pipeline_output.png)

## SQL Query Output

![SQL Query](screenshots/sql_query.png)

## Folder Structure

![Folder Structure](screenshots/folder_structure.png)

## Transformed data into CSV

![Folder Structure](screenshots/transformed_data.png)

---

# 📌 Future Improvements

* Incremental Loading
* CDC (Change Data Capture)
* Docker Deployment
* Airflow Scheduling

---

# 👨‍💻 Author

Rakesh Tati
Aspiring Data Engineer
