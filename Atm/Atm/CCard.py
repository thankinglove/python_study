#!/usr/bin/env python
import cclog


class CCard:
    def __init__(self, idNum, total):
        self.idNum = idNum
        self.password = "123456"
        self.total = total
        self.remain = total
        self.status = 0

    def getId(self):
        return self.idNum

    def setpassword(self, old_password, new_password_1, new_password_2):
        if old_password == self.password:
            if new_password_1 == new_password_2:
                self.password = new_password_1
                cclog.savePassword("%s: 修改密码成功" % self.idNum)
                print("密码修改成功")
                return True
            else:
                cclog.savePassword("%s: 修改密码失败, 新密码不一致" % self.idNum)
                print("新密码不一致")
                return False
        else:
            print("旧密码错误")
            cclog.savePassword("%s: 修改密码失败, 旧密码错误" % self.idNum)
            return False

    def getCash(self, money):
        self.remain = float(self.total - money * 1.05)
        if self.remain < 0:
            cclog.savePay("%s: 金额不足, 提现失败，" % self.idNum)
            print("金额不足，提现失败")
            return False
        else:
            cclog.savePay("%s: 提现成功，提现金额：%d" % (self.idNum, money))
            print("提现成功，提现金额：%d" % money)
            return True

    def pay(self, money):
        account = self.remain - money
        if account >= 0:
            self.remain = account
            cclog.savePay("%s: 支付成功，支付金额： %d" % (self.idNum, money))
            print("支付成功，支付金额： %d" % money)
            return True
        else:
            cclog.savePay("%s: 支付失败，金额不足" % self.idNum)
            print("支付失败，金额不足")
            return False

    def getRepay(self) -> object:
        return float(self.total - self.remain)

    def repay(self, money):
        account = self.getRepay()
        if money < account:
            cclog.saverePay("%s: 偿还金额不足" % self.idNum)
            print("偿还金额不足,您需要偿还：%f" % account)
            return False
        elif money > account:
            cclog.saverePay("%s: 您需要偿还：%f" % (self.idNum, account))
            print("您需要偿还：%f" % account)
            return False
        else:
            cclog.saverePay("%s: 偿还成功, 偿还金额：%f" % (self.idNum, account))
            print("偿还成功")
            return True

    # def transfer(self, ccid, money):
    #     isinstance(ccid, CCard)
    #     pass
