---
title: OpenWeather
category: misc
source_lines: 76624-76647
line_count: 23
---

# OpenWeather
Source: https://docs.agno.com/tools/toolkits/others/openweather



**OpenWeatherTools** enable an Agent to access weather data from the OpenWeatherMap API.

## Prerequisites

The following example requires the `requests` library and an API key which can be obtained from [OpenWeatherMap](https://openweathermap.org/api). Once you sign up the mentioned api key will be activated in a few hours so please be patient.

```shell
export OPENWEATHER_API_KEY=***
```

## Example

The following agent will use OpenWeatherMap to get current weather information for Tokyo.

```python cookbook/tools/openweather_tools.py
from agno.agent import Agent
from agno.tools.openweather import OpenWeatherTools

