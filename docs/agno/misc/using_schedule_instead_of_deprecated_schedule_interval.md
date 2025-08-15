---
title: Using 'schedule' instead of deprecated 'schedule_interval'
category: misc
source_lines: 74461-74506
line_count: 45
---

# Using 'schedule' instead of deprecated 'schedule_interval'
with DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule='@daily',  # Changed from schedule_interval
    catchup=False
) as dag:
    def print_hello():
        print("Hello from Airflow!")
        return "Hello task completed"
    task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello,
        dag=dag,
    )
"""

agent.run(f"Save this DAG file as 'example_dag.py': {dag_content}")

agent.print_response("Read the contents of 'example_dag.py'")
```

## Toolkit Params

| Parameter  | Type            | Default          | Description                                      |
| ---------- | --------------- | ---------------- | ------------------------------------------------ |
| `dags_dir` | `Path` or `str` | `Path.cwd()`     | Directory for DAG files                          |
| `save_dag` | `bool`          | `True`           | Whether to register the save\_dag\_file function |
| `read_dag` | `bool`          | `True`           | Whether to register the read\_dag\_file function |
| `name`     | `str`           | `"AirflowTools"` | The name of the tool                             |

## Toolkit Functions

| Function        | Description                                        |
| --------------- | -------------------------------------------------- |
| `save_dag_file` | Saves python code for an Airflow DAG to a file     |
| `read_dag_file` | Reads an Airflow DAG file and returns the contents |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/airflow.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/airflow_tools.py)


