# cobalt_py Python Wrapper
## About
This is a Python wrapper for the cobalt.tools API. With this wrapper, you can easily make requests to the cobalt API from your Python applications.

## Usage
First, import CobaltPy class from cobalt_py module
```python
from cobalt_py import CobaltPy
```
Then, create an instance for the cobalt.py
```python
cobalt_api_url = "https://co.wuk.sh"
cobaltpy = CobaltPy(cobalt_api_url)
```
Now, you can use the cobalt_api instance to make requests. Example:
```python
payload = {
    "url": "<insert_youtube_url_here>",
    "vCodec": "h264",
    "vQuality": "max",
    }
json_request_response = cobaltpy.json_request(payload)
print(json_request_response)
```

## License
This wrapper is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
