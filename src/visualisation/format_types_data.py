from src import default
from concepts import Definition, Context


def format_types_data(tobjects):
    output = {}
    for tobject in tobjects:
        types = tobject[default.FIELD_TYPE].strip('##')
        output[tobject[default.FIELD_NAME]] = types
    return output


def lattice(tobjects):
    definition = Definition()
    for obj, props in format_types_data(tobjects).items():
        definition.add_object(obj, props)
    print(definition)
    Context(*definition).lattice.graphviz(view=True)
