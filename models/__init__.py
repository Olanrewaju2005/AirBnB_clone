#!/usr/bin/python3

import sys

sys.path.append('models/engine/file_storage.py')

import file_storage

storage = FileStorage()
storage.reload()
