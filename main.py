from pyscript import document
import sys

def print(*args, **kwargs):
    sys.stdout.write(' '.join(map(str, args)) + '\n')

def handle_input(input_text):
    try:
        result = eval(input_text)
        print(result)
    except Exception as e:
        print('Error:', e)

def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)
