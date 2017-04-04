import urllib
import urllib2
from pprint import pprint
from sets import SETS

QUERY = """
CONSTRUCT { ?s ?p ?o }
  WHERE {{?s ?p ?o .
    FILTER (?s in
      (
        <http://staging.eea.europa.eu/unicode-table/%s>
          ) ).
  }}
"""

sets = []
for k in sorted(SETS,
        cmp=lambda a, b: cmp(int(a.split('-')[0], 16), int(b.split('-')[0], 16))
    ):
    val = SETS[k].lower().replace(' ', '-')
    params = urllib.urlencode({"query": QUERY % val})
    url = "http://semantic.eea.europa.eu/sparql?%s" % params

    req = urllib2.Request(url)
    try:
        resp = urllib2.urlopen(req)
    except Exception as err:
        status = "ERROR"
    else:
        status = resp.code
        if 'char' not in resp.read():
            status = 'EMPTRY'

    print "| {k} | {val} | {status} |".format(k=k, val=val, status=status)
