from requests import post, get

print(post('http://127.0.0.1:8080/api/jobs',
           json={'team_leader': 1,
                 'job': 'Clean floor',
                 'work_size': 5,
                 'collaborators': '3, 4',
                 'is_finished': True}).json())

# не хватает ключа is_finished в json
print(post('http://127.0.0.1:8080/api/jobs',
           json={'team_leader': 1,
                 'job': 'Clean floor',
                 'work_size': 5,
                 'collaborators': '3, 4'}).json())

# json не передан
print(post('http://127.0.0.1:8080/api/jobs', json=0).json())

# не хватает ключа team_leader
print(post('http://127.0.0.1:8080/api/jobs',
           json={'job': 'Clean floor',
                 'work_size': 5,
                 'collaborators': '3, 4',
                 'is_finished': True}).json())

print(get('http://127.0.0.1:8080/api/jobs').json())
