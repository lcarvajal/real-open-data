from constants import DATA_SETS_BASE_URL, DATA_SETS_META_FILE_PATH, DATA_SETS_DIRECTORY_PATH
import pandas as pd
import requests

# ETL

def etl_data_sets_meta():
    data_sets_meta_response = extract_data_sets_meta_data(DATA_SETS_BASE_URL + f'?q=publisher%3A%22Stadt%20Wien%22&sort=relevance%20asc%2C%20metadata_modified%20desc&rows={1000}&include_drafts=false')
    data_sets_meta_df = convert_data_sets_meta_response_to_df(data_sets_meta_response)
    data_sets_meta_df = filter_data_sets_meta_for_csv_files(data_sets_meta_df)
    load_data_sets_meta(data_sets_meta_df, DATA_SETS_META_FILE_PATH)

def etl_data_sets(data_sets_meta):
    for i, meta in data_sets_meta.head(10).iterrows():
        url = meta['Resource URL'].replace(' ', '')
        df = extract_data_set(url)

        if len(df) != 0:
            name = meta['Dataset Name']
            id = meta['Resource ID'].replace(' ', '')
            
            print(f'{name} is usable and will get saved!')
            load_data_set(df, f'{DATA_SETS_DIRECTORY_PATH}{id}-{name}.csv')

# Extract

def extract_data_sets_meta_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code)
        return None
    
def extract_data_set(url):
    try:
        return pd.read_csv()
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Transform

def convert_data_sets_meta_response_to_df(response_json):
    data_sets_response = response_json["result"]["results"]

    data_list = []
    for dataset in data_sets_response:
        for res in dataset["resources"]:
            resource_data = {
                "Dataset Name": dataset.get('name', ''),
                "Begin Datetime": dataset.get('begin_datetime', ''),
                "End Datetime": dataset.get('end_datetime', ''),
                "Notes": dataset.get('notes', ''),
                "Attribute Description": dataset.get('attribute_description', ''),
                "Resource ID": res.get('id', ''),
                "Resource URL": res.get('url', ''),
                "Resource Format": res.get('format', '')
            }
            data_list.append(resource_data)

    return pd.DataFrame(data_list)

def filter_data_sets_meta_for_csv_files(df):
    df = df[df['Resource URL'].str.contains('outputFormat=csv')]
    return df

# Load

def load_data_sets_meta(df, file_path):
    df.to_csv(file_path, index=False)

def load_data_set(df, file_path):
    df.to_csv(file_path, index=False)