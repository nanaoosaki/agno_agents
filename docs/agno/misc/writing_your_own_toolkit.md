---
title: Writing your own Toolkit
category: misc
source_lines: 71227-71283
line_count: 56
---

# Writing your own Toolkit
Source: https://docs.agno.com/tools/custom-toolkits



Many advanced use-cases will require writing custom Toolkits. Here's the general flow:

1. Create a class inheriting the `agno.tools.Toolkit` class.
2. Add your functions to the class.
3. **Important:** Include all the functions in the `tools` argument to the `Toolkit` constructor.

Now your Toolkit is ready to use with an Agent. For example:

```python shell_toolkit.py
from typing import List

from agno.agent import Agent
from agno.tools import Toolkit
from agno.utils.log import logger

class ShellTools(Toolkit):
    def __init__(self, **kwargs):
        super().__init__(name="shell_tools", tools=[self.run_shell_command], **kwargs)

    def run_shell_command(self, args: List[str], tail: int = 100) -> str:
        """
        Runs a shell command and returns the output or error.

        Args:
            args (List[str]): The command to run as a list of strings.
            tail (int): The number of lines to return from the output.
        Returns:
            str: The output of the command.
        """
        import subprocess

        logger.info(f"Running shell command: {args}")
        try:
            logger.info(f"Running shell command: {args}")
            result = subprocess.run(args, capture_output=True, text=True)
            logger.debug(f"Result: {result}")
            logger.debug(f"Return code: {result.returncode}")
            if result.returncode != 0:
                return f"Error: {result.stderr}"
            # return only the last n lines of the output
            return "\n".join(result.stdout.split("\n")[-tail:])
        except Exception as e:
            logger.warning(f"Failed to run shell command: {e}")
            return f"Error: {e}"

agent = Agent(tools=[ShellTools()], show_tool_calls=True, markdown=True)
agent.print_response("List all the files in my home directory.")

```


