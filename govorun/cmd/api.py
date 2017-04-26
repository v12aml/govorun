#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from oslo_log import log as logging

from oslo_config import cfg

from govorun.common import service
from govorun import conf

LOG = logging.getLogger(__name__)
CONF = conf.CONF


def main():
    server = service.WSGIService('govorun-api')
    launcher = service.launch(CONF, server)
    launcher.wait()


if __name__ == "__main__":
    main()
