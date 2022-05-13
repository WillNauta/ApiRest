import requests

url = "https://aerodatabox.p.rapidapi.com/flights/%7BsearchBy%7D/KL1395/2020-06-10"

headers = {
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com",
	"X-RapidAPI-Key": "50daa66138mshe5635556e23262ap1d5e26jsn564f8398c9ca"
}

response = requests.request("GET", url, headers=headers)

print(response.text)