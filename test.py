from ctransformers import AutoModelForCausalLM

# Path to the GGUF model file
model_path = "models\mistral-7b-instruct-v0.2.Q8_0.gguf"

# Load the model
llm = AutoModelForCausalLM.from_pretrained(
    model_path,
    model_type="mistral"  # Specify the model type
)

# Test the model with a prompt
prompt = "Write a Python function to calculate the sum of an array."
response = llm(
    prompt, 
    max_new_tokens=400,   # Limit the length of the output
    temperature=0.7       # Adjust the creativity of the response
)

print(response)
