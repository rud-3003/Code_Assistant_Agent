#Approach
# -> Instead of using Mistral-7B model locally, I have used the GGUF version of the model available on Hugging Face. (https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)
#    GGUF version being smaller in size was easier to implement on my laptop. 
# -> Used Streamlit to input prompt to and display the output generated from the model.

#Assumptions
# -> User prompts are clear and are not vague, thus creating easier prompt to the model as of now.
# -> Code generated by the model is not malicious and thus safe to extract.
# -> Users have basic understanding of Python to test the code.

#Improvements
# -> Bug while extracting code, for example generating functions involving recursion like fibonacci and factorial
# -> Parse the User prompt so that better quality code can be generated.
# -> Due to smaller size of the model and respectively its max_new_token generation capacity(512 tokens), complex and lengthy codes are not fully generated.
#    Solve the above issue.

#Demonstration
# -> I have uploaded a youtube video to showcase the above project
# Link: https://youtu.be/rsHNO8OyeRY 
# GitHub Repo: https://github.com/rud-3003/Code_Assistant_Agent


import streamlit as st
import traceback
from ctransformers import AutoModelForCausalLM
import re

def generate_code(user_prompt):
    model_path = "models/mistral-7b-instruct-v0.2.Q8_0.gguf"
    llm = AutoModelForCausalLM.from_pretrained(
        model_path,
        model_type="mistral"
    )
    
    template = """
        You are a Python Programming Assistant. Generate Python code for the following task:
        {user_prompt}
        Your output should include only Python code, without any additional comments or explanations or use cases.
        """
    
    # Format the prompt using the template
    formatted_prompt = template.format(user_prompt=user_prompt.strip())
    
    try:
        response = llm(
            formatted_prompt,
            max_new_tokens=500,
            temperature=0.01  
        )
        # Extract only the Python code using a regex
        code_match = re.search(r"```python(.*?)```", response, re.DOTALL) #regex to extract tge python code and discard all rest text generated
        if code_match:
            return code_match.group(1).strip() 
        else:
            return response.strip()
    except Exception as e:
        print("Error generating code:", e)
        return None

def test_generated_code(code_snippet, function_name, test_case):
    #For this function to work we have to explicitly declare function name to be stored in the safe environment created to test the code
    try:
        local_vars = {}
        exec(code_snippet, {}, local_vars)
        
        if function_name not in local_vars:
            return f"Test failed: Function '{function_name}' is not defined in the code." 

        result = local_vars[function_name](*test_case)
        return f"Output: {result}"
    except Exception as e:
        return f"Test failed: {traceback.format_exc()}"

if "generated_code" not in st.session_state:
    st.session_state.generated_code = None


# Streamlit app
st.title("Python Code Assistant")

user_input = st.text_input("Enter a Python programming request:", "") # User Input

if st.button("Generate Code"): # Generate Code Button   
    if user_input:
        code = generate_code(user_input)
        if code:
            st.session_state.generated_code = code  # Save generated code to session state
        else:
            st.error("Failed to generate code.")

if st.session_state.generated_code: # Display the generated code if available
    st.subheader("Generated Code:")
    st.text_area("Python Code", st.session_state.generated_code, height=200)

    st.subheader("Test Your Code:") # Take inputs for testing the code
    func_name = st.text_input("Enter the function name to test:")
    test_case_input = st.text_input("Enter the test case as a tuple (e.g., 2, 3):")
    
    if st.button("Run Test"):
        if func_name and test_case_input:
            try:
                test_case = eval(f"({test_case_input})") # Converting test cases input into a tuple becuase of the varying size of parameters for a function.
                test_result = test_generated_code(st.session_state.generated_code, func_name, test_case)
                st.write(test_result)
            except Exception as e:
                st.error(f"Invalid test case format: {e}")
        else:
            st.error("Please provide both the function name and test case.")
