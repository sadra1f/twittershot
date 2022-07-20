import sys
import shutil
import PyInstaller.__main__
from distutils.dir_util import copy_tree

if __name__ == "__main__":
    args = sys.argv
    PyInstaller.__main__.run(
        [
            "--onefile",
            "--windowed",
            "--add-data",
            r"res;res/",
            args[1],
        ]
    )

    try:
        copy_tree("bin/", "dist/bin/")
    except:
        print("bin/ not found")
    copy_tree("templates/", "dist/templates/")
    shutil.copy("config.sample.json", "dist/")
