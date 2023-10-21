import sys
from cx_Freeze import setup, Executable
build_exe_options = {"packages": ["os"], "excludes": []}
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name="clicker",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("clicker.py", base=base, icon='ojirou.ico')]
)