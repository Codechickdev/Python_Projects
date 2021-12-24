import requests

url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=5'
r = requests.get(url)
res = r.json()

facts = []

for result in res:
    for key, value in result.items():
        if key == 'text':
            facts.append(value)

for i in facts:
    print('')
    print(i)
    print('')

    with open('facts.txt', 'a') as file:
        file.write(i +'\n')