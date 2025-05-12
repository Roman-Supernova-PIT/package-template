from importlib.metadata import version, PackageNotFoundError
{%- if cookiecutter.include_example_code == 'y' %}
from .example_mod import do_primes
__all__ = ['do_primes']
{%- else %}
__all__ = []
{% endif %}


try:
    __version__ = version("{{ cookiecutter.module_name }}")
except PackageNotFoundError:
    # package is not installed
    pass
