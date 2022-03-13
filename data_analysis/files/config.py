import json

def read():
    json_file_path = '..\\config.json'
    with open(json_file_path, 'r') as json_file:
        config_file = json.load(json_file)
    print ('File {file} imported successfully.'.format(file=json_file_path))
    return config_file

