# Getting Started
## Prerequisites
- Python 3.11+
- Poetry [Installation Guide](https://python-poetry.org/docs/master/#installing-with-the-official-installer)


## Setup
```shell
git clone https://github.com/ebarti/cortex-xdr-client.git
cd cortex-xdr-client
poetry install
```


## Running Tests
Run the following:
```shell
poetry run python -m pytest tests/
```
The offline compatibility suite covers XDR 3.x and 5.x. CI runs on Python 3.11,
3.12, 3.13 and 3.14. If Poetry is unavailable, use a virtual environment:

```shell
python -m pip install -e . 'pytest>=9.1.1,<10' 'requests-mock>=1.9,<2' 'pytest-mock>=3.10,<4'
python -m pytest tests/
```

See [the API compatibility audit](docs/API_COMPATIBILITY.md) for specification
sources, snapshot provenance and known documentation inconsistencies. Tests
must register literal vendor paths instead of deriving their expected URLs from
`_get_url`, so a routing regression cannot make both sides of a test pass.
