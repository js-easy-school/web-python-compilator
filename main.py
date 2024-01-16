import arrr
import sys
from pyscript import document

# Redefining the print function to write to stdout
def print(*args, **kwargs):
    sys.stdout.write(' '.join(map(str, args)) + '\n')

# Function to handle input and evaluate the expression
def handle_input(input_text):
    try:
        result = eval(input_text)
        print(result)
    except Exception as e:
        print('Error:', e)

# Function to handle the translation of English to Pirate speak
def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)  # The 'arrr' object is not defined
