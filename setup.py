from distutils.core import setup


with open("README.rst") as f:
    readme = f.read()

setup(
    version="0.6",
    name="pretend",
    description="A library for stubbing in Python",
    long_description=readme,
    author="Alex Gaynor",
    author_email="alex.gaynor@gmail.com",
    py_modules=["pretend"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
    ]
)
