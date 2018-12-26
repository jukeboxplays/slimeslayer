# -*- coding: utf-8 -*-

import os 
import zlib

def zlib_compress(archive):
	b = os.path.basename(archive)

	with open(b, "rb") as in_file:
		compressed = zlib.compress(in_file.read(), 9)

	with open(b, "wb") as out_file:
		out_file.write(compressed)

def zlib_decompress(archive):
	b = os.path.basename(archive)

	with open(b, "rb") as out_file:
		decompressed = zlib.decompress(out_file.read())

	with open(b, "wb") as dfile:
		dfile.write(decompressed)






