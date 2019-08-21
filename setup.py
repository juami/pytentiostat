from setuptools import setup, find_packages

names = [
]

#entry_points = {
#    "console_scripts": [
#        f"{name}= xpdan.startup.{name}:run_main" for name in names
#    ]
#}

setup(
    name="pytentiostat",
    version='0.0.1',
    packages=find_packages(),
    description="python API for JUAMI potentiostat",
    zip_safe=False,
    package_data={"pytentiostat": ["config/*"]},
    include_package_data=True,
    url="http:/github.com/juami/pytentiostat",
    scripts=["scripts/pytentiostat"],
)
