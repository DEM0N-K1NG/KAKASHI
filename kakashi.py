import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))