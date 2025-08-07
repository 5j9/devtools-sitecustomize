__version__ = '0.1.10.dev1'

import builtins

from devtools import debug


def add_debug_to_builtins():
    setattr(builtins, 'debug', debug)
