from cobalt_py import CobaltPy
# Declare wrapper
cobalt_api_url = "https://co.wuk.sh"
cobaltpy = CobaltPy(cobalt_api_url)

# GET server info
server_info_response = cobaltpy.server_info()
print(server_info_response)

# POST video link with options
payload = {
    "url": "<insert_youtube_url_here>",
    "vCodec": "h264",
    "vQuality": "max",
    }
json_request_response = cobaltpy.json_request(payload)
print(json_request_response)