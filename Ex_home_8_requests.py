import requests

print('Задача №1\n')


def main():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    heroes = requests.get(url=url + '/all.json', headers={'Content-Type': 'application/json; charset=utf-8'})
    super_heroes = ['Hulk', 'Captain America', 'Thanos']
    intelligence = {}
    for hero in heroes.json():
        if hero['name'] in super_heroes:
            intelligence[hero['name']] = hero['powerstats']['intelligence']
    intelligence_hero = dict([max(intelligence.items(), key=lambda k_v: k_v[1])])
    most_intelligence = [(key, value) for key, value in intelligence_hero.items()]

    print(f"Самый умный супергерой - {most_intelligence[0][0]}, с интеллектом, {most_intelligence[0][1]}")


main()

print('\nЗадача №2\n')


def upload_file_to_disk(disk_file_path, file_name):
    with open('token.txt', 'r') as token_file:
        token = token_file.readline()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    params = {"path": disk_file_path, "overwrite": "true"}
    response = requests.get(upload_url, headers=headers, params=params)
    response_data = response.json()
    url_to_upload = response_data['href']
    response = requests.put(url_to_upload, data=open(file_name, 'rb'))
    response.raise_for_status()
    if response.status_code == 201:
        print("Файл Test.txt добавлен на ЯндексДиск")


upload_file_to_disk('Test.txt', 'Test.txt')
