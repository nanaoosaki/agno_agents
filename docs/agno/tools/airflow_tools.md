---
title: Airflow Tools
category: tools
source_lines: 27876-27908
line_count: 32
---

# Airflow Tools
Source: https://docs.agno.com/examples/concepts/tools/others/airflow



## Code

```python cookbook/tools/airflow_tools.py
from agno.agent import Agent
from agno.tools.airflow import AirflowTools

agent = Agent(
    tools=[AirflowTools(dags_dir="tmp/dags", save_dag=True, read_dag=True)],
    show_tool_calls=True,
    markdown=True,
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

