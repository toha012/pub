import sys

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

def error(msg):
    sys.exit('[' + str_red('X') + '] ' + msg)

def warn(msg):
    print('[' + str_magenta('!') + '] ' + str_magenta(msg))

def log(msg):
    print('[' + str_blue('*') + '] ' + msg, flush=True)