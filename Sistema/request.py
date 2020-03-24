import json
import requests


print("Pull request")
if __name__ == "__main__":
	response = requests.get("https://api.mobygames.com/v1/genres?api_key=DFn2Ua5s6hGcwNRsLtrw1g==")
	data = json.loads(response.text)
	print(response.json())
	for element in data:
		print("Elemento:",element)
		