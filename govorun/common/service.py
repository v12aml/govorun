#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from oslo_log import log
from oslo_service import service
from oslo_service import wsgi
from oslo_config import cfg
from oslo_concurrency import processutils


from govorun.api import app

CONF = cfg.CONF
LOG = log.getLogger(__name__)


class WSGIService(service.ServiceBase):
    """  """
    def __init__(self, service_name):
        """Initialize, but do not start the WSGI server.
        :param service_name: The service name of the WSGI server.
        """
        self.service_name = service_name
        self.app = app.VersionSelectorApplication()
        self.workers = (
            CONF.api.workers or processutils.get_worker_count())
        self.server = wsgi.Server(
            CONF,
            self.service_name,
            self.app,
            host=CONF.api.host,
            port=CONF.api.port,
            use_ssl=False,
            logger_name=self.service_name)

    def start(self):
        print("start")
        self.server.start()

    def stop(self):
        print("stop")
        self.server.stop()

    def wait(self):
        print("wait")
        self.server.wait()

    def reset(self):
        print("reset")
        self.server.reset()


def launch(conf, service_):
    return service.launch(conf, service_)
