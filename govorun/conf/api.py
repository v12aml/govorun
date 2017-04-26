#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from oslo_config import cfg


API_SERVICE_OPTS = [
    cfg.PortOpt(
        'port',
        default=8012,
        help='The port for the govorun API server'),
    cfg.HostnameOpt(
        'host',
        default='127.0.0.1',
        help='The listen IP address for the govorun API server'
        ),
    cfg.BoolOpt(
        'enable_ssl',
        default=False,
        help="Enable the integrated stand-alone API to service "
             "requests via HTTPS instead of HTTP. If there is a "
             "front-end service performing HTTPS offloading from "
             "the service, this option should be False; note, you "
             "will want to change public API endpoint to represent "
             "SSL termination URL with 'public_endpoint' option."),
]


api = cfg.OptGroup(
    name='api',
    title='Options for the govorun API service')


def register_opts(conf):
    conf.register_group(api)
    conf.register_opts(API_SERVICE_OPTS, group=api)


def list_opts():
    return [('api', API_SERVICE_OPTS)]
