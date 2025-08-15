---
title: Create agents with more specific validation criteria
category: misc
source_lines: 56556-56605
line_count: 49
---

# Create agents with more specific validation criteria
data_validator = Agent(
    name="Data Validator",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "You are a data validator. Analyze the provided data and determine if it's valid.",
        "For data to be VALID, it must meet these criteria:",
        "- user_count: Must be a positive number (> 0)",
        "- revenue: Must be a positive number (> 0)",
        "- date: Must be in a reasonable date format (YYYY-MM-DD)",
        "",
        "Return exactly 'VALID' if all criteria are met.",
        "Return exactly 'INVALID' if any criteria fail.",
        "Also briefly explain your reasoning.",
    ],
)

data_processor = Agent(
    name="Data Processor",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="Process and transform the validated data.",
)

report_generator = Agent(
    name="Report Generator",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="Generate a final report from processed data.",
)


def early_exit_validator(step_input: StepInput) -> StepOutput:
    """
    Custom function that checks data quality and stops workflow early if invalid
    """
    # Get the validation result from previous step
    validation_result = step_input.previous_step_content or ""

    if "INVALID" in validation_result.upper():
        return StepOutput(
            content="❌ Data validation failed. Workflow stopped early to prevent processing invalid data.",
            stop=True,  # Stop the entire workflow here
        )
    else:
        return StepOutput(
            content="✅ Data validation passed. Continuing with processing...",
            stop=False,  # Continue normally
        )


