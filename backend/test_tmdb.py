import requests


API_KEY = "ba69cdc31d8c469e4e8a90c6fec53702"


url = "https://api.themoviedb.org/3/trending/movie/week"


params = {
    "api_key": API_KEY
}


response = requests.get(
    url,
    params=params,
    timeout=30
)


print(response.status_code)

print(response.json())