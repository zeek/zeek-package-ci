import configparser
import os

METADATA_FILENAME = 'bro-pkg.meta'
def get_metadata(pkg):
    fn = os.path.join(pkg,  METADATA_FILENAME)
    if not os.path.exists(fn):
        return {}
    parser = configparser.RawConfigParser()
    parser.read(fn)
    metadata = {item[0]: item[1] for item in parser.items('package')}
    return metadata
