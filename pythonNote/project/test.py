users_database = {0: {'balance': 1, 'full_name': 'Anonymous Anonymously'},
                  1: {'balance': 32, 'full_name': '𝓜𝓪𝔁𝓲𝓶'},
                  2: {'balance': 15, 'full_name': '𝓜𝓪𝔁𝓲𝓶'}}

res = dict(sorted(users_database.items(), key=lambda x: x[1].get("balance")))

print(res)

