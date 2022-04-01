import glob
from setuptools import setup
# you may need setuptools instead of distutils

binfiles = glob.glob('bin/*')

setup(
    # basic stuff here
    name='shellutils',
    version='1.1',
    scripts = binfiles,
    author='phx',
    author_email='phx@example.com',
    description='various useful shell utilities',
    url='https://github.com/phx/shell_utils',
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Linux",
    ],
)
