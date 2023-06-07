'''
Author: Rushab Shah
Code: extract.py
Purpose: To make API calls to gpt for all the chunks of given text and extract key features
'''
import requests

##########
API_KEY = ""
##########

URL="https://api.openai.com/v1/chat/completions"
HEADERS = {'Authorization': 'Bearer '+API_KEY,'Accept':'application/json','Content-Type':'application/json'}
OUTPUT_PATH = "./output/"
PROMPT_PATH = "../prompts/"
TEXT_MODEL = "gpt-3.5-turbo"

def extract_features(chunks):
    """
    TODO
    """
    print("Making API calls to gpt")
    prompt = get_prompt()
    result = []
    messages = []
    count = 0
    ind = 0
    length = len(chunks)
    print(length)
    for ind in range(0,1):
        count+=1
        if count==1:
            message_obj = {"role": "user", "content":prompt+preprocess_prompt(chunks[len(chunks)-2])}
        else:
            message_obj = {"role": "user", "content":preprocess_prompt(chunks[len(chunks)-2])}
        messages.append(message_obj)
    request_body = {
        "model": TEXT_MODEL,
        "messages": messages
    }
    try:
        response = requests.post(URL, headers=HEADERS, json=request_body, timeout=300)
    except requests.exceptions.RequestException as ex:
        error_message = str(ex)  # Extract the error message from the exception
        print("Request failed with error:", error_message)
    if response.status_code==200:
        print(response.json())
        response_obj = response.json()
        result.append(response_obj["choices"][0]["message"]["content"])
    else:
        print(response.json())
        print(response.status_code)
    write_result(result)
    return


def get_prompt():
    """
    Method to get the prompt needed to talk to GPT
    """
    prompt = ""
    with open(PROMPT_PATH+"extract-features.txt","r") as file_object:
        prompt = file_object.read()
    return prompt

def preprocess_prompt(prompt_str):
    """
    TODO
    """
    preprocessed_str = prompt_str.strip()
    return preprocessed_str

def write_result(result):
    """
    Storing result
    """
    print("Storing result")
    with open(OUTPUT_PATH+'op.txt','w') as file_object:
        for res in result:
            file_object.write(res+"\n\n")
    print("Done!")
