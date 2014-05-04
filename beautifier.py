#! /usr/bin/env python

import json

def beautify(string, sort_keys=True, indent=4):
    j = json.loads(string)
    return json.dumps(j, sort_keys=sort_keys, indent=indent)
