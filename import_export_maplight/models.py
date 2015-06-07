# import_export_maplight/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.db import models

class MapLightContest(models.Model):
    election_date = models.DateField('election date', default=None, null=True, blank=True) # "2014-09-03"
    contest_id = models.CharField(verbose_name='contest id',
                                       max_length=255, null=False, blank=False, unique=True) # "O1524"
    title = models.CharField(verbose_name='title',
                                       max_length=255, null=False, blank=False, unique=False) # "Governor - California"
    type = models.CharField(verbose_name='type',
                                       max_length=255, null=False, blank=False, unique=False) # "office"
    url = models.CharField(verbose_name='url',
                                       max_length=255, null=False, blank=False, unique=False) # "http://votersedge.org/california/2014/november/state/candidates/governor"

class MapLightPolitician(models.Model):
    candidate_id = models.IntegerField(verbose_name='candidate id', null=False, blank=False, unique=True) # "5746"
    display_name = models.CharField(verbose_name='display name',
                                       max_length=255, null=False, blank=False, unique=False) # "Jerry Brown"
    first_name = models.CharField(verbose_name='first name',
                                       max_length=255, null=False, blank=True, unique=False)
    models.CharField(verbose_name='display name',
                                       max_length=255, null=False, blank=False, unique=False)
    gender = models.CharField(verbose_name='gender',
                                       max_length=1, null=False, blank=False, default='U', unique=False) # "M"
    last_funding_update = models.DateField('last funding update date', default=None, null=True, blank=True) # "2014-09-03"
    last_name = models.CharField(verbose_name='last name',
                                       max_length=255, null=False, blank=True, unique=False) # "Brown"
    middle_name = models.CharField(verbose_name='middle name',
                                       max_length=255, null=False, blank=False, unique=False)
    name_prefix = models.CharField(verbose_name='name prefix',
                                       max_length=255, null=False, blank=True, unique=False)
    name_suffix = models.CharField(verbose_name='name suffix',
                                       max_length=255, null=False, blank=True, unique=False)
    original_name = models.CharField(verbose_name='original name',
                                       max_length=255, null=False, blank=True, unique=False) # "Edmund G Brown"
    party = models.CharField(verbose_name='political party',
                                       max_length=255, null=False, blank=True, unique=False) # "Democratic"
    photo = models.CharField(verbose_name='photo url',
                                       max_length=255, null=False, blank=True, unique=False) # "http://votersedge.org/sites/all/modules/map/modules/map_proposition/images/politicians/2633.jpg?v"
    politician_id = models.IntegerField(verbose_name='politician id', null=False, blank=False, unique=True) # "2633"
    roster_name = models.CharField(verbose_name='roster name',
                                       max_length=255, null=False, blank=True, unique=False) # "Jerry Brown"
    type = models.CharField(verbose_name='type',
                                       max_length=255, null=False, blank=True, unique=False)
    url = models.CharField(verbose_name='url',
                                       max_length=255, null=False, blank=True, unique=False) # "http://votersedge.org/california/2014/november/state/candidates/governor/2633-jerry-brown"
