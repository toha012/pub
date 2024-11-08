import sys
import enum

from src.context import context

class LOG_LEVEL(enum.IntEnum):
    DEBUG   = enum.auto()
    INFO    = enum.auto()
    WARNING = enum.auto()
    ERROR   = enum.auto()

def str_red(s):
    return f'\033[31m{s}\033[0m'

def str_green(s):
    return f'\033[32m{s}\033[0m'

def str_yellow(s):
    return f'\033[33m{s}\033[0m'

def str_blue(s):
    return f'\033[34m{s}\033[0m'

def str_magenta(s):
    return f'\033[35m{s}\033[0m'

def debug(msg):
    if context.log_level <= LOG_LEVEL.DEBUG:
        print('[' + '*' + ']' + msg)

def info(msg):
    if context.log_level <= LOG_LEVEL.INFO:
        print('[' + str_blue('+') + '] ' + msg, flush=True)

def warn(msg):
    if context.log_level <= LOG_LEVEL.WARNING:
        print('[' + str_magenta('!') + '] ' + msg)

def error(msg):
    if context.log_level <= LOG_LEVEL.ERROR:
        sys.exit('[' + str_red('X') + '] ' + msg)