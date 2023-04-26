# Your API KEYS (you need to use your own keys - very long random characters)

import requests

url = "https://mashvisor-api.p.rapidapi.com/rental-rates"

querystring = {"state":"CA","source":"airbnb","city":"Los Angeles","zip_code":"90291"}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "0a2679a9c0mshe4760d5ee1ce0dcp15c64ejsn38f0ead0c686",
	"X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()

print(response["content"]["retnal_rates"]["studio_value"])

studio_value = response["content"]["retnal_rates"]["studio_value"]
one_room_value = ["content"]["retnal_rates"]["one_room_value"]
two_room_value = ["content"]["retnal_rates"]["two_room_value"]
three_room_value = ["content"]["retnal_rates"]["three_room_value"]
four_room_value = ["content"]["retnal_rates"]["four_room_value"]




# def get_json(url: str) -> dict:
#     """
#     Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.
#     Both get_lat_long() and get_nearest_station() might need to use this function.
#     """
#     f = urllib.request.urlopen(url)
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#     return response_data


# def get_lat_long(place_name: str) -> tuple[str, str]:
#     """
#     Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.
#     See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
#     """
#     url=f'{MAPBOX_BASE_URL}/{place_name}.json?access_token={MAPBOX_TOKEN}&types=poi'
#     responses_data = get_json(url)
#     return [responses_data["features"][0]["center"][1],responses_data["features"][0]["center"][0]]




# def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
#     """
#     Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.
#     See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
#     """
    
#     MBTA_URL = f"https://api-v3.mbta.com/stops?api_key={MBTA_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    
#     responses_data =get_json(MBTA_URL)

#     return (responses_data['data'][0]["attributes"]['name'], responses_data['data'][0]["attributes"]['wheelchair_boarding'])



# def find_stop_near(place_name: str) -> tuple[str, bool]:
#     """
#     Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
#     This function might use all the functions above.
#     """
#     latitude, longitude = get_lat_long(place_name)

#     return get_nearest_station(latitude, longitude)


# def main():
#     """
#     You can test all the functions here
#     """
    
#     print(find_stop_near("brookline"))



# if __name__ == '__main__':
#     main()