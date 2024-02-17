import sys
from ctypes import windll # pyright: ignore uknown import
from andria.main import main

if not windll.shell32.IsUserAnAdmin():
    windll.shell32.ShellExecuteW(None, 'runas', sys.executable, __file__, None, 1)
    sys.exit()

main()
