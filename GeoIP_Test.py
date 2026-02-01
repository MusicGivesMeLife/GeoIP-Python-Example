import geoip2.database
from requests import get
import socket

def locate_IP(address):
	reader = geoip2.database.Reader('/var/lib/GeoIP/GeoLite2-City.mmdb')
	response = reader.city(address)
	human_response = (response.city.names['en'], response.subdivisions[0].iso_code, response.country.iso_code)
	return human_response

ipv4 = get('https://api.ipify.org').content.decode('utf8')

local = locate_IP(ipv4)
print('We are at: {}'.format(ipv4), "located in", local[0], local[1])

print('And the people reading our blog are at:')
with open('/home/pi/unique_IPs.txt') as file:
	while line := file.readline():
		try:
			print(line.rstrip(), ' is at ', locate_IP(line.rstrip()))
		except:
			try:
				print(line.rstrip(), ' is at ', locate_IP(socket.gethostbyname(line.rstrip())))
			except:
				pass
