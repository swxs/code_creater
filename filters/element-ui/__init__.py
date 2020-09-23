def get_enum_upper(name, field, klass):
    from .. import upper

    return f"{upper(klass.name)}_{upper(field.name)}_{upper(name)}"


def get_enum_dict(field, klass):
    from .. import upper

    return f"{upper(klass.name)}_{upper(field.name)}_DICT"


def get_enum_list(field, klass):
    from .. import upper

    return f"{upper(klass.name)}_{upper(field.name)}_LIST"
