import requests
from datetime import datetime

CRAWL_CDX = "http://crawldb-fc.api.wa.bl.uk/fc"
ACCESS_CDX = "http://cdx.api.wa.bl.uk/data-heritrix"

class CDX11():    
    def __init__(self, line):
        self.urlkey, self.timestamp, self.original, self.mimetype, self.statuscode, \
        self.digest, self.redirecturl, self.robotflags, self.length, self.offset, self.filename = line.split(' ')

    def __str__(self):
        return ' '.join([self.urlkey, self.timestamp, self.original, self.mimetype, self.statuscode, \
        self.digest, self.redirecturl, self.robotflags, self.length, self.offset, self.filename])
    
    @property
    def crawl_date(self):
        return datetime.strptime(self.timestamp, '%Y%m%d%H%M%S')
    
    def to_dict(self):
        return {
            'urlkey': self.urlkey,
            'timestamp': self.timestamp, 
            'crawl_date': self.crawl_date,
            'original': self.original,
            'mimetype': self.mimetype,
            'statuscode': self.statuscode,
            'digest': self.digest, 
            'redirecturl': self.redirecturl, 
            'robotflags': self.robotflags, 
            'length': int(self.length), 
            'offset': int(self.offset), 
            'filename': self.filename
        }

def cdx_query(url, cdx_service=ACCESS_CDX, limit=25, sort='reverse'):
    r = requests.get(cdx_service, params = { 'url' : url, 'limit': limit, 'sort': sort} )
    if r.status_code == 200:
        for line in r.iter_lines(decode_unicode=True):
            cdx = CDX11(line)
            yield cdx
    elif r.status_code != 404:
        print("ERROR! %s" % r)

def cdx_scan(url, cdx_service=ACCESS_CDX, limit=10000):
    r = requests.get(cdx_service, params = { 'url' : url, 'limit': limit, 'matchType': 'prefix' } )
    if r.status_code == 200:
        for line in r.iter_lines(decode_unicode=True):
            cdx = CDX11(line)
            yield cdx
    elif r.status_code != 404:
        print("ERROR! %s" % r)
