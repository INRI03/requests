import requests

name1 = 'Hulk'
name2 = 'Captain America'
name3 = 'Thanos'
_list = [name1, name2, name3]
url = "https://superheroapi.com/api/2619421814940190/search/"


def best_intelligence(persons):
  main = {}
  for name in _list:
    intels = []
    resp = requests.get(url+name)
    results = resp.json()['results']
    for i in results:
      if i['name'] == name:
        intels.append(i['powerstats']['intelligence'])
    main[name] = intels
  print(max(main))


best_intelligence(_list)