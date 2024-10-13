from homeassistant.components.device_tracker.config_entry import TrackerEntity
from homeassistant.helpers.event import async_track_state_change

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the GPS Coordinates Converter device tracker."""
    async_add_entities([GPSCoordinatesConverterTracker(hass)])

class GPSCoordinatesConverterTracker(TrackerEntity):
    def __init__(self, hass):
        """Initialize the GPS Coordinates Converter Device Tracker."""
        self._state = None
        self._latitude = None
        self._longitude = None
        self.hass = hass

        # Retrieve sensor names from the stored configuration
        latitude_sensor = hass.data["gps_coordinates_converter"]["latitude_sensor"]
        longitude_sensor = hass.data["gps_coordinates_converter"]["longitude_sensor"]

        async_track_state_change(
            hass, [latitude_sensor, longitude_sensor], self.update_position
        )

    @property
    def name(self):
        return "GPS Coordinates Converter"

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def should_poll(self):
        return False

    async def update_position(self, entity_id, old_state, new_state):
        """Update the GPS position based on sensors."""
        # Use the dynamically configured sensors to get latitude and longitude
        latitude_sensor = self.hass.data["gps_coordinates_converter"]["latitude_sensor"]
        longitude_sensor = self.hass.data["gps_coordinates_converter"]["longitude_sensor"]

        lat = self.hass.states.get(latitude_sensor)
        lon = self.hass.states.get(longitude_sensor)

        if lat and lon:
            self._latitude = float(lat.state)
            self._longitude = float(lon.state)

        self.async_write_ha_state()
