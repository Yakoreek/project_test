from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json
import random
from faker import Faker
from urllib.parse import urlparse, parse_qs

faker = Faker()


class UserRequestsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path != '/Users':
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
            return

        users = []
        for __ in range(number_of_users):
            users.append({
                'name': faker.name(),
                'address': faker.address(),
                'age': random.randint(0, 100),
                'premium_user': random.choice(['False', 'True'])
            }
            )


        response = {
            'requested_number_of': number_of_users,
            'status': 'success',
            'users': users,
        }


        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers() # обозначает конец заголовка
        self.wfile.write(json.dumps(response).encode('utf-8'))






if __name__ == '__main__':
    os.chdir('.')
    server_object = HTTPServer(('', 80), RequestHandlerClass = UserRequestsHandler)
    print('Server running on port 80')
    server_object.serve_forever()

