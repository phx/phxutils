import glob
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

binfiles = glob.glob('bin/*')

setuptools.setup(
    name='phxshellutils',
    version='1.1',
    scripts = binfiles,
    author='phx',
    author_email='phx@example.com',
    description='various useful shell utilities',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/phx/shellutils',
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
