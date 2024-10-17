# GPS-coordinates-converter
Converts coordinates (latitude, longitude) to location and creates a device_tracker entity

Add the following to configuration.yaml:

gps_coordinates_converter:
  latitude_sensor: sensor.esp32_NEO-6M_GPS_Module_latitude
  longitude_sensor: sensor.esp32_NEO-6M_GPS_Module_longitude

where 'esp32_NEO-6M_GPS_Module_latitude' and 'esp32_NEO-6M_GPS_Module_longitude' is 
the name of your sensor that provides the latitude and longitude.
