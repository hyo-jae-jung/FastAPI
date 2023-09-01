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
params = {'key1': 'value1', 'key2': 'value2'}
r = httpx.get('https://httpbin.org/get', params=params)
print(r.url)
