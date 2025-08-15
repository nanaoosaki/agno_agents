---
title: Google Maps
category: misc
source_lines: 75847-75927
line_count: 80
---

# Google Maps
Source: https://docs.agno.com/tools/toolkits/others/google_maps

Tools for interacting with Google Maps services including place search, directions, geocoding, and more

**GoogleMapTools** enable an Agent to interact with various Google Maps services for location-based operations including place search, directions, geocoding, and more.

## Prerequisites

The following example requires the `googlemaps` library and an API key which can be obtained from the [Google Cloud Console](https://console.cloud.google.com/projectselector2/google/maps-apis/credentials).

```shell
pip install googlemaps
```

```shell
export GOOGLE_MAPS_API_KEY=your_api_key_here
```

You'll need to enable the following APIs in your Google Cloud Console:

* Places API
* Directions API
* Geocoding API
* Address Validation API
* Distance Matrix API
* Elevation API
* Time Zone API

## Example

Basic usage of the Google Maps toolkit:

```python
from agno.agent import Agent
from agno.tools.google_maps import GoogleMapTools

agent = Agent(tools=[GoogleMapTools()], show_tool_calls=True)
agent.print_response("Find coffee shops in San Francisco")
```

For more examples, see the [Google Maps Tools Examples](/examples/concepts/tools/others/google_maps).

## Toolkit Params

| Parameter             | Type            | Default | Description                                                                         |
| --------------------- | --------------- | ------- | ----------------------------------------------------------------------------------- |
| `key`                 | `Optional[str]` | `None`  | Optional API key. If not provided, uses GOOGLE\_MAPS\_API\_KEY environment variable |
| `search_places`       | `bool`          | `True`  | Enable places search functionality                                                  |
| `get_directions`      | `bool`          | `True`  | Enable directions functionality                                                     |
| `validate_address`    | `bool`          | `True`  | Enable address validation functionality                                             |
| `geocode_address`     | `bool`          | `True`  | Enable geocoding functionality                                                      |
| `reverse_geocode`     | `bool`          | `True`  | Enable reverse geocoding functionality                                              |
| `get_distance_matrix` | `bool`          | `True`  | Enable distance matrix functionality                                                |
| `get_elevation`       | `bool`          | `True`  | Enable elevation functionality                                                      |
| `get_timezone`        | `bool`          | `True`  | Enable timezone functionality                                                       |

## Toolkit Functions

| Function              | Description                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_places`       | Search for places using Google Maps Places API. Parameters: `query` (str) for the search query. Returns stringified JSON with place details including name, address, phone, website, rating, and hours.   |
| `get_directions`      | Get directions between locations. Parameters: `origin` (str), `destination` (str), optional `mode` (str) for travel mode, optional `avoid` (List\[str]) for features to avoid. Returns route information. |
| `validate_address`    | Validate an address. Parameters: `address` (str), optional `region_code` (str), optional `locality` (str). Returns address validation results.                                                            |
| `geocode_address`     | Convert address to coordinates. Parameters: `address` (str), optional `region` (str). Returns location information with coordinates.                                                                      |
| `reverse_geocode`     | Convert coordinates to address. Parameters: `lat` (float), `lng` (float), optional `result_type` and `location_type` (List\[str]). Returns address information.                                           |
| `get_distance_matrix` | Calculate distances between locations. Parameters: `origins` (List\[str]), `destinations` (List\[str]), optional `mode` (str) and `avoid` (List\[str]). Returns distance and duration matrix.             |
| `get_elevation`       | Get elevation for a location. Parameters: `lat` (float), `lng` (float). Returns elevation data.                                                                                                           |
| `get_timezone`        | Get timezone for a location. Parameters: `lat` (float), `lng` (float), optional `timestamp` (datetime). Returns timezone information.                                                                     |

## Rate Limits

Google Maps APIs have usage limits and quotas that vary by service and billing plan. Please refer to the [Google Maps Platform pricing](https://cloud.google.com/maps-platform/pricing) for details.

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/google_maps.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/google_maps_tools.py)


