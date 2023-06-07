'''
Author: Rushab Shah
Code: extract.py
Purpose: To make API calls to gpt for all the chunks of given text and extract key features
'''
import requests
import json

##########
API_KEY = "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"
##########

URL="https://api.openai.com/v1/chat/completions"
HEADERS = {'Authorization': 'Bearer '+API_KEY,'Accept':'application/json','Content-Type':'application/json'}
OUTPUT_PATH = "../output/"
PROMPT_PATH = "../prompts/"
TEXT_MODEL = "gpt-3.5-turbo"

def extract_features(filepath):
    """
    TODO
    """
    print("Starting to extract features")
    parsed_data = load_parsed_data(filepath)
    result = []
    for paper in parsed_data:
        paper_features = {
            "name":str(paper),
            "features":[]
        }
        ## PROCESS
        paper_features["features"] = make_api_calls(paper,parsed_data)
        result.append(paper_features)
    print("Features extracted. Saving output as JSON")
    write_result(result)

def make_api_calls(paper_name,parsed_data):
    """
    Method to process and make API calls
    """
    print("Started making API calls for "+str(paper_name))
    prompt = get_prompt()
    paper_chunk_data = parsed_data[paper_name]
    features = []
    messages = []
    # count = 0
    no_of_chunks = len(paper_chunk_data)
    for i in range(0,no_of_chunks):
        # count+=1
        # if count==1:
        message_obj = {"role": "user", "content":prompt+preprocess_prompt(paper_chunk_data[i])}
        # else:
        #     message_obj = {"role": "user", "content":preprocess_prompt(paper_chunk_data[i])}
        messages.append(message_obj)
        request_body = {
            "model": TEXT_MODEL,
            "messages": messages
        }
        try:
            response = requests.post(URL, headers=HEADERS, json=request_body, timeout=180)
        except requests.exceptions.RequestException as ex:
            error_message = str(ex)  # Extract the error message from the exception
            print("Request failed with error:", error_message)
        if response.status_code==200:
            # print(response.json())
            response_obj = response.json()
            features.append(response_obj["choices"][0]["message"]["content"])
        else:
            print(response.json())
            print(response.status_code)
    print("All features extracted for "+str(paper_name))
    return features

def load_parsed_data(filepath):
    """
    Method to read the json file containing a map of research paper title to its text chunk data
    """
    parsed_data={}
    with open(filepath,'r') as file_obj:
        data = file_obj.read()
    parsed_data = json.loads(data)
    return parsed_data

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
    with open(OUTPUT_PATH+'output.json','w') as file_object:
        file_object.write(json.dumps(result))
    print("Done!")
