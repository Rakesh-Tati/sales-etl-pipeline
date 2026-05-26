# Sales ETL Pipeline Project 🚀

This is an End-to-End Data Engineering ETL pipeline that extracts sales data, transforms it, and loads it into a PostgreSQL database.

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Data Manipulation:** Pandas
- **Database Connection:** SQLAlchemy & Psycopg2
- **Database:** PostgreSQL (pgAdmin)

## 📐 Architecture & Data Flow
1. **Extract:** Read raw sales transaction data from a local CSV file.
2. **Transform:** Clean missing rows, eliminate duplicate entries, and dynamically calculate a 10% bonus column for each sale.
3. **Load:** Safely establish a connection to PostgreSQL and load the clean dataset as a relational table (`sales_data`).

## 🚀 How to Setup and Run
1. Install dependencies:
   ```bash
   pip install pandas sqlalchemy psycopg2-binary
   ```
2. Setup database credentials inside `main.py`.
3. Run the complete pipeline:
   ```bash
   python main.py
   ```
