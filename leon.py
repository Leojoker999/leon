import requests


# Requesting from the webiste to retrieve information ; using google as an example

res = requests.get('http://172.18.58.238/freebix')


# Writing IF else statement to determine whether it responses.
if res.status_code ==  200 :
    print("ok")
else:
    print('Failed')

print("Status code:")
print("\t *", res.status_code)

# Formatting the header output
print("Header:")
print("**********")

for x in res.headers:
    print("\t ", x, ":", res.headers[x])

print("**********")

# Changing the header to Mobile
headers = {'User-Agent' : 'Mobile'}
# Test it on an external site
url = 'http://172.18.58.238/headers.php'
resh = requests.get(url, headers=headers)
print(resh.text)

# Able to see the source code in a html page of the website for scrapping
output = open('index.html', 'w')

output.write(res.text)

output.close()


output.close()


