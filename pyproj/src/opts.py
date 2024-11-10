import argparse

def parse_options():
    parser = argparse.ArgumentParser(description='')
    
    parser.add_argument('-d', '--debug', action='store_true', default=False,  help='Debug (--log-level 1)')
    parser.add_argument('-L', '--log-level', default=None, help='Log level (default: 2 INFO)')

    parser.add_argument('-b', '--bin', help='')
    parser.add_argument('-l', '--lib', help='')
    parser.add_argument('-nohoge', '--no-hoge', action='store_true', default=False, help='Disable hoge')
    parser.add_argument('-huga', '--huga-huga', action='store_false', default=True,  help='help')
    parser.add_argument('--config', action='store_true', help='config')
    parser.add_argument('--piyo', help='piyo')
    parser.add_argument('-p', '--set-popo', default=None,  help='popo help')

    args = parser.parse_args()
    return args