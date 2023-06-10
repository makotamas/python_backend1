import unicodedata

# Task 1
users = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

modified_users = []
for user in users:
  name = user
  email = f"{user[0].lower()}.{user[1].lower()}@company.hu"
  normal_email = unicodedata.normalize('NFKD', email).encode('ASCII', 'ignore')
  password = f"{user[0]}123Start"
  modified_users.append({
      'name': name,
      'email': normal_email.decode("utf-8"),
      'password': password
  })

print(modified_users)

sorted_users = sorted(modified_users, key=lambda x: ' '.join(x['name']))
with open('nevek.txt', 'w', encoding='utf-8') as file:
  for user in sorted_users:
    file.write(
        f"{user['name'][0]} {user['name'][1]} {user['email']} {user['password']}\n"
    )


