import openai

openai.api_key = open("keys\\openai").read()


def get_response(prompt):
    return openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=2000).choices[0].text

def format(prompt):
    prompt = prompt.split("\n")
    formatted_response = []
    for line in prompt:
        if line.startswith(("1.", "2.", "3.", "4.", "5.")):
            formatted_response.append(line.replace("â€™", "'"))

    return formatted_response
