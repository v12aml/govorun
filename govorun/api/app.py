#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pecan

from oslo_config import cfg

from govorun.api import hooks
from govorun import conf


CONF = conf.CONF

server = {
    'port': '8012',
    'host': '127.0.0.1'
}

app = {
    'root': 'govorun.api.controllers.root.RootController',
    'modules': ['govorun.api'],
    'hooks': [
        hooks.ContextHook(),
        hooks.NoExceptionTracebackHook(),
    ],
    'static_root': '%(confdir)s/public',
}

wsme = {
    'debug': cfg.CONF.get("debug") if "debug" in cfg.CONF else False,
}

PECAN_CONFIG = {
    "server": server,
    "app": app,
    "wsme": wsme,
}


def get_pecan_config():
    # Set up the pecan configuration
    return pecan.configuration.conf_from_dict(PECAN_CONFIG)


def setup_app(config=None):
    if not config:
        config = get_pecan_config()

    app_conf = dict(config.app)

    return pecan.make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        debug=CONF.debug,
        **app_conf
    )


class VersionSelectorApplication(object):
    def __init__(self):
        pc = get_pecan_config()
        self.v1 = setup_app(config=pc)

    def __call__(self, environ, start_response):
        return self.v1(environ, start_response)
