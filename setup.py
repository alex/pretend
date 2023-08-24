from setuptools import setup


with open("README.rst") as f:
    readme = f.read()

setup(
    version="1.0.9",
    name="pretend",
    description="A library for stubbing in Python",
    long_description=readme,
    author="Alex Gaynor",
    author_email="alex.gaynor@gmail.com",
    py_modules=["pretend"],
    url="https://github.com/alex/pretend",
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
