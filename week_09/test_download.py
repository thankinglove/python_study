# -*- encoding: Utf-8 -*-
import os
import time
import paramiko


class Download_gitlab_backup:
    def __init__(self):
        self.hostname = '101.132.238.148'
        self.hostport = 22
        self.username = 'root'
        self.userpassword = 'qDtr55T3x5k'
        self.localpath = "D:/Handeson_Gitlab_Backup/"
        self.remotepath = '/srv/gitlab/data/backups/'
        self.command = self.RemoteSSH("ls -lt /srv/gitlab/data/backups |awk 'NR==2'|awk '{print $9}'")
        self.date = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

    def RemoteSSH(self, cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname=self.hostname, port=self.hostport, username=self.username, password=self.userpassword)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        ssh.close()
        return result.strip()


    def RemoteScp(self, src, des):
        scp = paramiko.Transport(self.hostname, self.hostport)
        scp.connect(username=self.username, password=self.userpassword)
        sftp = paramiko.SFTPClient.from_transport(scp)
        sftp.get(src, des)
        scp.close()


    def Download(self):
        # data = Download_gitlab_backup()
        remotefilepath = self.remotepath + self.command
        localfilepath = self.localpath + self.command
        self.RemoteScp(remotefilepath, localfilepath)


if __name__ == "__main__":
    result = Download_gitlab_backup()
    result.Download()
