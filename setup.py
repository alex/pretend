from distutils.core import setup


with open("README.rst") as f:
    readme = f.read()

setup(
    name="pretend",
    description="A library for stubbing in Python",
    long_description=readme,
    author="Alex Gaynor",
    author_email="alex.gaynor@gmail.com",
    packages=["pretend"],
)
