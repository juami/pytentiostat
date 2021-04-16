from setuptools import setup, find_packages
import subprocess
import webbrowser
import os

subprocess.call([r'scripts\deploy_docs.bat'])

cwd = os.getcwd()
url = 'file:///' + cwd + '/docs/_build/html/index.html'
webbrowser.open(url, new=2)  # open in new tab

setup(
    name="pytentiostat",
    version='0.0.5',
    packages=find_packages(),
    description="python API for JUAMI potentiostat",
    zip_safe=False,
    package_data={"pytentiostat": ["config/*"]},
    include_package_data=True,
    url="http:/github.com/juami/pytentiostat",
    scripts=["scripts/pytentiostat"],
)
