# UpdateIp

Simple Python 3 script to update CloudFlare A record to match your dynamic IP (basically to access your firewall-free LAN using a domain from the WAN).

# How to use

1. Create a CloudFlare account and a domain
2. Update the nameservers of your domain accordingly to CF
3. Get a CF token and edit the script(s)
4. Run the script using Python 3

## Dependencies

`requests, json`

# How to edit

Open `updateIp.py` or `openwrt/updateIp.py` (for the openwrt-compatible version) and edit the `AUTH_*` and `DOMAIN` variables according to yours.

# How to install

If you are using the stand-alone version, just put it on the crontab.
If you are using the openwrt version, add it as script to run when the WAN IP has changed. This version will update the A record basing on the given shell parameter.