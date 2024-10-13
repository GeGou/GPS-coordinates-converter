from homeassistant.components.sensor import SensorEntity
from homeassistant.const import ATTR_LATITUDE, ATTR_LONGITUDE

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up GPS Coordinates Converter sensors."""
    async_add_entities([GPSLatitudeSensor(hass), GPSLongitudeSensor(hass)])

class GPSLatitudeSensor(SensorEntity):
    def __init__(self, hass):
        """Initialize the Latitude sensor for GPS Coordinates Converter."""
        self._state = None
        self.hass = hass

    @property
    def name(self):
        return "GPS Coordinates Latitude"

    @property
    def state(self):
        return self.hass.states.get("sensor.latitude").state if self.hass.states.get("sensor.latitude") else None

    @property
    def unit_of_measurement(self):
        return "°"

    @property
    def icon(self):
        return "mdi:map-marker"

class GPSLongitudeSensor(SensorEntity):
    def __init__(self, hass):
        """Initialize the Longitude sensor for GPS Coordinates Converter."""
        self._state = None
        self.hass = hass

    @property
    def name(self):
        return "GPS Coordinates Longitude"

    @property
    def state(self):
        return self.hass.states.get("sensor.longitude").state if self.hass.states.get("sensor.longitude") else None

    @property
    def unit_of_measurement(self):
        return "°"

    @property
    def icon(self):
        return "mdi:map-marker"
