import streamlit as st
import traceback
from langchain.prompts import PromptTemplate
from ctransformers import AutoModelForCausalLM
from langchain.prompts import PromptTemplate
import re

# # Function to parse user input
# def parse_user_input(user_input):
#     """
#     Parse and interpret user input as a Python programming request.
#     """
#     return user_input  # For now, return the input as is

# Function to generate Python code based on a prompt
def generate_code(user_prompt):
    model_path = "models/mistral-7b-instruct-v0.2.Q8_0.gguf"
    llm = AutoModelForCausalLM.from_pretrained(
        model_path,
        model_type="mistral"
    )
    
    # Define the template
    template = """
You are a Python Programming Assistant. Generate Python code for the following task:
{user_prompt}
Your output should include only Python code, without any additional comments or explanations or use cases.
"""
    
    # Format the prompt using the template
    formatted_prompt = template.format(user_prompt=user_prompt.strip())
    
    try:
        # Generate the response
        response = llm(
            formatted_prompt,
            max_new_tokens=500,
            temperature=0.01  # Low temperature for deterministic output
        )
        # Extract only the Python code using a regex
        code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
        if code_match:
            return code_match.group(1).strip()  # Return only the code inside the Python block
        else:
            # If no code block is found, return the raw response
            return response.strip()
    except Exception as e:
        print("Error generating code:", e)
        return None

# Function to test the generated code snippet
def test_generated_code(code_snippet, test_case):
    """
    Test the generated code snippet by running it with a test case.
    """
    try:
        # Simulate running the code (this is a minimal placeholder)
        local_vars = {}
        exec(code_snippet, {}, local_vars)  # Execute the code in a safe environment
        result = local_vars['fib'](*test_case)
        return f"Output: {result}"
    except Exception as e:
        return f"Test failed: {traceback.format_exc()}"

# Streamlit app
st.title("Python Code Assistant")

# Input section
user_input = st.text_input("Enter a Python programming request:", "")

if st.button("Generate Code"):
    if user_input:

        # Generate code
        code = generate_code(user_input)
        if code:
            st.subheader("Generated Code:")
            st.text_area("Python Code", code, height=200)

            # Optionally test the code
            test_result = test_generated_code(code, (6,))  # Example test case
            st.subheader("Test Result:")
            st.write(test_result)
        else:
            st.error("Failed to generate code.")
    else:
        st.error("Please enter a valid prompt.")
