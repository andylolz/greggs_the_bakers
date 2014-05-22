import urllib2, urllib, json, csv
import scraperwiki


headers = {'X-Requested-With': 'XMLHttpRequest'}
data = urllib.urlencode({
    'Position': '0,0',
    'Bounds': '-100,-100,100,100',
})
url = 'https://www.greggs.co.uk/home/shop-finder'

# run the request
raw_res = urllib2.urlopen(urllib2.Request(
    url,
    data=data,
    headers=headers,
)).read()

# jsonify and listify the output
res = [{'id': id_, 'name': x['Name'], 'lat': x['Latitude'], 'long': x['Longitude'], 'phone': x['Telephone'], 'addr': x['HTMLAddress']} for id_, x in json.loads(raw_res).items()]

# save it
scraperwiki.sqlite.save(unique_keys=['id'], data=res)

# with open('out.csv', 'wb') as f:
#     w = csv.DictWriter(f, res[0].keys())
#     w.writeheader()
#     w.writerows(res)
