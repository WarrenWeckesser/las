from setuptools import setup
from os import path


def get_version():
    """
    Find the value assigned to __version__ in las.py.

    This function assumes that there is a line of the form

        __version__ = "version-string"

    in las.py.  It returns the string version-string, or None if such a
    line is not found.
    """
    with open("las.py", "r") as f:
        for line in f:
            s = [w.strip() for w in line.split("=", 1)]
            if len(s) == 2 and s[0] == "__version__":
                return s[1][1:-1]


# Get the long description from README.rst.
_here = path.abspath(path.dirname(__file__))
with open(path.join(_here, 'README.rst')) as f:
    _long_description = f.read()

setup(
    name='las',
    version=get_version(),
    author='Warren Weckesser',
    description=("A reader for Canadian Well Logging Society LAS "
                 "(Log ASCII Standard) files."),
    long_description=_long_description,
    long_description_content_type='text/x-rst',
    url="https://github.com/WarrenWeckesser/las",
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    py_modules=["las"],
    install_requires=[
        'numpy >= 1.5.0',
    ],
    keyword="numpy las reader",
)
