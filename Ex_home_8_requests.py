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
