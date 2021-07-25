#!/usr/bin/env python
# from https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s04.html
import os, sys

nargs = len(sys.argv)

if not 3 <= nargs <= 5:
    print "usage: %s search_text replace_text [infile [outfile]]" % \
        os.path.basename(sys.argv[0])
else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    input = sys.stdin
    output = sys.stdout
    if nargs > 3:
        input = open(sys.argv[3])
    if nargs > 4:
        output = open(sys.argv[4], 'w')
    # #perform the search and replace one line at at time
    for s in input.xreadlines(  ):
        output.write(s.replace(stext, rtext))
    output.close(  )
	# # perform the search and replace with the whole file in memory
    # output.write(input.read(  ).replace(stext, rtext))
    input.close(  )