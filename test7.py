from weakref import proxy
import requests

proxy={'https':"34.145.226.144:8080"}


url="https://httpbin.org/ip"

resp=requests.get(url,proxies=proxy)

print(resp.text)