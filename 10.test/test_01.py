#!coding=utf8

import re
import functools

# 1.将字符串中含"."和含"/"的字符去掉
REMOVE_NAME_INVALID_CHARS = functools.partial(re.compile(r'[./]').sub, '')
print REMOVE_NAME_INVALID_CHARS("12[34.56/78]90")

# 2.就是把花括号和花括号里面的字符变为_，这里"^"代表非的意思
# 解释：[]表示分组，[]+表示匹配多次，匹配什么呢，匹配非}的字符多次
PATH_VARIABLE = re.compile(r'{([^}]+)}')
REMOVE_VARIABLES = functools.partial(PATH_VARIABLE.sub, r'_')
print REMOVE_VARIABLES("{(}12{(}34{56+-7}89}0123")

# 3.就是把花括号和花括号里面的字符变为'(?P<\1>[^/]+)'，
CONVERT_PATH_VARIABLES = functools.partial(PATH_VARIABLE.sub, r'(?P<\1>[^/]+)')
print CONVERT_PATH_VARIABLES("{(}12{23423sd}34{(]+}567")

# 4.在匹配的结果两侧加单下划线
SPLIT_CAMEL_BLOCKS = functools.partial(re.compile(r'[A-Z][a-z0-9_$]+').sub, lambda match: '_{}_'.format(match.group(0)))
print SPLIT_CAMEL_BLOCKS("AaBb....Eabcd0+KKwesde23_$SE")
print SPLIT_CAMEL_BLOCKS("AaBb....Eabcd0+KKwesde23_$SE").strip('_').lower()




