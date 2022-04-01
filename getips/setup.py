from setuptools import setup
# you may need setuptools instead of distutils

setup(
    # basic stuff here
    name='getips',
    version='1.0',
    scripts = ['getips'],
    author='phx',
    author_email='phx@example.com',
    description='list IPs with or without their associated network interfaces',
    url='https://github.com/phx/shell_utils/tree/master/getips',
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Linux",
    ],
)
