from src.context import context
from src.log_level import LOG_LEVEL
from src.log import debug, info, warn, error
from src.opts import parse_options

def main():
    args = parse_options()

    if args.log_level:
        log_level = int(args.log_level)
        lb_log_level = min(LOG_LEVEL)
        ub_log_level = max(LOG_LEVEL)
        if log_level < lb_log_level or log_level > ub_log_level:
            error(f'Invalid log level ({lb_log_level} <= log level <= {ub_log_level})')
        context.log_level = LOG_LEVEL(log_level)
    elif args.debug:
        context.log_level = LOG_LEVEL.DEBUG

    debug('debug msg')
    info('info msg')
    warn('warn msg')
    error('error msg')