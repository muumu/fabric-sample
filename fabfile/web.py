# -*- coding: utf-8 -*-

from common import Component
from fabric.api import run, execute

def service_out():
    run('echo "service out"')

def service_in():
    run('echo "service in"')

def restart():
    run('echo "restart"')

class Web(Component):
    def service_out(self, hosts):
        execute(service_out, hosts=hosts)
    def service_in(self, hosts):
        execute(service_in, hosts=hosts)
    def restart(self, hosts):
        execute(restart, hosts=hosts)
