#! /usr/bin/env python

import json

def beautify(json_string, sort_keys=True, indent=4):
    ''' Converts the json string int one formated via the options.

        :param json_string: The unformated string.
        :param sort_keys: Whether to sort keys.
        :param indent: The indent. Default 4.
    '''

    j = json.loads(json_string)
    return json.dumps(j, sort_keys=sort_keys, indent=indent)

