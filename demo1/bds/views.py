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

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.db import connection
from bds.models import State
import matplotlib
matplotlib.use('SVG')
import matplotlib.pyplot as plt

class StringFile:
    """Acts as a file-like object to save the results of a plot while
       being able to return it as a string"""
    def __init__(self):
       self.inbuf = []
       self.outbuf = ''

    def write(self, s):
        self.inbuf.append(s)

    def read(self, n=0):
        self.outbuf = "".join(self.inbuf)
        if n:
            return self.outbuf[:n]
        else:
            return self.outbuf

def selections(request):
    t = loader.get_template('selections.html')
    states = State.objects.iterator()
    c = Context({'states': states})
    return HttpResponse(t.render(Context(c)))

def chart(request):
    params = dict(request.GET.lists())
    if params.has_key("state") and params.has_key("indicator"):
        svgplot = do_plot(params)
        t = loader.get_template('chart.html')
        c = Context({
             'svg': svgplot
        })
        return HttpResponse(t.render(c))
    else:
        t = loader.get_template('selections.html')
        states = State.objects.iterator()
        c = Context({'states': states, 'missing_params': 1})
        return HttpResponse(t.render(Context(c)))
#        return HttpResponseRedirect(reverse('bds.views.selections'))

def do_plot(lists):
    cur = connection.cursor()
    sf = StringFile()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    states = lists.get('state')
    indicator = lists.get('indicator')[0]
    plt.title(indicator.replace('_', ' ').capitalize())
    for state in states: 
        cur.execute("select year2, sum(coalesce(" + indicator + ", 0)) \
                     from bds_bds \
                     where state = %s \
                     group by year2 \
                     order by year2", (state,))
        data = cur.fetchall()
        [xlab,ylab] = data[0]
        x = [i[0] for i in data]
        y = [i[1] for i in data]
        ax.annotate(state, xy=(xlab,ylab), clip_on=False)
        ax.plot(x,y)
    fig.savefig(sf)
    return sf.read()
