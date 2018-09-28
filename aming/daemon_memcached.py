#!/usr/bin/env python

import sys
import os
from subprocess import Popen, PIPE


class Process(object):
    args = {'USER': 'memcached',
            'PORT': 11211,
            'MAXCONN': 1024,
            'CACHESIZE': 64,
            'OPTIONS': ''}

    def __init__(self, name, program, workdir):
        self.name = name
        self.program = program
        self.workdir = workdir
        self.__pid = ''
        self.__init()

    def __init(self):
        if not os.path.exists(self.workdir):
            os.mkdir(self.workdir)
            os.chdir(self.workdir)

    def _pidFile(self):
        return os.path.join(self.workdir, "%s.pid" % self.name)

    def _writePid(self):
        if self.__pid:
            with open(self._pidFile(), 'w+') as fd:
                fd.write(str(self.__pid))

    def __readConf(self, f):
        with open(f) as fd:
            lines = fd.readlines()
            return dict([ i.strip().replace('"', '').split('=') for i in lines ])

    def __parseArgs(self):
        conf = self.__readConf('/etc/sysconfig/memcached')
        if 'USER' in conf:
            self.args['USER'] = conf['USER']
        if 'PORT' in conf:
            self.args['PORT'] = conf['PORT']
        if 'MAXCONN' in conf:
            self.args['MAXCONN'] = conf['MAXCONN']
        if 'CACHESIZE' in conf:
            self.args['CACHESIZE'] = conf['CACHESIZE']
        options = ['-u', self.args['USER'],
                   '-p', self.args['PORT'],
                   '-m', self.args['MAXCONN'],
                   '-c', self.args['CACHESIZE']]
        os.system("chown -R %s %s" % (self.args['USER'], self.workdir))
        return options

    def start(self):
        pid = self.__pid
        if pid:
            print("%s is already runing" % self.name)
            sys.exit()
        self.__init()
        cmd = [self.program] + self.__parseArgs() + ['-d', '-P', self._pidFile()]
        print(cmd)
        p = Popen(cmd, stdout=PIPE)
        # self.__pid = p.pid
        # self._writePid()
        print("%s start Sucessful" % self.name)

    def __getPid(self):
        p = Popen(['pidof', self.name], stdout=PIPE)
        pid = p.stdout.read().strip()
        return pid

    def stop(self):
        pid = self.__getPid()
        if pid:
            os.kill(int(pid), 15)
            if os.path.exists(self._pidFile()):
                os.remove(self._pidFile())
            print("%s is stopped" % self.name)

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        pid = self.__getPid()
        if pid:
            print("%s is already runing" % self.name)
        else:
            print("%s is not runing" % self.name)

    def help(self):
        print("Usage: %s {start|stop|status|restart}" % __file__)
        return None


def main():
    name = 'memcached'
    program = '/usr/bin/memcached'
    wd = '/var/tmp/memcached'
    pm = Process(name, program, wd)
    try:
        cmd = sys.argv[1]
    except IndexError:
        print("Optinon Error")
        sys.exit()
    if cmd == 'start':
        pm.start()
    elif cmd == 'stop':
        pm.stop()
    elif cmd == 'restart':
        pm.restart()
    elif cmd == 'status':
        pm.status()
    else:
        pm.help()


if __name__ == '__main__':
    main()
