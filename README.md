# GeoIP-Python-Example
A simple bash/python script combo to sort unique IPs or hostnames from an Apache log and return their GeoIP information

##Requirements
Python GeoIP2 library as well as the city GeoIP database from MaxMind. If you don't have those yet, Google is free.

##How it works
The bash script uses some fancy one-liners to pull a list of unique IP addresses from the Apache2 access log, saves it to a text file, then calls the python script which iterates through said file, printing the location of each address (resolving domain names to IPs if necessary).

That's all folks.

Made these scripts for personal use out of boredom, and figured they were a decent example of how to use the GeoIP2 Python library.
