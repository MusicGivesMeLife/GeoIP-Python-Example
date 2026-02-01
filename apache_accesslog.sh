#!/bin/sh
cat /var/log/apache2/access.log | awk '{print $1}' | sort -n | uniq >> unique_IPs.txt
cat /var/log/apache2/access.log.1 | awk '{print $1}' | sort -n | uniq >> unique_IPs.txt
rm unique_hosts.txt
python GeoIP_Test.py >> unique_hosts.txt
rm unique_IPs.txt
cat unique_hosts.txt
exit 0
