import os

# Change this to where the assets directory is located on your PC
_asset_dir = 'assets'


def asset(path):
    global _asset_dir
    data = b''
    with open(os.path.join(_asset_dir, path), 'rb') as f:
        data = f.read()
    return data

