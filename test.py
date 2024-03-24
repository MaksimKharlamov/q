from requests import put

print(put('http://127.0.0.1:8080/api/jobs/1',
          json={'team_leader': 1,
                'job': 'Clean floor',
                'work_size': 5,
                'collaborators': '3, 4',
                'is_finished': True}).text)
