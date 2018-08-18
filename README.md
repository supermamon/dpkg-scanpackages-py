# dpkg-scanpackages.py

A Python implementation of Debian's `dpkg-scanpackages`.

## Requirements

This script requires [python-dpkg](https://github.com/TheClimateCorporation/python-dpkg). Install from [PyPi](https://pypi.python.org/) using the [pip](https://packaging.python.org/installing/) tool:

```
pip install pydpkg
```

## Usage

```
usage: dpkg-scanpackages.py [-h] [-v] [-m] [-a ARCH] [-t TYPE] [-o OUTPUT]
                            binary_path

positional arguments:
  binary_path

optional arguments:
  -h, --help                    show this help message and exit
  -v, --version                 show the version.
  -m, --multiversion            allow multiple versions of a single package.
  -a ARCH, --arch ARCH          architecture to scan for.
  -t TYPE, --type TYPE          scan for <type> packages (default is 'deb').
  -o OUTPUT, --output OUTPUT    Write to file instead of stdout
```

## Caveats

* On Windows™, piping the output to a file results into a file with CRLF endings. File must me converted to unix-style (LF) line endings before using in an apt repo. Or use the `--output` parameter to save the output directly to file.

## Changelog

* v0.4.0
    * `--output` parameter. Write to file instead of stdout.
* v0.3.0
    * `--arch` and `--type` parameter support
* v0.2.0
    * `--multiversion` parameter support 
* v0.1.1
    * variable name correction 
* v0.1.0
    * Base functionality. No switches available besides `--help` and `--version`