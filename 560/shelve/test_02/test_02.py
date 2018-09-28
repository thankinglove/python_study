import time
import datetime
import hashlib
import shelve

LOGIN_TIME_OUT = 600
db = shelve.open('user_shelve.db', writeback=True)


def newuser():
    global db
    prompt = "login desired: "
    while True:
        name = input(prompt)
        if name in db:
            prompt = "name taken, try another: "
            continue
        elif len(name) == 0:
            prompt = "name should not be empty, try another: "
            continue
        else:
            break
    pwd = input("password: ")
    db[name] = {"password": md5_digest(pwd), "last_login_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
    print(db)


def olduser():
    global db
    name = input("login: ")
    pwd = input("password: ")
    try:
        password = db.get(name).get('password')
    except AttributeError as e:
        print("\033[1;31;40mUsername '%s' doesn't existed\033[0m" % name)
        return
    if md5_digest(pwd) == password:
        login_time = time.mktime(time.localtime())
        # last_login_time = time.mktime(time.strptime(db.get(name).get('last_login_time'), "%Y-%m-%d %H:%M:%S"))
        last_login_time = time.mktime(time.strptime(db.get(name).get('last_login_time'), "%Y-%m-%d %H:%M:%S"))
        print(login_time)
        print(last_login_time)
    else:
        print("inncorrect password")
        return
    if login_time - last_login_time < LOGIN_TIME_OUT:
        print("\033[1;31;40mYou already logged in at: <%s>\033[0m" % datetime.datetime.fromtimestamp(
            last_login_time).isoformat())
        db[name]['last_login_time'] = login_time
        print("\033[1;32;40mwelcome back\033[0m", name)
    else:
        print("\033[1;31;40mlogin incorrect\033[0m")


def md5_digest(plain_pass):
    m = hashlib.md5(plain_pass.encode(encoding='utf-8'))
    ms = m.hexdigest()
    return ms


def showuser():
    global db
    # print(db)
    for name in db.keys():
        print(name, ':', db[name])

def showtime():
    now_time = time.time()
    pass

def showmenu():
    # print '>>>', db
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))
    global db
    prompt = """
 (N)ew User Login
 (E)xisting User Login
 (Q)uit
 (S)how
 Enter choice: """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = "q"
            print("\nYou picked: [%s]" % choice)
            if choice not in "neqs":
                print("invalid option, try again")
            else:
                chosen = True
        if choice == "q": done = True
        if choice == "n": newuser()
        if choice == "e": olduser()
        if choice == "s": showuser()
    db.close()


if __name__ == "__main__":
    showmenu()
