from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in singlecoreapps_app/__init__.py
from singlecoreapps_app import __version__ as version

setup(
	name="singlecoreapps_app",
	version=version,
	description="aplikasi buat PKL di Bea dan Cukai",
	author="Firman",
	author_email="firmanhartono305@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
