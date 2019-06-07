def get_enum_upper(name, field, model):
    from .. import upper
    return f"{upper(model.name)}_{upper(field.get('field_name'))}_{upper(name)}"


def get_enum_dict(field, model):
    from .. import upper
    return f"{upper(model.name)}_{upper(field.get('field_name'))}_DICT"


def get_enum_list(field, model):
    from .. import upper
    return f"{upper(model.name)}_{upper(field.get('field_name'))}_LIST"
