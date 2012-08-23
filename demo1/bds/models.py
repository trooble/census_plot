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

from django.db import models

# Create your models here.
class Bds(models.Model):
    year2 = models.IntegerField()
    state = models.CharField(null=True,max_length=2)
    sic1 = models.CharField(null=True,max_length=2)
    size = models.CharField(null=True,max_length=15)
    fsize = models.CharField(null=True,max_length=15)
    age4 = models.CharField(null=True,max_length=16)
    fage4 = models.CharField(null=True,max_length=16)
    firms = models.IntegerField(null=True)
    estabs = models.IntegerField(null=True)
    emp = models.IntegerField(null=True)
    denom = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    estabs_entry = models.IntegerField(null=True)
    estabs_entry_rate = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    estabs_exit = models.IntegerField(null=True)
    estabs_exit_rate = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    job_creation = models.IntegerField(null=True)
    job_creation_births = models.IntegerField(null=True)
    job_creation_continuers = models.IntegerField(null=True)
    job_creation_rate_births = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    job_creation_rate = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    job_destruction = models.IntegerField(null=True)
    job_destruction_deaths = models.IntegerField(null=True)
    job_destruction_continuers = models.IntegerField(null=True)
    job_destruction_rate_deaths = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    job_destruction_rate = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    net_job_creation = models.IntegerField(null=True)
    net_job_creation_rate = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    reallocation_rate = models.DecimalField(null=True,max_digits=10,decimal_places=1)
    d_flag = models.IntegerField(null=True)

class State(models.Model):
    code = models.CharField(max_length=2)
    abbreviation = models.CharField(max_length=2)
