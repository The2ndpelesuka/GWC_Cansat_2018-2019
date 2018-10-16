import bme680

#Setup the sensor
try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
	sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

#Setup sensor settings
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

#Main class
class sensor:
	name = "bme680"
	
	def data():
		#Return data
		if sensor.get_sensor_data():
			return([sensor.data.temperature, sensor.data.pressure, sensor.data.humidity])
	
	def test():
		#Self test
		return True