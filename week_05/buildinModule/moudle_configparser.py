#! /usr/bin/env python

import configparser # Configparser

# http://www.cnblogs.com/alex3714/articles/5161349.html

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)

    # [DEFAULT]
    # ServerAliveInterval = 45
    # Compression = yes
    # CompressionLevel = 9
    # ForwardX11 = yes
    #
    # [bitbucket.org]
    # User = hg
    #
    # [topsecret.server.com]
    # Port = 50022
    # ForwardX11 = no

config = configparser.ConfigParser()
sections = config.sections()
print(sections)

print(config.read('example.ini'))
sections = config.sections()

print(config.defaults())
print(sections)
print('========================================')
print('bitbucket.org' in config)

print('bytebong.com' in config)
print('========================================')
print(config['bitbucket.org']['User'])

print(config['DEFAULT']['Compression'])

print('========================================')
topsecret = config['topsecret.server.com'] # topsecret.server.com
print(topsecret['forwardX11'])

print(topsecret['host port'])

print('========================================')

for key in config['bitbucket.org']:
    print(key, config['bitbucket.org'][key])

print('========================================')
print(config['bitbucket.org']['ForwardX11'])