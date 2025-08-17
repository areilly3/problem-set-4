'''
PART 1: ETL the dataset and save in `data/`

Here is the imbd_movie data:
https://github.com/cbuntain/umd.inst414/blob/main/data/imdb_movies_2000to2022.prolific.json?raw=true

It is in JSON format, so you'll need to handle accordingly and also figure out what's the best format for the two analysis parts. 
'''

import os
import pandas as pd
import json
import requests

def etl():
    """
    Extracts json data and saves it to 'data/'
    Args:
        none
    Returns:
        Saves a json file to 'data/'
    """
    
    # Create '/data' directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)

    # Load datasets and save to '/data'
    response = requests.get(url= 'https://github.com/cbuntain/umd.inst414/blob/main/data/imdb_movies_2000to2022.prolific.json?raw=true')

    # Save data as json file
    with open('data/data.json', 'w') as file:
        file.write(response.text)