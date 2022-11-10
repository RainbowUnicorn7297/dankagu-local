import os

# Change this to where the data directory of raw assets is located on your PC
_asset_dir = '../assets/tdk_adl_final/raw/unique_raw/data'

def asset(path):
    global _asset_dir
    data = b''
    with open(os.path.join(_asset_dir, path), 'rb') as f:
        data = f.read()
    return data
