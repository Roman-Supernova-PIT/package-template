{{ cookiecutter.package_name }} Documentation
{{ '-' * (cookiecutter.package_name + " Documentation")|length }}


This is the documentation for {{ cookiecutter.package_name }}.

**Version**: |version|


This package contains the Python software suite developed for use with the Roman Telescope project, as part of the Roman Supernova Project Implementation Team (PIT) project. 


If you have questions or concerns regarding the software, please create an issue in
the github package repository at {{ cookiecutter._project_url + "/" + cookiecutter.package_name }}

--------------------------------

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   installation.rst
   usage.rst
   changes.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
