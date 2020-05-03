#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib

m = hashlib.md5()
m.update('hy123456'.encode(encoding='utf-8'))
result = m.hexdigest()
print(result)
