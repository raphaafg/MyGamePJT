from cx_Freeze import setup, Executable
import os

# Read all asset list to include on .exe
path = "./assets"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]
print(asset_list_completa)

# cx_Freeze code
executables = [Executable("main.py")]
files = {"include_files": asset_list_completa, "packages": ["pygame"]}

setup(
    name="RUNAWAYHEAT",
    version="1.0",
    description="Runaway Heat app",
    options={"build_exe": files},
    executables=executables
)
