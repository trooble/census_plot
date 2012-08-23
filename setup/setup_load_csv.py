# Copyright 2012 Karim Sumun
#
# This file is part of Simple Census Plotter.
#
# Simple Census Plotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import psycopg2, csv, sys

# Should be a BDS csv file
fh = open(sys.argv[1], 'r')
r = csv.reader(fh)

# Header row
cols = r.next()
sql = 'insert into bds_bds (' \
      + reduce(lambda x,y: x+','+y, cols) \
      + ') values (%s' \
      + (',%s' * (len(cols) - 1)) + ');'

print sql
conn = psycopg2.connect('dbname=demo1 user=demo1 password=demo1')
cur = conn.cursor()

line=2
try:
    for row in r:
        rowout = []
        for i in range(len(row)):
            if row[i] == '':
                rowout.append(None)
            else:
                rowout.append(row[i])
        cur.execute(sql, rowout)
        line=line+1
except psycopg2.DataError:
    print 'DataError at line ' + str(line)
    raise

conn.commit()
cur.close()
conn.close()
