import json


def beautify(json_string, sort_keys=True, indent=4):
    ''' Converts the json string int one formatted via the options.

        :param json_string: The unformatted string.
        :param sort_keys: Whether to sort keys. Default True.
        :param indent: The indent. Default 4.
        :returns: A formmated json string.
    '''

    json_object = json.loads(json_string)
    return json.dumps(json_object, sort_keys=sort_keys, indent=indent)
