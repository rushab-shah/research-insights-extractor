'''
Author: Rushab Shah
Code: extract.py
Purpose: To make API calls to gpt for all the chunks of given text and extract key features
'''
import json
import time
import requests
from tqdm import tqdm

##########
API_KEY = "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"
##########

URL="https://api.openai.com/v1/chat/completions"
HEADERS = {'Authorization': 'Bearer '+API_KEY,'Accept':'application/json','Content-Type':'application/json'}
OUTPUT_PATH = "../output/"
UI_CONSUMPTION_PATH = "../UI/public/"
PROMPT_PATH = "../prompts/"
TEXT_MODEL = "gpt-3.5-turbo"
JSON_URL = "https://api.jsonbin.io/v3/b/"
JSON_KEY = "$2b$10$SLBgMhKNPW02.cj5pTQS5.qothtYp7kTnspUoSQDcesZ59.Z1zosG"
BIN_ID = "64827d968e4aa6225eab6224"

def access_cached_data():
    """
    TODO
    """
    headers = {
        "X-Master-Key":JSON_KEY
    }
    response = requests.get(JSON_URL+BIN_ID, headers=headers, timeout=240)
    if response.status_code==200:
        resp = response.json()
        return resp["record"]
    else:
        return None

def get_cached_papers(cached_data):
    """
    TODO
    """
    cached_papers = {data["name"]: index for index, data in enumerate(cached_data)}
    return cached_papers


def extract_features(filepath):
    """
    TODO
    """
    parsed_data = load_parsed_data(filepath)
    result = []
    cached_data = access_cached_data()
    if cached_data is not None:
        cached_papers = get_cached_papers(cached_data)
    else:
        cached_papers = None
    print("Processing papers...")
    for paper in tqdm(parsed_data, desc="Processing papers", ncols=70):
        # print("Processing paper "+str(paper))
        if cached_papers is not None and paper in cached_papers:
            cached_features = cached_data[cached_papers[str(paper)]]["features"]
            if cached_features is not None and len(cached_features)>0:
                result.append(paper_features)
                continue
        paper_features = {
            "name":str(paper),
            "features":[]
        }
        paper_features["features"] = make_api_calls(paper,parsed_data)
        result.append(paper_features)
    print("All features extracted.")
    write_result(result)

def make_api_calls(paper_name,parsed_data):
    """
    Method to process and make API calls
    """
    # print("Started making API calls for "+str(paper_name))
    prompt = get_prompt()
    paper_chunk_data = parsed_data[paper_name]
    features = []
    no_of_chunks = len(paper_chunk_data)
    for i in range(0,no_of_chunks):
        messages = []
        message_obj = {"role": "user", "content":prompt+preprocess_prompt(paper_chunk_data[i])}
        messages.append(message_obj)
        request_body = {
            "model": TEXT_MODEL,
            "messages": messages
        }
        try:
            response = requests.post(URL, headers=HEADERS, json=request_body, timeout=240)
        except requests.exceptions.RequestException as ex:
            error_message = str(ex)  # Extract the error message from the exception
            print("Request failed with error:", error_message)
        if response.status_code==200:
            response_obj = response.json()
            # Modify code to extract JSON from response_obj["choices"][0]["message"]["content"]
            # You might have to parse the string to find where the JSON starts
            content = extract_json_from_content(response_obj["choices"][0]["message"]["content"])
            try:
                features.append(json.loads(content))
            except Exception as ex:
                create_error_log(ex,content)
        else:
            print(response.json())
            print(response.status_code)
    # print("All features extracted for "+str(paper_name))
    return features

def extract_json_from_content(content):
    """
    TODO
    """
    opening_bracket_index = content.find('[')
    if opening_bracket_index != -1:
        return content[opening_bracket_index:]
    else:
        return content

def create_error_log(error,content):
    """
    Method to store errors while parsing response
    """
    # Generate timestamp for the error file name
    timestamp = str(int(time.time()))

    # Create the error message with the timestamp
    error_message = f"Error: {str(error)}"
    # print(str(error_message))
    # Write the error message to the error file
    error_file = f"error_{timestamp}.txt"
    with open(OUTPUT_PATH+error_file, "w") as f:
        f.write(str(content))


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

def post_processing_result(result):
    """
    Method for post processing the feature array for each paper.
    """
    merged_papers = []
    for paper in result:
        merged_features = []
        feature_dict = {}
        for feature_group in paper["features"]:
            for feature in feature_group:
                if "name" in feature and "value" in feature:
                    if feature["name"] not in feature_dict:
                        if feature["value"] not in [None, "N/A", "Not mentioned", "Not provided in the text","Not provided","not provided","Not explicitly mentioned."]:
                            feature_dict[feature["name"]] = str(feature["value"])
                        else:
                            feature_dict[feature["name"]] = ""
                    else:
                        if feature["value"] not in [None, "N/A", "Not mentioned", "Not provided in the text","Not provided","not provided","Not explicitly mentioned."]:
                            if feature_dict[feature["name"]]:  # Avoid trying to concatenate 'NoneType' and 'str'
                                feature_dict[feature["name"]] += "; " + str(feature["value"])
                            else:
                                feature_dict[feature["name"]] = str(feature["value"])

        for name, value in feature_dict.items():
            merged_features.append({"name": name, "value": value})

        merged_papers.append({"name": paper["name"], "features": merged_features})

    return merged_papers


def write_result(result):
    """
    Storing result
    """
    post_processed_data = post_processing_result(result)
    with open(OUTPUT_PATH+'output.json','w') as file_object:
        file_object.write(json.dumps(post_processed_data))
    send_to_json_store(post_processed_data)
    print("Terminating.")

def send_to_json_store(data):
    """
    TODO
    """
    headers = {
        "Content-Type":"application/json",
        "X-Master-Key":JSON_KEY
    }
    response = requests.put(JSON_URL+BIN_ID, headers=headers, json=data,timeout=60)
    if response.status_code==200:
        print("Data stored online!")
    else:
        print(response.status_code)
