import requests
import time
import yaml
import os

# Helium Integration
#
# from helium import *

# start_chrome(
#     "https://www.surfline.com/surf-report/river-jetties/5842041f4e65fad6a77088ee?camId=5834a0223421b20545c4b581"
# )
# time.sleep(3)
# kill_browser()


def get_all_data():
    s = requests.Session()

    # get 5 days of wave conditions
    response = s.get(
        "https://services.surfline.com/kbyg/regions/forecasts/conditions?subregionId=58581a836630e24c44878fd6&days=5"
    )

    yaml_urls = {
        "rating": "https://services.surfline.com/kbyg/spots/forecasts/rating?spotId=5842041f4e65fad6a77088ee&days=5&intervalHours=1&cacheEnabled=true",
        "surf": "https://services.surfline.com/kbyg/spots/forecasts/surf?cacheEnabled=true&days=5&intervalHours=1&spotId=5842041f4e65fad6a77088ee&units%5BwaveHeight%5D=FT",
        "swells": "https://services.surfline.com/kbyg/spots/forecasts/swells?cacheEnabled=true&days=5&intervalHours=1&spotId=5842041f4e65fad6a77088ee&units%5BswellHeight%5D=FT",
        "wind": "https://services.surfline.com/kbyg/spots/forecasts/wind?spotId=5842041f4e65fad6a77088ee&days=5&intervalHours=1&corrected=false&cacheEnabled=true&units%5BwindSpeed%5D=KTS",
        "sunlight": "https://services.surfline.com/kbyg/spots/forecasts/sunlight?spotId=5842041f4e65fad6a77088ee&days=16&intervalHours=1",
        "tides": "https://services.surfline.com/kbyg/spots/forecasts/tides?spotId=5842041f4e65fad6a77088ee&days=6&cacheEnabled=true&units%5BtideHeight%5D=FT",
        "weather": "https://services.surfline.com/kbyg/spots/forecasts/weather?spotId=5842041f4e65fad6a77088ee&days=16&intervalHours=1&cacheEnabled=true&units%5Btemperature%5D=F",
    }

    timestamp = int(time.time())

    for key, url in yaml_urls.items():
        response = s.get(url)
        yaml_data = response.json()

        directory = f"surfline_data/{timestamp}"

        # Ensure directory exists
        os.makedirs(directory, exist_ok=True)

        # Save JSON data to a file as YAML
        with open(f"{directory}/{key}.yaml", "w") as yaml_file:
            yaml.dump(yaml_data, yaml_file, allow_unicode=True)

    print(yaml_data)


get_all_data()
