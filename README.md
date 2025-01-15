# Python Code Assistant

This project is a Python Code Assistant that uses the locally hosted Mistral-7B model to generate Python code based on user prompts. It allows users to test the generated code with custom function names and test cases.

## Features

- Generates Python code based on user-defined prompts.
- Provides a user interface to test the generated code with custom function names and test cases.
- Supports a local Mistral-7B model for offline inference. [Download It](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/tree/main)

## Project Structure
```
project_root/
├── app.py              # Main Streamlit application
├── models/             # Folder to store the downloaded Mistral model
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd project_root
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the Mistral-7B model and place it in the `models/` folder.

## Setup

1. Ensure the model is correctly loaded from the `models/` directory in the script.
2. Install the necessary Streamlit and model dependencies.

## Usage

1. Run the script to analyze text files:
   ```bash
   streamlit run app.py
   ```
2. Enter a programming prompt in the text box and click Generate Code.
3. Review the generated code displayed in the text area.
4. Enter the function name and test case to test the code's functionality.

## Example Workflow

### Input Prompt:
Multiplication of Two Arrays    

### Generated Code:
```bash
  def multiply_arrays(array1, array2):
    return [x*y for x,y in zip(array1, array2)]
```

### Testing the Code:
- Function Name: `multiply_arrays`
- Test Case: `([1,3,4],[2,5,6])`

### Output
`Output`: `[2,15,24]`

## Requirements

- Python 3.8+
- Required libraries:
  - streamlit
  - ctransformers
  - langchain
  - re
 
## Notes

1. Ensure the Mistral model is downloaded and placed in the `models/` folder. [Download It](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/tree/main). Choose `mistral-7b-instruct-v0.2.Q8_0.gguf`
2. Test cases should be formatted as tuples, even for single arguments (e.g., `(5,)`).

## License

This project is licensed under the MIT License.
