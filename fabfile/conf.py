# -*- coding: utf-8 -*-

from fabric.api import env

env.roledefs = {
    'web': ['web01.example.com', 'web02.example.com'],
    'ap': ['ap01.example.com', 'ap02.example.com'],
    'db': ['db01.example.com', 'db02.example.com']
}

env.eagerly_disconnect = True
env.use_ssh_config = True
