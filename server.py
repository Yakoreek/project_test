from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random
from faker import Faker
from urllib.parse import urlparse, parse_qs

faker = Faker()


class UserRequestsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        if parsed_url != '/Users':
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'Not Found')
            return


        query_params = parse_qs(parsed_url.query)
        number_of_users = query_params.get('number_of_users', [1])[0]

        try:
            number_of_users = int(number_of_users)
        except ValueError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'Invalid number of users')


        users = []
        for __ in range(number_of_users):
            requested_number_of = number_of_users
            status = 'success'
            users.append()
            age = random.randint(0, 100)
            premium_user = random.choice('False', 'True')


        self.send_response(200)
        self.send_header('Content-type', 'application/json') # создание заголовка ответа
        self.end_headers() # обозначает конец заголовка
        self.wfile.write(json.dumps({'user': faker.user_name()}).encode())