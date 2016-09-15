import setuptools

setuptools.setup(
    name="jeffs_fred_implementation",
    version="0.1.0",
    url="https://github.com/drugdata/cookiecutter-pycustomdock",

    author="Jeff Wagner",
    author_email="j5wagner@ucsd.edu",

    description="Jeff's test of CELPPade by implementing a minimal version of Openeye FRED docking",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
     scripts = ['jeffs_fred_implementation/jeffs_fred_implementation.py']
)
