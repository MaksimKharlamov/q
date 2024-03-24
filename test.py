from requests import post, get, delete

print(delete('http://127.0.0.1:8080/api/jobs/1').json())

# такой работы нет
print(delete('http://127.0.0.1:8080/api/jobs/52').json())

# повторно удалить не получится
print(delete('http://127.0.0.1:8080/api/jobs/1').json())

# передана строка
print(delete('http://127.0.0.1:8080/api/jobs/qqq').json())

print(get('http://127.0.0.1:8080/api/jobs').json())
