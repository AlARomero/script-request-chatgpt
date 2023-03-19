import openai
from dotenv import load_dotenv
import os
import argparse

load_dotenv()

token = os.environ.get('GPT_TOKEN')
do_completion = False

parser = argparse.ArgumentParser()
parser.add_argument("pregunta")
args = parser.parse_args()

index = 0
while not do_completion and index < len(args.pregunta):
    if args.pregunta[index] == " ":
        do_completion = True
    index+=1 

if do_completion:
    openai.api_key = token
    completion = openai.Completion.create(engine = "text-davinci-003", prompt = args.pregunta, max_tokens = 3000)
    response = completion.choices[0].text[1:]
    print(response + "\n")
else:
    print("\nLongitud minima de la pregunta de 2 palabras\n")