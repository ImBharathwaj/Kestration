# Kestration
Orchestrating the data pipeline

# Dagster + DBT + DuckDB Integration

## Overview
This project integrates **Dagster**, **DBT**, and **DuckDB** to enable a robust data pipeline orchestration framework. It ensures seamless data transformations using DBT, efficient data storage with DuckDB, and scalable workflow management with Dagster.

## Prerequisites
Ensure you have the following installed:

- Python
- [Dagster](https://dagster.io/)
- [DBT](https://docs.getdbt.com/)
- [DuckDB](https://duckdb.org/)

## Installation

Clone the repository and install dependencies:

```sh
# Clone the repository
git clone https://github.com/ImBharathwaj/Kestration.git

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Project Structure

```
.
├── orchestrator_dbt  # Dagster project directory
│   ├── assets        # DBT models and assets
│   ├── resources     # Custom resources
│   ├── schedules     # Dagster schedules
│   ├── definitions.py # Dagster definitions
│   └── constants.py  # Environment variables
├── dbt_project       # DBT project
│   ├── models        # DBT models
│   ├── profiles.yml  # DBT profile configuration
│   └── dbt_project.yml # DBT project settings
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

## Configuration

### DBT Setup
Ensure that the `profiles.yml` file is configured correctly for DuckDB:

```yaml
default:
  outputs:
    dev:
      type: duckdb
      path: "data/dev.duckdb"
  target: dev
```

### Dagster Definitions
Update `definitions.py` to include DBT and DuckDB resources:

```python
import os
from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets import dbt_assets
from .resources import DuckDBResource

# Environment variables
dbt_project_dir = os.getenv("DBT_PROJECT_DIR", "./dbt_project")

defs = Definitions(
    assets=[dbt_assets],
    resources={
        "dbt": DbtCliResource(project_dir=dbt_project_dir),
        "duckdb": DuckDBResource(db_path="data/dev.duckdb")
    }
)
```

## Running the Pipeline

### Run DBT Transformations
```sh
dbt run --profiles-dir ./dbt_project
```

### Run Dagster
Start the Dagster UI and run your pipeline:
```sh
dagster dev
```

## Conclusion
This setup provides a powerful way to orchestrate data workflows with **Dagster**, transform data with **DBT**, and efficiently store data using **DuckDB**. You can extend this by adding more assets, schedules, and resources as needed.

