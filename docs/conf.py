project = "onap"
release = "master"
version = "master"

#####
# Deprecation of Sphinx context injection at build time
# see https://about.readthedocs.com/blog/2024/07/addons-by-default/
import os

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True
#
#####

author = "Open Network Automation Platform"
# yamllint disable-line rule:line-length
copyright = "ONAP. Licensed under Creative Commons Attribution 4.0 International License"

exclude_patterns = [
    '.tox'
]

pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "style_nav_header_background": "white",
    "sticky_navigation": "False" }
html_logo = "_static/logo_onap_2024.png"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_show_sphinx = False

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.spelling' ,
    'sphinxcontrib.openapi',
]

#
# Map to 'latest' if this file is used in 'latest' (master) 'doc' branch.
# Change to {releasename} after you have created the new 'doc' branch.
#

branch = 'latest'

intersphinx_mapping = {}
doc_url = 'https://docs.onap.org/projects'
master_doc = 'index'

exclude_patterns = [
    '.tox'
]

spelling_word_list_filename='spelling_wordlist.txt'
spelling_lang = "en_GB"

#
# Example:
# intersphinx_mapping['onap-aai-aai-common'] = ('{}/onap-aai-aai-common/en/%s'.format(doc_url) % branch, None)
#

html_last_updated_fmt = '%d-%b-%y %H:%M'

def setup(app):
    app.add_css_file("css/ribbon.css")

linkcheck_ignore = [
  r'https://git\.onap\.org/doc/plain/etc/upper-constraints\.onap\.txt',
  r'https://git\.onap\.org/.*',
  r'http://localhost:\d+/',
  r'.*'  # ignores everything!
]
