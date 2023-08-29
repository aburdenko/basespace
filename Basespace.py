import json
import requests
import os
from google.cloud import pubsub

BASESPACE_BEARER_TOKEN=os.environ.get("BASESPACE_BEARER_TOKEN")
headers = {
    "Authorization": f"Bearer {BASESPACE_BEARER_TOKEN}",
}

params = {
    "limit": 100,
}


def create_project(name: str):
    basespace_url = "https://api.basespace.illumina.com/v2"
    params["name"] = name

    basespace_url += "/projects"
    response = requests.post(basespace_url, data=params, headers=headers)

    if response.status_code == 200:
        projects = response.json()

        for project in projects:
            print(project["name"])

    else:
        print(response.text)


def get_datasets( project_id, topic_name):
    basespace_url = "https://api.basespace.illumina.com/v2"
    response = requests.get(f"{basespace_url}/datasets", headers=headers)
    #print(response)

    if response.status_code == 200:
        datasets = response.json()

        if len(datasets['Items']) > 0:
            for ds in datasets['items']:
                print(ds["name"])
                
                # post response to GCP Pub/Sub Queue
                
                with pubsub.PublisherClient() as publisher:
                # Convert the dictionary to a JSON string.
        
                    json_string = json.dumps(ds)

                    # Convert the JSON string to a bytestring.
                    bytestring = bytes(json_string, "utf-8")
                    
                    fq_topic_name = f"projects/{project_id}/topics/{topic_name}"
                    future = publisher.publish(fq_topic_name, bytestring)
                message = future.result()

        else:
            print("No items!")

    else:
        print(response.text)
