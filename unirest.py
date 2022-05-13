import http.client

conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")

headers = {
    'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com",
    'X-RapidAPI-Key': "50daa66138mshe5635556e23262ap1d5e26jsn564f8398c9ca"
    }

conn.request("GET", "/flights/%7BsearchBy%7D/KL1395/2020-06-10", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))