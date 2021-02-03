from typing import List

current_users = ['admin', 'mark', 'judy', 'mac', 'windows']
current_users_upper = []
current_users_title = []
for i in current_users:
    current_users_upper.append(i.upper())
    current_users_title.append(i.title())
print(current_users_upper)
print(current_users_title)

new_users = ['Admin', 'Mark', 'microsoft', 'apple', 'google']

for user in new_users:
    if user in current_users or user in current_users_title or user in current_users_upper:
        print(f"Your username {user} is being used, please change a username!")
    else:
        print(f"Your username {user} is OK!")
