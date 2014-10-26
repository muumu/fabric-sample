# -*- coding: utf-8 -*-

import conf
from fabric.api import env
from abc import ABCMeta, abstractmethod

# 各コンポーネントが持っているべきメソッドを宣言します
# 実際のシステムでは全プロセスを止めるstopとかもあるべきかと思います
class Component:
    __metaclass__ = ABCMeta
    @abstractmethod
    def service_out(self, hosts): pass

    @abstractmethod
    def service_in(self, hosts): pass

    @abstractmethod
    def restart(self, hosts): pass

# 大規模システムだとサーバー情報を入れたDBからホスト名を引いてくるかと思いますが
# ここでは簡単のため@rolesデコレータとして利用可能なenv.roledefsを使用します
def get_hosts(role_name):
    if role_name not in env.roledefs:
        raise Exception('Invalid role name: %s' % role_name)
    return env.roledefs[role_name]

# ホスト名からロール名を取得する関数です
# これも簡単のため単にenv.roledefsから逆引き
def get_role(hostname):
    for role, hosts in env.roledefs.items():
        if hostname in hosts:
            return role
    raise Exception('Invalid hostname: %s' % hostname)


