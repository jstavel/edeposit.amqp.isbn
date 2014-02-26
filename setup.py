from setuptools import setup, find_packages


version = '0.2'
long_description = "\n\n".join([
    open('README.rst').read(),
    open('CONTRIBUTORS.txt').read(),
    open('CHANGES.txt').read()
])


setup(
    name='edeposit.amqp.isbn',
    version=version,
    description="E-Deposit AMQP middleware for ISBN checking",
    long_description=long_description,

    url='https://github.com/jstavel/edeposit.amqp.isbn',

    author='Edeposit team',
    author_email='edeposit@email.cz',

    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    license='GPLv2',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    namespace_packages=[
        'edeposit',
        'edeposit.amqp'
    ],
    include_package_data=True,

    zip_safe=False,
    install_requires=[
        'setuptools',
        'pyisbn',
    ],
    extras_require={
        "test": [
            "unittest2",
            "robotsuite",
        ],
        "docs": [
            "sphinxcontrib-robotdoc",
            "sphinx",
        ]
    },
)
