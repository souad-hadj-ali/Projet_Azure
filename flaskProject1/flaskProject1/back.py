import json
from azure.cosmos import CosmosClient
from azure.cosmos.partition_key import PartitionKey
#from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
#from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
#from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
#from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
import os
import sys
import requests
from io import BytesIO

from array import array
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import time


def create_db_client():
    cosmosdb_uri = 'https://projectdabase.documents.azure.com:443/'
    cosmosdb_primary_key = 'CrqivVmXtfHT3gVCC394h9vJX2U9jjDlMkXGHuHda9hLgku6MJnLTRK3CVV7NmBxTJpxTxtX2rIq8l6pnmqLAg=='
    client = CosmosClient(cosmosdb_uri, cosmosdb_primary_key)
    print("Connextion success to", type(client))
    db = client.create_database_if_not_exists('imagesDataBase')
    print('Database created or used', type(db))
    container = db.create_container_if_not_exists(id='WebsiteData', partition_key=PartitionKey(path='/CartID'))
    print('Container WebsiteData created', type(container))
    return container

def create_IA():
    cog_key = '9b9f11767d6b4326bb398fec2eb34fc2'
    cog_endpoint = 'https://westus2.api.cognitive.microsoft.com/'
    computervision_client = ComputerVisionClient(cog_endpoint, CognitiveServicesCredentials(cog_key))

def create_blob_client():
    blob_service_client = BlobServiceClient.from_connection_string(
        "DefaultEndpointsProtocol=https;AccountName=storageprojectesgi22;AccountKey=7nKbWyikD69q5ZNMy80kuRDxoylnlz0coVat0zDDG+kt4inbLhKsXkZxdz5mJPtMkTjYsHv9kAeb+AStzJcHJg==;EndpointSuffix=core.windows.net")
    return blob_service_client

def get_items(tags):
    container = create_db_client()
    items = list(container.query_items(
        query="SELECT c.path FROM c WHERE c.tags like @tags",
        parameters=[
            {"name": "@tags", "value": tags}
        ],
        enable_cross_partition_query=True
    ))
    i = 0
    chemin = list()
    while i < len(items):
        print(items[i].get('path'))
        chemin.append(items[i].get('path'))
        i += 1
    return chemin

def get_images(path):
    i=0
    list_image = list()
    while i < len(path):
        list_image.append("https://storageprojectesgi22.blob.core.windows.net/contenair-images/C:/Users/John/Desktop/DataSet/"+str(path[i])+".jpg")
        i += 1
    return list_image



