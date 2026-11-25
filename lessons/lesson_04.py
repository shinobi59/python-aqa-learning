def check_response(status_code):
    return status_code in [200, 201]

print(check_response(200))
print(check_response(201))
print(check_response(400))
print(check_response(404))
print(check_response(500))
print(check_response(501))