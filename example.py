# import the module
import python_weather
import asyncio
import os

async def getweather():
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(format=python_weather.IMPERIAL) as client:

    # fetch a weather forecast from a city
    weather = await client.get("35406")

    # current conditions
    print("Description: " + str(weather.current.description))
    print("Current Temp: " + str(weather.current.temperature) + "F")
    print("Feels Like: " + str(weather.current.feels_like) + "F")
    print("Current Wind Speed: " + str(weather.current.wind_speed) + "mph")
    print("Current Wind Direction: " + str(weather.current.wind_direction))
    print("Current Humidity: " + str(weather.current.humidity) + "%")
    print("Precipitation: " + str(weather.current.precipitation))
    print("Pressure: " + str(weather.current.pressure) + "mb")
    print("Visibility: " + str(weather.current.visibility))
    print("UV Index: " + str(weather.current.uv_index) + "%")





    #weather.current.chance_of_thunder,weather.current.chance_of_rewdry,weather.current.cloud_cover,weather.current.lowest_temperature,weather.current.highest_temperature,weather.current.sun_set,weather.current.sun_rise,weather.current.moon_set,weather.current.moon_rise,weather.current.moon_phase,weather.current.moon_illumination

    # setup forcast arrays
    dates = []
    lowest_temps = []
    highest_temps = []
    sun_shines = []
    snow_width = []
    astro = []
    dew_points = []
    heat_indexes = []
    wind_gusts = []
    wind_chills = []
    fog_chances = []
    frost_chances = []
    rain_chances = []
    snow_chances = []
    overcast_chances = []
    sunshine_chances = []
    windy_chances = []
    hightemp_chances = []
    f = 0
    h = 0
    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        dates.append(forecast.date);
        lowest_temps.append(forecast.lowest_temperature);
        highest_temps.append(forecast.highest_temperature);
        sun_shines.append(forecast.sun_shines);
        snow_width.append(forecast.snow_width);
        astro.append(forecast.astronomy);
        f += 1;
        for hourly in forecast.hourly:
            dew_points.append(hourly.dew_point);
            heat_indexes.append(hourly.heat_index);
            wind_gusts.append(hourly.wind_gust);
            wind_chills.append(hourly.wind_chill);
            fog_chances.append(hourly.chance_of_fog);
            frost_chances.append(hourly.chance_of_frost);
            rain_chances.append(hourly.chance_of_rain);
            snow_chances.append(hourly.chance_of_snow);
            overcast_chances.append(hourly.chance_of_overcast);
            sunshine_chances.append(hourly.chance_of_sunshine);
            windy_chances.append(hourly.chance_of_windy);
            hightemp_chances.append(hourly.chance_of_hightemp);
            h += 1;

    print("Dew Point: " + str(dew_points[0]) + "F")
    print("Heat Index: " + str(heat_indexes[0]) + "F")
    print("Wind Gust: " + str(wind_gusts[0]) + " MPH")
    print("Wind Chill: " + str(wind_chills[0]) + "F")
    print("Chance of Rain: " + str(rain_chances[0]) + "%")
    print("Chance of Fog: " + str(fog_chances[0]) + "%")
    print("Chance of Frost: " + str(frost_chances[0]) + "%")
    print("Chance of Snow: " + str(snow_chances[0]) + "%")
    print("Chance of Overcast: " + str(overcast_chances[0]) + "%")
    print("Chance of Sunshine: " + str(sunshine_chances[0]) + "%")
    print("Chance of Wind: " + str(windy_chances[0]) + "%")
    print("Chance of High Temp: " + str(hightemp_chances[0]) + "%")

        #print(forecast)


      # hourly forecasts
      #for hourly in forecast.hourly:
        #print(f' --> {hourly!r}')

if __name__ == "__main__":
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())
