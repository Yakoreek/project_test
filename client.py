from pprint import pprint
import requests
import csv

def client_pars(url, number_of_users, output_file):
    response = requests.get(url, params={'number_of_users': number_of_users})
    json_data = response.json()

    users = json_data['users']
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'address', 'age', 'premium_user'])
        writer.writeheader()
        writer.writerows(users)

    print('Данные загружены: ')
    pprint(json_data)

if __name__ == '__main__':
    client_pars('http://127.0.0.1:80/Users', 5, 'users.csv')
