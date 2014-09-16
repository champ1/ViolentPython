import pygeoip
gi = pygeoip.GeoIP('GeoLiteCity.dat')

def printRecord(tgt):

  rec = gi.record_by_name(tgt)
  city = rec['city']
  region = rec['region_name']
  country = rec['country_name']
  long = rec['longitude']
  lat = rec['latitude']
  print 'Target:' + tgt + ' Geo-located.'
  print ':' +str(city) + str(region) + str(country)
  print 'Latitude:' + str(lat) +str(long)

tgt = '90.201.120.115'
printRecord(tgt)
