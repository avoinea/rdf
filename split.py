from sets import SETS

RDF = u"""<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
{sets}
</rdf:RDF>
"""

SET = u"""<rdf:UnicodeSet rdf:about="{name}">
{chars}
 </rdf:UnicodeSet>"""

CHAR = u"""  <rdf:char{x}>{char}</rdf:char{x}>"""

sets = []
for k in sorted(SETS,
        cmp=lambda a, b: cmp(int(a.split('-')[0], 16), int(b.split('-')[0], 16))
    ):
    name = SETS[k].lower().replace(' ', '-')
    start, stop = k.split('-')
    start = int(start, 16)
    stop = int(stop, 16) + 1
    lines = []
    for x in range(start, stop):
        lines.append(CHAR.format(char=unichr(x), x=x))
    sets.append(SET.format(chars=u"\n".join(lines), name=name))
    rdf = RDF.format(sets=u"\n".join(sets))
    with open('split/{name}.rdf'.format(name=name), 'w') as ofile:
       ofile.write(rdf.encode("utf-8"))
    sets = []
