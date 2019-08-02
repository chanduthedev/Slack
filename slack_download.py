import requests
import time
import json
import sys

token = 'Add your slack token here'

no_of_days = 1
file_extension = ".jpg"

if len(sys.argv) < 2:
    print("Usage: python3 {0} {1} {2}".format(sys.argv[0], 'file_extension', 'no_of_days'))
    print("Please refer README file for more info")
    exit(1)


file_extension = '.'+sys.argv[1]

no_of_days = int(sys.argv[2])


ts_to = int(time.time()) - no_of_days * 24 * 60 * 60


def list_files():
    params = {
        'token': token,
        'ts_to': ts_to,
        'count': 1000
    }
    uri = 'https://slack.com/api/files.list'
    response = requests.get(uri, params=params)
    return json.loads(response.text)['files']


def download_files(file_name_url_list):

    for file_name_url in file_name_url_list:
        if file_name_url.endswith(file_extension):
            file_name = file_name_url.split('/')[-1]
            print(file_name, ' file downloading is in progress ...')
            r = requests.get(file_name_url, headers={'Authorization': 'Bearer %s' % token})

            with open(file_name, 'wb') as f:
                f.write(r.content)

            print(file_name, ' file downloading finished with status code ', r.status_code)


print("Started reading files... ")
files = list_files()
file_ids = [f['id'] for f in files]
file_names = [f['url_private_download'] for f in files]
print("Total files are:{0}".format(file_ids.__len__()))

download_files(file_names)




