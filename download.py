from pathlib import Path

import requests

base_url = "https://www.anantagame.com/pc/gw/20241112104639/static_da7146d6/keep_origin/spine"
dir_path = '.'

role = [
    'tafei',
    'banxi',
    'yalan',
    'meika',
    'ailin',
    'laikaya',
    'dila',
    'linqin',
]
index = [
    'dila',
    'meila',
    'nanzhu',
    'nanzhu_2',
    'nvzhu',
    'nvzhu_2',
    'nvzhu_3',
    'tafei',
]


def download(file_path, url):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as file:
        response = requests.get(url, stream=True).iter_content(chunk_size=8192)
        for chunk in response:
            file.write(chunk)


for key in role:
    partial = f'role/{key}/{key}'
    for ext in ['.skel', '.atlas', '.png']:
        download(f'{dir_path}/{partial}{ext}', f'{base_url}/{partial}{ext}')

for key in index:
    partial = f'index/{key}'
    download(f'{dir_path}/{partial}.png', f'{base_url}/{partial}.png')
    if '_' in key:
        continue
    for ext in ['.skel', '.atlas']:
        download(f'{dir_path}/{partial}{ext}', f'{base_url}/{partial}{ext}')
