import requests
import json

token = 'Add your slack token here'


def list_files():
    params = {
        'token': token,
        'count': 1000
    }
    uri = 'https://slack.com/api/files.list'
    response = requests.get(uri, params=params)
    return json.loads(response.text)['files']


def display_files(file_name_url_list):

    for file_name_url in file_name_url_list:
            print(file_name_url)


print("Started reading files... ")
files = list_files()
file_names = [f['url_private_download'] for f in files]

display_files(file_names)
print("Total files are:{0}".format(file_names.__len__()))




