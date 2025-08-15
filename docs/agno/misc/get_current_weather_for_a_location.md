---
title: Get current weather for a location
category: misc
source_lines: 76657-76687
line_count: 30
---

# Get current weather for a location
agent.print_response("What's the current weather in Tokyo?", markdown=True)
```

## Toolkit Params

| Parameter         | Type   | Default  | Description                                                                  |
| ----------------- | ------ | -------- | ---------------------------------------------------------------------------- |
| `api_key`         | `str`  | `None`   | OpenWeatherMap API key. If not provided, uses OPENWEATHER\_API\_KEY env var. |
| `units`           | `str`  | `metric` | Units of measurement. Options: 'standard', 'metric', 'imperial'.             |
| `current_weather` | `bool` | `True`   | Enable current weather function.                                             |
| `forecast`        | `bool` | `True`   | Enable forecast function.                                                    |
| `air_pollution`   | `bool` | `True`   | Enable air pollution function.                                               |
| `geocoding`       | `bool` | `True`   | Enable geocoding function.                                                   |

## Toolkit Functions

| Function              | Description                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------- |
| `get_current_weather` | Gets current weather data for a location. Takes a location name (e.g., "London").                    |
| `get_forecast`        | Gets weather forecast for a location. Takes a location name and optional number of days (default 5). |
| `get_air_pollution`   | Gets current air pollution data for a location. Takes a location name.                               |
| `geocode_location`    | Converts a location name to geographic coordinates. Takes a location name and optional result limit. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/openweather.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/openweather_tools.py)


