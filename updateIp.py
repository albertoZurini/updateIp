import requests, json, subprocess

AUTH_EMAIL = 'YOUR_EMAIL@YOUR_DOMAIN.com'
AUTH_KEY = 'YOUR_CLOUDFLARE_API_KEY'
DOMAIN = 'YOUR_DOMAIN.tk'

sync_ip = [DOMAIN, 'www.'+DOMAIN]

my_ip = subprocess.Popen("""dig TXT +short o-o.myaddr.l.google.com @ns1.google.com | awk -F'"' '{ print $2}'""", shell=True, stdout=subprocess.PIPE).stdout.read()
my_ip = str(my_ip).split("'")[1].split('\\')[0]

headers = {'X-Auth-Email': AUTH_EMAIL, 'X-Auth-Key': AUTH_KEY, 'Content-Type': 'application/json'}
zone_req = requests.get('https://api.cloudflare.com/client/v4/zones', headers=headers).json()

zone = ''

for result in zone_req['result']:
    if result['name']==DOMAIN:
        zone = result['id']

print("Zone: "+zone+"; IP: "+my_ip+"; Domains synced: ")
print(sync_ip)

record_req = requests.get('https://api.cloudflare.com/client/v4/zones/'+zone+'/dns_records', headers=headers).json()
print(record_req)

for result in record_req['result']:
    if result['name'] in sync_ip:
        cfId = result['id']
        data = {'type':'A','name':str(result['name']),'content':my_ip}
        update = requests.put('https://api.cloudflare.com/client/v4/zones/'+zone+'/dns_records/'+cfId, data=json.dumps(data), headers=headers).content
        print(update)
