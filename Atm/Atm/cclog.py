#!/usr/bin/env python


def savePay(content):
    with open("../logs/pay.txt", 'w+') as fd:
        fd.write(content)


def saveRepay(content):
    with open("../logs/repay.txt", 'w+') as fd:
        fd.write(content)


def saveRegister(content):
    with open("../logs/register.txt", 'w+') as fd:
        fd.write(content)


def savePassword(content):
    with open("../logs/password.txt", 'w+') as fd:
        fd.write(content)
