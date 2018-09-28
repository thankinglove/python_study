import sys
import os

print(sys.path)
print(sys.argv)

#只执行命令，不保存结果
print(os.system('dir'))
os.popen('dir')