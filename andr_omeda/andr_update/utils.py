"""iterating through all request data will not be necessary,
   as the depth of a certain value is already known from
   docs
"""
def id_key_sanitize_for_value(data , telegramIdKey, \
    AndromedaIdKey, key1=None, key2=None, key3=None):
    if key1 and data.get(key1, None):
        if not key2:
            if not data[key1].get(telegramIdKey, None):
                raise Exception("Andr_update utils Error")
            data[key1][AndromedaIdKey] = data[key1][telegramIdKey]
            del data[key1][telegramIdKey]
        elif key2 and not key3:
            if not data[key1].get(key2, None):
                raise Exception("Andr_update utils Error")
            data[key1][key2][AndromedaIdKey] = data[key1][key2][telegramIdKey]
            del data[key1][key2][telegramIdKey]
        else:
            if not data[key1].get(key2, None) and \
                not data[key1].get(key2, None).get(key3, None):
                raise Exception("Andr_update utils Error")
            data[key1][key2][key3][AndromedaIdKey] = data[key1][key2][key3][telegramIdKey]
            del data[key1][key2][key3][telegramIdKey]