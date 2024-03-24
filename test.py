from requests import put, get

print(put('http://127.0.0.1:8080/api/jobs/1',
          json={'team_leader': 1,
                'job': 'Clean floor',
                'work_size': 5,
                'collaborators': '3, 4',
                'is_finished': True}).json())

# не хватает ключа is_finished в json
print(put('http://127.0.0.1:8080/api/jobs/2',
          json={'team_leader': 1,
                'job': 'Clean floor',
                'work_size': 5,
                'collaborators': '3, 4'}).json())

# json не передан
print(put('http://127.0.0.1:8080/api/jobs/2', json=0).json())

# не хватает ключа team_leader
print(put('http://127.0.0.1:8080/api/jobs/2',
          json={'job': 'Clean floor',
                'work_size': 5,
                'collaborators': '3, 4',
                'is_finished': True}).json())

# некорректный id
print(put('http://127.0.0.1:8080/api/jobs/52',
          json={'team_leader': 1,
                'job': 'Clean floor',
                'work_size': 5,
                'collaborators': '3, 4',
                'is_finished': True}).json())

# некорректный id
print(put('http://127.0.0.1:8080/api/jobs/qqq',
          json={'team_leader': 1,
                'job': 'Clean floor',
                'work_size': 5,
                'collaborators': '3, 4',
                'is_finished': True}).json())

print(get('http://127.0.0.1:8080/api/jobs').json())
