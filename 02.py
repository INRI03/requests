import requests
import os

YANDEX_TOKEN = 'AQAAAAAN_EidAADLW6McFuOt_EKzt1eZDuFoFQM'


class YaDisk:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
    }

    def get_link(self, path: str):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        return response.json().get('href')

    def upload_file(self, path, file_name):
        upload_link = self.get_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'))
        if response.status_code == 201:
            print('ОК')


if __name__ == '__main__':
    disk = YaDisk(YANDEX_TOKEN)
    old_path = r'E:\картинки\обои напитки'
    path = old_path.replace('\\', '/')
    files = os.listdir(path)
    address = map(lambda file: os.path.join(path, file), files)
    for val in address:
        disk.upload_file(val.split('\\')[-1], val)