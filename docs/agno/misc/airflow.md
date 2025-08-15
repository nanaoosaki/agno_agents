---
title: Airflow
category: misc
source_lines: 74431-74461
line_count: 30
---

# Airflow
Source: https://docs.agno.com/tools/toolkits/others/airflow



## Example

The following agent will use Airflow to save and read a DAG file.

```python cookbook/tools/airflow_tools.py
from agno.agent import Agent
from agno.tools.airflow import AirflowTools

agent = Agent(
    tools=[AirflowTools(dags_dir="dags", save_dag=True, read_dag=True)], show_tool_calls=True, markdown=True
)

dag_content = """
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
