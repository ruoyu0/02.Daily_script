#!coding=utf8

import re
import functools

REMOVE_NAME_INVALID_CHARS = functools.partial(re.compile(r'[./]').sub, '')
PATH_VARIABLE = re.compile(r'{([^}]+)}')
REMOVE_VARIABLES = functools.partial(PATH_VARIABLE.sub, r'_')
CONVERT_PATH_VARIABLES = functools.partial(PATH_VARIABLE.sub, r'(?P<\1>[^/]+)')
SPLIT_CAMEL_BLOCKS = functools.partial(re.compile(r'[A-Z][a-z0-9_$]+').sub, lambda match: '_{}_'.format(match.group(0)))

print "y1"
print REMOVE_NAME_INVALID_CHARS("12[34.56/78]90")

if __name__ == '__main__':
    print "ss"