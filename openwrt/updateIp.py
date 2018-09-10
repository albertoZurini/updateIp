#!/usr/bin/python
from __future__ import print_function
import requests, sys, json

AUTH_EMAIL = 'YOUR_EMAIL@YOUR_DOMAIN.com'
AUTH_KEY = 'YOUR_CLOUDFLARE_API_KEY'
DOMAIN = 'YOUR_DOMAIN.tk'

syncIp = [DOMAIN, 'www.'+DOMAIN]

if len(sys.argv) < 1:
    assert "NO IP WAS GIVEN"

my_ip = sys.argv[1]

headers = {'X-Auth-Email': AUTH_EMAIL, 'X-Auth-Key': AUTH_KEY, 'Content-Type': 'application/json'}
zone_req = requests.get('https://api.cloudflare.com/client/v4/zones', headers=headers).json()

zone = ''

for result in zone_req['result']:
    if result['name']==DOMAIN:
        zone = result['id']

print("Zone: "+zone+"; IP: "+my_ip+"; Domains synced: ")
print(syncIp)

record_req = requests.get('https://api.cloudflare.com/client/v4/zones/'+zone+'/dns_records', headers=headers).json()
print(record_req)

for result in record_req['result']:
    if result['name'] in syncIp:
        cfId = result['id']
        data = {'type':'A','name':str(result['name']),'content':my_ip}
        update = requests.put('https://api.cloudflare.com/client/v4/zones/'+zone+'/dns_records/'+cfId, data=json.dumps(data), headers=headers).content
        print(update)

