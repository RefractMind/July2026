import os

import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

tools = [
    {
        "name": "calculate_risk_category",
        "description": "Calculates the financial risk category based on the numeric ratio.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ratio": {
                    "type": "number",
                    "description": "The debt-to-equity ratio to evaluate."
                }
            },
            "required": ["ratio"]
        }
    }
]


def calculate_risk_category(ratio):
    """
    Calculates the financial risk category based on the numeric ratio.

    Parameters:
    ratio (float): The debt-to-equity ratio to evaluate.

    Returns:
    str: The risk category (Low, Medium, High) and a brief explanation.
    """
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=100,
        messages=[{
            "role": "user",
            "content": f"Given the financial ratio of {ratio}, determine the risk category (Low, Medium, High) and provide a brief explanation.",
        }],
    )
    return response.content[0].text


def run_agent(
    tools,
    user_input,
    model="claude-sonnet-5",
    max_tokens=200,
    temperature=0.7,
):
    """
    Runs the agent with the provided tools and user input.

    Parameters:
    tools (list): A list of tool dictionaries (Anthropic tool-use schema).
    user_input (str): The input from the user.
    model (str): The model to use for generating responses.
    max_tokens (int): The maximum number of tokens to generate.
    temperature (float): The sampling temperature for response generation.

    Returns:
    Message: The response message from the agent, which may include a tool_use block.
    """
    return client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        tools=tools,
        messages=[{"role": "user", "content": user_input}],
    )


if __name__ == "__main__":
    print(calculate_risk_category(0.72))