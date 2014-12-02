def ros2Obj(msgInstance):
    obj = {}
    for key in msgInstance.__slots__:
        attr = getattr(msgInstance, key)
        if hasattr(attr, '__slots__'):
            obj[key] = ros2Obj(attr)
        elif key is "data":
            return attr
        else:
            obj[key] = attr
    return obj


def obj2Ros(obj, msgInstance):
    if hasattr(msgInstance, '__slots__'):
        if len(msgInstance.__slots__) is 1 and msgInstance.__slots__[0] is "data":
            if type(obj) is dict:
                raise Exception("Not a primitive")
            msgInstance.data = obj
        else:
            for key in msgInstance.__slots__:
                if key in obj:
                    setattr(msgInstance, key, obj2Ros(obj[key], getattr(msgInstance, key)))
    else:
        if type(obj) is dict:
            raise Exception("Not a primitive")
        msgInstance = obj
    return msgInstance