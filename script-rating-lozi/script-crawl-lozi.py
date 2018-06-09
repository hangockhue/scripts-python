import requests

print("Input your key word")
you_key = input()

url_key = "%20".join(you_key.split(" "))
api_file = requests.get(
    "https://latte.lozi.vn/v1.2/search/blocks?skip=0&q={}&limit=20&t=nearest&cityId=50".format(url_key))
data = api_file.json()['data']
data_list = []
for i in data:
    try:
        data_list.append(
            {'name': i['dish']['eatery']['name'], 'rating': i['rating']})
    except Exception as e:
        data_list.append({'name': i['dish']['eatery']['name'], 'rating': 0})
sort_data = sorted(data_list, key=lambda x: x['rating'])[::-1]
for i in sort_data[0:5]:
    print(i)
