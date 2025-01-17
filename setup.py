from setuptools import find_packages, setup

setup(
    name="pytentiostat",
    version="0.0.5",
    packages=find_packages(),
    description="python API for JUAMI potentiostat",
    zip_safe=False,
    package_data={"pytentiostat": ["config/*"]},
    include_package_data=True,
    url="https://github.com/juami/pytentiostat",
    scripts=["scripts/pytentiostat"],
)
