---
title: Define the workflow
category: misc
source_lines: 81688-81706
line_count: 18
---

# Define the workflow
class GenerateNewsReport(Workflow):
    agent_1: Agent = ...

    agent_2: Agent = ...

    agent_3: Agent = ...

    def run(self, ...) -> RunResponse:
        # Run agents and gather the response
        final_agent_input = ...

        # Generate the final response from the writer agent
        agent_3_response: RunResponse = self.agent_3.run(final_agent_input)

        # Return the response
        return agent_3_response

