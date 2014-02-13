#!/usr/bin/python
# encoding: utf-8
 
import requests
import xml.dom.minidom

sonos_ip = "10.0.1.3:1400"
soap_action = '"urn:schemas-upnp-org:service:AVTransport:1#Pause"'
request = u"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:Pause xmlns:u="urn:schemas-upnp-org:service:AVTransport:1"><InstanceID>0</InstanceID></u:Pause></s:Body></s:Envelope>"""

encoded_request = request.encode('utf-8')
url = "http://" + sonos_ip + "/MediaRenderer/AVTransport/Control"
 
headers = {"HOST": sonos_ip,
           "CONTENT-TYPE": "text/xml; charset=UTF-8",
           "CONTENT-LENGTH": len(encoded_request),
           "USER-AGENT": """Linux UPnP/1.0 Sonos/24.0-68210o (MDCR_MacBookAir4,2)""",
           "SOAPACTION": soap_action
			}
                           
response = requests.post(url=url,
                         headers = headers,
                         data = encoded_request,
                         verify=False)

response = xml.dom.minidom.parseString(response.text)
response = response.toprettyxml()

print unicode(response)