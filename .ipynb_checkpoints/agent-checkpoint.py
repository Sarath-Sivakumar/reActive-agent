import ollama
import os

from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT

from tools import (
    get_weather,
    get_current_time,
    calculate
)

# -----------------------------------------
# LOAD ENV
# -----------------------------------------

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")


# -----------------------------------------
# AGENT CORE
# -----------------------------------------

def run_agent(user_message: str):

    # -------------------------------------
    # STEP 1 — THINK + ACTION
    # -------------------------------------

    prompt = f"""
{SYSTEM_PROMPT}

User Question:
{user_message}
"""

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    agent_output = response["message"]["content"]

    print("\n=== AGENT REASONING ===")
    print(agent_output)

    # -------------------------------------
    # STEP 2 — PARSE RESPONSE
    # -------------------------------------

    lines = agent_output.split("\n")

    action = ""
    action_input = ""

    for line in lines:

        if line.startswith("ACTION:"):
            action = line.replace("ACTION:", "").strip()

        if line.startswith("ACTION_INPUT:"):
            action_input = line.replace(
                "ACTION_INPUT:",
                ""
            ).strip()

    # -------------------------------------
    # STEP 3 — EXECUTE TOOL
    # -------------------------------------

    observation = ""

    if action == "weather":

        observation = get_weather(action_input)

    elif action == "calculator":

        observation = calculate(action_input)

    elif action == "time":

        observation = get_current_time()

    else:

        observation = "No valid tool selected"

    # -------------------------------------
    # STEP 4 — FINAL RESPONSE
    # -------------------------------------

    final_prompt = f"""
User Question:
{user_message}

Agent Thought + Action:
{agent_output}

Tool Observation:
{observation}

Generate a final helpful response for the user.
"""

    final_response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return {
        "thought_process": agent_output,
        "tool_used": action,
        "tool_input": action_input,
        "observation": observation,
        "final_answer": final_response["message"]["content"]
    }