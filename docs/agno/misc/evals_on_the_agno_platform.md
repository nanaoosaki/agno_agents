---
title: Evals on the Agno platform
category: misc
source_lines: 6479-6541
line_count: 62
---

# Evals on the Agno platform
Source: https://docs.agno.com/evals/platform

You can track your evaluation runs on the Agno platform

<img height="200" src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/accuracy-eval-on-platform.png" style={{ borderRadius: "8px" }} />

## Track your evaluations

Apart from running your evaluations on the CLI, you can also track them on the Agno platform. This is useful to keep track of results and share them with your team.
Do it following these steps:

<Steps>
  <Step title="Authenticate">
    You can authenticate using your CLI or API key.

    **Using your CLI:**

    ```bash
    ag setup
    ```

    **Using your API key:**

    Get your API key from [Agno App](https://app.agno.com/settings) and use it to link your locally running agents to the Agno platform.

    ```bash
    export AGNO_API_KEY=your_api_key_here
    ```
  </Step>

  <Step title="Track your evaluations">
    When running an evaluation, set `monitoring=True` to track all its runs on the Agno platform:

    ```python
    from agno.agent import Agent
    from agno.eval.accuracy import AccuracyEval
    from agno.models.openai import OpenAIChat

    evaluation = AccuracyEval(
      model=OpenAIChat(id="gpt-4o"),
      agent=Agent(model=OpenAIChat(id="gpt-4o")),
      input="What is 10*5 then to the power of 2? do it step by step",
      expected_output="2500",
      monitoring=True, # This activates monitoring
    )

    # This run will be tracked on the Agno platform
    result = evaluation.run(print_results=True)
    ```

    You can also set the `AGNO_MONITOR` environment variable to `true` to track all evaluation runs.
  </Step>

  <Step title="View your evaluations">
    You can now view your evaluations on the Agno platform at [app.agno.com/evaluations](https://app.agno.com/evaluations).
  </Step>
</Steps>

<Info>Facing issues? Check out our [troubleshooting guide](/faq/cli-auth)</Info>


