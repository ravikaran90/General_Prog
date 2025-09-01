import sys
import os

class Solution:
    def sys_os(self):
        print("Current Working Directory:",os.getcwd())
        print("Process ID of the current process:",os.getpid())
        print("Name of the Process:",os.name)
        print("Platform:",sys.platform)

def main():
    obj=Solution()
    obj.sys_os()

if __name__=="__main__":
    main()