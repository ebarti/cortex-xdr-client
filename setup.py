from setuptools import setup

version = {}
with open("src/cortex/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='cortex-xdr-client',
    version=version['__version__'],
    url='',
    license='MIT',
    author='Eloi Barti',
    author_email='me@eloibarti.com',
    description='API client for Cortex XDR Prevent',
    packages=[
        'cortex',
        'cortex/api',
        'cortex/api/util',
        'cortex/api/models'
    ],
    package_dir={
        '': 'src',
    },
    install_requires=[
        'requests>=2,<3',
    ],
    test_suite='tests',
    extras_require={
        'test': (
            'coverage>=3,<6',
            'pylint>=1,<3',
            'pep8>=1,<2',
            'pyflakes>=1,<3',
        ),
    },
)
