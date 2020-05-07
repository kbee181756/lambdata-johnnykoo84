from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
    name="lambdata-johnnykoo",
    version='0.1.0',
    description="My first python package practice",
    long_description="A project to find git information about authors' commits,most active days and time.",
    long_description_content_type="text/markdown",
    author="Ilmo Koo",
    author_email="johnnykoo84@gmail.com",
    url="https://github.com/johnnykoo84/lambdata-johnnykoo84",
    license="MIT",
    packages=find_packages() # ['my_labmdata']
)
