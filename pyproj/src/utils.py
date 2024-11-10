import os
import pathlib
import subprocess

from src.log import error

def normalize_path(path):
    return os.path.abspath(str(pathlib.Path(path).expanduser()))

def exec_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True).stdout
        return res
    except subprocess.CalledProcessError as e:
        error(e)