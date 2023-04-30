from slugify import slugify
from sqlalchemy.engine.default import DefaultExecutionContext


def generate_slug_name(context: DefaultExecutionContext):
    params = context.get_current_parameters()
    name = params['name']
    return slugify(name)
