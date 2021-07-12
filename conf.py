import sys
import os
import time

import sphinx_rtd_theme
import time

html_logo = "images/logo.svg"
#html_favicon = "images/favicon.ico"
project = u'THe Settlers II'

source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'html', 'doctrees']

locale_dirs = ['locale/']
gettext_compact = False
language = "en"

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
]

