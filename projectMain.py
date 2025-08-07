import requests
import os
import json
import argparse
import pandas as pd

def create_folder(file_name):
    current_directory = os.getcwd()
    output_directory = os.path.join(current_directory, file_name)
    try:
        os.makedirs(output_directory, exist_ok=True)
    except PermissionError:
        print(f"Permission Denied: Unable to create '{output_directory}'")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return output_directory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Support script to gather data from experiments/datasets within the specified project")
    parser.add_argument("-p", "--projectID", type=str, required=True, help="The ID of the project you are gathering events from")
    parser.add_argument("-a", "--apiKey", type=str, required=True, help="The API Key you  want to use for the script")

    args = parser.parse_args()


    PROJECT_ID = args.projectID
    API_KEY = args.apiKey

    # Define the base API url for easy reuse
    API_URL = "https://api.braintrust.dev/v1"

    # Create the base API urls for retrieving experiments and datasets
    GET_EXPERIMENT_URL = API_URL + "/experiment?project_id=" + PROJECT_ID
    GET_DATASET_URL = API_URL + "/dataset?project_id=" + PROJECT_ID

    headers = {
        "Authorization": "Bearer " + API_KEY
    }

    experiment_response = requests.request("GET", GET_EXPERIMENT_URL, headers=headers)
    dataset_response = requests.request("GET", GET_DATASET_URL, headers=headers)

    for experiment in experiment_response.json()["objects"]:
        folder_name = experiment["name"]
        file_name = folder_name + ".csv"

        output_directory = create_folder(folder_name)

        # Get the event data for each experiment
        GET_EVENTS_URL = API_URL + "/experiment/" + experiment["id"] + "/fetch"
        experiment_event_response = requests.request("GET", GET_EVENTS_URL, headers=headers)

        # Convert the event data to a Dataframe
        df = pd.DataFrame(experiment_event_response.json()["events"])
        
        # Output the Dataframe to a csv
        df.to_csv(output_directory + '/' + file_name, index=False)

    for dataset in dataset_response.json()["objects"]:
        folder_name = dataset["name"]
        file_name = folder_name + ".csv"

        output_directory = create_folder(folder_name)

        # Get the event data for each dataset
        GET_EVENTS_URL = API_URL + "/dataset/" + dataset["id"] + "/fetch"
        dataset_event_response = requests.request("GET", GET_EVENTS_URL, headers=headers)

        # Convert the event data to a Dataframe
        df = pd.DataFrame(dataset_event_response.json()["events"])
        
        # Output the Dataframe to a csv
        df.to_csv(output_directory + '/' + file_name, index=False)



        








