import requests
import os
import json
import pandas as pd

# Define the specific project ID that we want to search
PROJECT_ID = "INSERT_PROJECT_ID"

# Define the base API url for easy reuse
API_URL = "https://api.braintrust.dev/v1"

# Insert your API key
API_KEY = "INSERT_API_KEY"

# Create the base API urls for retrieving experiments and datasets
GET_EXPERIMENT_URL = API_URL + "/experiment?project_id=" + PROJECT_ID
GET_DATASET_URL = API_URL + "/dataset?project_id=" + PROJECT_ID

headers = {
    "Authorization": "Bearer " + API_KEY
}

# Attempt to create the directory to store CSV output in
current_directory = os.getcwd()
output_directory = os.path.join(current_directory, 'Braintrust Support Script Output')
try:
    os.mkdir(output_directory)
except FileExistsError:
    print(f"Directory '{output_directory}' already exists")
except PermissionError:
    print(f"Permission Denied: Unable to create '{output_directory}'")
except Exception as e:
    print(f"An error occurred: {e}")


experiment_response = requests.request("GET", GET_EXPERIMENT_URL, headers=headers)
dataset_response = requests.request("GET", GET_DATASET_URL, headers=headers)

for experiment in experiment_response.json()["objects"]:
    file_name = experiment["name"] + ".csv"

    # Get the event data for each experiment
    GET_EVENTS_URL = API_URL + "/experiment/" + experiment["id"] + "/fetch"
    experiment_event_response = requests.request("GET", GET_EVENTS_URL, headers=headers)

    # Convert the event data to a Dataframe
    df = pd.DataFrame(experiment_event_response.json()["events"])
    
    # Output the Dataframe to a csv
    df.to_csv(output_directory + '/' + file_name, index=False)

for dataset in dataset_response.json()["objects"]:
    file_name = dataset["name"] + ".csv"

    # Get the event data for each dataset
    GET_EVENTS_URL = API_URL + "/dataset/" + dataset["id"] + "/fetch"
    dataset_event_response = requests.request("GET", GET_EVENTS_URL, headers=headers)

    # Convert the event data to a Dataframe
    df = pd.DataFrame(dataset_event_response.json()["events"])
    
    # Output the Dataframe to a csv
    df.to_csv(output_directory + '/' + file_name, index=False)

    









