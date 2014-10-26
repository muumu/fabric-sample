# -*- coding: utf-8 -*-

from common import Component, get_hosts
from fabric.api import run, execute
from functools import partial

def service_out(hostname):
    run('echo "service out %s"' % hostname)

def service_in(hostname):
    run('echo "service in %s"' % hostname)

def restart():
    run('echo "restart"')

def backup():
    run('echo "Backup database"')

class Database(Component):
    def service_out(self, *hosts):
        for host in hosts:
            execute(partial(service_out, host), hosts=get_hosts('ap'))
    def service_in(self, *hosts):
        for host in hosts:
            execute(partial(service_in, host), hosts=get_hosts('ap'))
    def restart(self, hosts):
        execute(restart, hosts=hosts)
    def backup(self, hosts):
        execute(backup, hosts=hosts)

