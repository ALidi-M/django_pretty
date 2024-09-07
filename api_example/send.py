import requests

headers = {}
headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NzI4MDE2LCJpYXQiOjE3MTk3Mjc3MTYsImp0aSI6IjQ3YmM1MDlhYWU0ZDQxYmM4MmZkY2UzNGYxNDdmYjEyIiwidXNlcl9pZCI6MX0.kyvGTIeuq20DvBwk1pZtQEfxFS_qe46p6cBKR8P3ODA'
r = requests.get('http://127.0.0.1:8000/paradigm',headers=headers)

print(r.text)