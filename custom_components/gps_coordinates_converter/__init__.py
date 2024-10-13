"""Set up the GPS Coordinates Converter integration."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the GPS Coordinates Converter component from configuration.yaml."""
    
    # Retrieve the sensor names from configuration.yaml
    latitude_sensor = config["gps_coordinates_converter"].get("latitude_sensor")
    longitude_sensor = config["gps_coordinates_converter"].get("longitude_sensor")

    # Store them in `hass.data` so other parts of your integration can access them
    hass.data["gps_coordinates_converter"] = {
        "latitude_sensor": latitude_sensor,
        "longitude_sensor": longitude_sensor,
    }

    # Return True to indicate successful setup
    return True
