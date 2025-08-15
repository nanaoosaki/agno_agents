---
title: CSV
category: misc
source_lines: 73082-73151
line_count: 69
---

# CSV
Source: https://docs.agno.com/tools/toolkits/database/csv



**CsvTools** enable an Agent to read and write CSV files.

## Example

The following agent will download the IMDB csv file and allow the user to query it using a CLI app.

```python cookbook/tools/csv_tools.py
import httpx
from pathlib import Path
from agno.agent import Agent
from agno.tools.csv_toolkit import CsvTools

url = "https://agno-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv"
response = httpx.get(url)

imdb_csv = Path(__file__).parent.joinpath("wip").joinpath("imdb.csv")
imdb_csv.parent.mkdir(parents=True, exist_ok=True)
imdb_csv.write_bytes(response.content)

agent = Agent(
    tools=[CsvTools(csvs=[imdb_csv])],
    markdown=True,
    show_tool_calls=True,
    instructions=[
        "First always get the list of files",
        "Then check the columns in the file",
        "Then run the query to answer the question",
        "Always wrap column names with double quotes if they contain spaces or special characters",
        "Remember to escape the quotes in the JSON string (use \")",
        "Use single quotes for string values"
    ],
)

agent.cli_app(stream=False)
```

## Toolkit Params

| Parameter           | Type                     | Default | Description                                                            |
| ------------------- | ------------------------ | ------- | ---------------------------------------------------------------------- |
| `csvs`              | `List[Union[str, Path]]` | -       | A list of CSV files or paths to be processed or read.                  |
| `row_limit`         | `int`                    | -       | The maximum number of rows to process from each CSV file.              |
| `read_csvs`         | `bool`                   | `True`  | Enables the functionality to read data from specified CSV files.       |
| `list_csvs`         | `bool`                   | `True`  | Enables the functionality to list all available CSV files.             |
| `query_csvs`        | `bool`                   | `True`  | Enables the functionality to execute queries on data within CSV files. |
| `read_column_names` | `bool`                   | `True`  | Enables the functionality to read the column names from the CSV files. |
| `duckdb_connection` | `Any`                    | -       | Specifies a connection instance for DuckDB database operations.        |
| `duckdb_kwargs`     | `Dict[str, Any]`         | -       | A dictionary of keyword arguments for configuring DuckDB operations.   |

## Toolkit Functions

| Function         | Description                                      |
| ---------------- | ------------------------------------------------ |
| `list_csv_files` | Lists all available CSV files.                   |
| `read_csv_file`  | This function reads the contents of a csv file   |
| `get_columns`    | This function returns the columns of a csv file  |
| `query_csv_file` | This function queries the contents of a csv file |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/csv.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/csv_tools.py)


