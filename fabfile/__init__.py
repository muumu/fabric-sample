# -*- coding: utf-8 -*-

import web, ap, db
from common import get_hosts, get_role
from fabric.api import sudo, execute
from fabric.decorators import task
from functools import partial

components = {
    'web': web.Web(),
    'ap': ap.Application(),
    'db': db.Database()
}

# デプロイ名を指定して各種デプロイを行う関数
def deploy(name):
    if name == 'update_pkgs':
        sudo('echo "Update packages"')
    else:
        raise Exception('Unknown deploy command %s' % name)

# 任意個のデプロイをFabricタスクとして呼び出す関数
def do_deploys(deploys, hosts):
    for d in deploys:
        execute(partial(deploy, d), hosts=hosts)

# 障害時などにホスト名を指定してサービスアウトを行うタスク
@task
def service_out(hostname):
    components[get_role(hostname)].service_out(hostname)

# 障害復旧時などにホスト名を指定してサービスインを行うタスク
@task
def service_in(hostname):
    c = components[get_role(hostname)]
    c.restart(hostname)
    c.service_in(hostname)

# パッケージ更新などのデプロイをコンポーネント指定でまとめて行うタスク
# サービスアウト、デプロイ、プロセス再起動、サービスインを順に行います
@task
def release(target, *deploys):
    c = components[target]
    # 一連のプロセスはサーバ1台毎に行う
    for host in get_hosts(target):
        c.service_out(host)
        do_deploys(deploys, host)
        c.restart(host)
        c.service_in(host)

@task
def backup_db():
    db.Database().backup(get_hosts('db'))
