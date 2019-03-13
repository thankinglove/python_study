__author__ = "Alex Li"

import configparser

conf = configparser.ConfigParser()

# print(type(conf))
# print(help(conf))

data = conf.read("example.ini")

# print(conf.items())

# print(conf.sections())

sec = conf.sections()
print(sec)

for i in sec:
    print(i)
    for key in conf[i]:
        print(key, ' = ', conf[i][key])

# for default in conf['DEFAULT']:
#     print(default, '=', conf['DEFALUT'][default])

print(conf.items())

# print(conf['topsecret.server.com'])


# print(conf['DEFAULT'])
# print(conf['bitbucket.org']['user'])
# print(conf.sections())
# sec = conf.remove_section('bitbucket.org')
# conf.write(open('example.ini', "w"))
