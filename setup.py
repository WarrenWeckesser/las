from setuptools import setup


setup(
    name='las',
    version='0.0.1',
    author='Warren Weckesser',
    description=("A reader for Canadian Well Logging Society LAS "
                 "(Log ASCII Standard) files."),
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    py_modules=["las"],
    install_requires=[
        'numpy >= 1.5.0',
    ],
)
