import httpx 

# r = httpx.get('https://httpbin.org/get')
# print(r)
# print(r.status_code)
# print(r.headers)
# r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
# print(r)
# r = httpx.delete('https://httpbin.org/delete')
# print(r)
# r = httpx.head('https://httpbin.org/get')
# print(r)
# r = httpx.options('https://httpbin.org/get')
# print(r)
# params = {'key1': 'value1', 'key2': 'value2'}
# headers = {
#     "accept": "application/json",
#     "Content-Type": "application/json"
# }
# data = {
#     "email":"inn@python.com",
#     "password":"exemplary",
#     "events":[]
# } 
# r = httpx.post('http://127.0.0.1:8000/user/signup',headers=headers,json=data)
# print(r.json())
# headers = {
#     "accept": "application/json",
#     "Content-Type": "application/x-www-form-urlencoded"
# }
# data = {
#     "username":"inn@python.com",
#     "password":"exemplary"
# }
# r2 = httpx.post('http://127.0.0.1:8000/user/signin',headers=headers,data=data)
# print(r2.json())

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiaW5uQHB5dGhvbi5jb20iLCJleHBpcmVzIjoxNjkzOTg3MzAyLjQ0NDY1ODN9.uSXxYP-qWkhxNWARVn0NoL8n5y08gkHnEN-QV285CVs"
}
data = {
        "title": "FastAPI Book Launch HTTPX",
        "image": "https://linktomyimage.com/image.png",
        "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
        "tags": [
            "python",
            "fastapi",
            "book",
            "launch"
        ],
        "location": "Google Meet",
    }
r3 = httpx.post('http://127.0.0.1:8000/event/new',headers=headers,json=data)
print(r3.json())
