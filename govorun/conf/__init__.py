#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from oslo_config import cfg
from govorun.conf import api


CONF = cfg.CONF

api.register_opts(CONF)
