from src import default


def format_types_data(tobjects):
    unique_types = set()
    output = {}
    for tobject in tobjects:
        types = tobject[default.FIELD_TYPE].strip('##')
        output[tobject[default.FIELD_NAME]] = types
        unique_types.add(types)

    return((output, unique_types))
