# **Data Pipeline Project (ETL Demo)**

This project demonstrates the essential skills required for an ETL (Extract, Transform, Load) process using Python and SQLite. It simulates a real-world data pipeline for transforming raw data into a more structured, processed format ready for analysis.

## **Project Overview**
This ETL pipeline project performs the following tasks:

- **Extract**: Reads data from a simulated data source (e.g., employee records).
- **Transform**: Applies transformations, such as increasing salaries, removing duplicates, and cleaning data.
- **Load**: Loads the transformed data into a local SQLite database.

This project showcases my ability to:
- Manage data from extraction to storage.
- Clean and transform data using Python and SQLite.
- Remove duplicates and ensure data integrity.
- Perform SQL operations and manipulate data with Pandas.
- Use version control and virtual environments for code isolation and reproducibility.

## **Table of Contents**
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [ETL Process Breakdown](#etl-process-breakdown)
  - [1. Extract Phase](#1-extract-phase)
  - [2. Transform Phase](#2-transform-phase)
  - [3. Load Phase](#3-load-phase)
- [How to Run the Project](#how-to-run-the-project)
- [Future Enhancements](#future-enhancements)

## **Technologies Used**
- **Python 3.9+**
- **SQLite3**: For database creation and storage.
- **Pandas**: For data manipulation and transformation.
- **SQLAlchemy**: For advanced database interaction.
- **Git**: For version control and collaboration.


## **Setup Instructions**
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd DataPipelinePro


## Prerequisites

- Python 3.x
- SQLite3
- A virtual environment (optional but recommended)
- Required Python libraries listed in `requirements.txt`

## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone <repository-url>
    cd DataPipelinePro
    ```

2. Set up a virtual environment (optional).

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the necessary Python libraries.

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

### 1. Setting up the Database

Before running the ETL pipeline, you need to create the SQLite database and set up the table. Run the `setup_database.py` script to initialize the database.

```bash
python setup_database.py
