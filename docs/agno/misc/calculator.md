---
title: Calculator
category: misc
source_lines: 73669-73736
line_count: 67
---

# Calculator
Source: https://docs.agno.com/tools/toolkits/local/calculator



**Calculator** enables an Agent to perform mathematical calculations.

## Example

The following agent will calculate the result of `10*5` and then raise it to the power of `2`:

```python cookbook/tools/calculator_tools.py
from agno.agent import Agent
from agno.tools.calculator import CalculatorTools

agent = Agent(
    tools=[
        CalculatorTools(
            add=True,
            subtract=True,
            multiply=True,
            divide=True,
            exponentiate=True,
            factorial=True,
            is_prime=True,
            square_root=True,
        )
    ],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("What is 10*5 then to the power of 2, do it step by step")
```

## Toolkit Params

| Parameter      | Type   | Default | Description                                                         |
| -------------- | ------ | ------- | ------------------------------------------------------------------- |
| `add`          | `bool` | `True`  | Enables the functionality to perform addition.                      |
| `subtract`     | `bool` | `True`  | Enables the functionality to perform subtraction.                   |
| `multiply`     | `bool` | `True`  | Enables the functionality to perform multiplication.                |
| `divide`       | `bool` | `True`  | Enables the functionality to perform division.                      |
| `exponentiate` | `bool` | `False` | Enables the functionality to perform exponentiation.                |
| `factorial`    | `bool` | `False` | Enables the functionality to calculate the factorial of a number.   |
| `is_prime`     | `bool` | `False` | Enables the functionality to check if a number is prime.            |
| `square_root`  | `bool` | `False` | Enables the functionality to calculate the square root of a number. |

## Toolkit Functions

| Function       | Description                                                                              |
| -------------- | ---------------------------------------------------------------------------------------- |
| `add`          | Adds two numbers and returns the result.                                                 |
| `subtract`     | Subtracts the second number from the first and returns the result.                       |
| `multiply`     | Multiplies two numbers and returns the result.                                           |
| `divide`       | Divides the first number by the second and returns the result. Handles division by zero. |
| `exponentiate` | Raises the first number to the power of the second number and returns the result.        |
| `factorial`    | Calculates the factorial of a number and returns the result. Handles negative numbers.   |
| `is_prime`     | Checks if a number is prime and returns the result.                                      |
| `square_root`  | Calculates the square root of a number and returns the result. Handles negative numbers. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/calculator.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/calculator_tools.py)


