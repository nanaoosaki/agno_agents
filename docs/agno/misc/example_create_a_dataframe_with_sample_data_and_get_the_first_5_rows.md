---
title: Example: Create a dataframe with sample data and get the first 5 rows
category: misc
source_lines: 73365-73398
line_count: 33
---

# Example: Create a dataframe with sample data and get the first 5 rows
agent.print_response("""
Please perform these tasks:
1. Create a pandas dataframe named 'sales_data' using DataFrame() with this sample data:
   {'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B'],
    'quantity': [10, 15, 8, 12, 20],
    'price': [9.99, 15.99, 9.99, 12.99, 15.99]}
2. Show me the first 5 rows of the sales_data dataframe
""")
```

## Toolkit Params

| Parameter                 | Type                      | Default | Description                                                    |
| ------------------------- | ------------------------- | ------- | -------------------------------------------------------------- |
| `dataframes`              | `Dict[str, pd.DataFrame]` | `{}`    | A dictionary to store Pandas DataFrames, keyed by their names. |
| `create_pandas_dataframe` | `function`                | -       | Registers a function to create a Pandas DataFrame.             |
| `run_dataframe_operation` | `function`                | -       | Registers a function to run operations on a Pandas DataFrame.  |

## Toolkit Functions

| Function                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_pandas_dataframe` | Creates a Pandas DataFrame named `dataframe_name` by using the specified function `create_using_function` with parameters `function_parameters`. Parameters include 'dataframe\_name' for the name of the DataFrame, 'create\_using\_function' for the function to create it (e.g., 'read\_csv'), and 'function\_parameters' for the arguments required by the function. Returns the name of the created DataFrame if successful, otherwise returns an error message. |
| `run_dataframe_operation` | Runs a specified operation `operation` on a DataFrame `dataframe_name` with the parameters `operation_parameters`. Parameters include 'dataframe\_name' for the DataFrame to operate on, 'operation' for the operation to perform (e.g., 'head', 'tail'), and 'operation\_parameters' for the arguments required by the operation. Returns the result of the operation if successful, otherwise returns an error message.                                             |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/pandas.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/pandas_tools.py)


