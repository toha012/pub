import argparse

def parse_options():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-b', '--bin', help='')
    parser.add_argument('-l', '--lib', help='')
    parser.add_argument('-hoge', '--hoge-hoge', action='store_false', default=True, help='help')
    parser.add_argument('-huga', '--huga-huga', action='store_false', default=True,  help='help')
    parser.add_argument('--config', action='store_true', help='config')
    parser.add_argument('--piyo', help='piyo')
    args = parser.parse_args()
    return args