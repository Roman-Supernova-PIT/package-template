{%- if cookiecutter.include_example_code == 'y' %}
from .example_mod import do_primes
{% endif %}

{% if cookiecutter.enable_dynamic_dev_versions == 'y' %}
from ._version import __version__
{% else%}
from .version import version as __version__
{% endif %}

{% if cookiecutter.include_example_code == 'y' -%}
# Then you can be explicit to control what ends up in the namespace,
__all__ = ['do_primes']
{% else -%}
__all__ = []
{% endif -%}