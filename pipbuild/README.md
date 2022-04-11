# pipbuild

Requirements:

- `/bin/sh`
- python3
- python3 build module
- python3 twine module

`pipbuild` is a script for auto-incrementing the build number in the current directory's `setup.py` version information, building the package, and uploading to PyPi.

It will prompt for PyPi username/token and password, but the following environment variables are also recognized for quickness/automation:

- `$PYPI_USER`
- `$PYPI_PASS`

## Caveats

`pipbuild` expects a version number in `x.x.x` format, with the last `x` representing the build number.

For the sake of keeping the script simple, if you wish to change the major/minor version numbers, just edit `setup.py` manually, and run `pipbuild -m` or `pipbuild --manual`
which will prevent the auto-incrementing of the build number before building and uploading to PyPi.

