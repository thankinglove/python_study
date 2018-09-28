#!/usr/bin/env python

import sys
import os
from subprocess import Popen, PIPE


class Process(object):
    '''memcached rc scripts'''

    def __init__(self, name, program, args, workdir):
        self.name = name
        self.program = program
        self.args = args
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

    def start(self):
        pid = self.__pid
        if pid:
            print("%s is already runing" % self.name)
            sys.exit()
        self.__init()
        cmd = self.program + '' + self.args
        p = Popen(cmd, stdout=PIPE, shell=True)
        self.__pid = p.pid
        self._writePid()
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


def main():
    name = 'memcached'
    program = '/usr/bin/memcached'
    args = ' -u nobody -p 11211 -c 1024 -m 64'
    wd = '/var/tmp/memcached'
    pm = Process(name, program, args, wd)
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
