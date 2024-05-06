import secrets
username, password = f"Liuwenjun{secrets.token_hex(6)}", secrets.token_hex(12)
print(username, password)