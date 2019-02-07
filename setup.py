from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()
    f.close()

setup(
    name="emt",
    version="1.0",
    description="A Turing Machine executor",
    license="GPLv3+",
    long_description=long_description,
    author='Andrea Esposito',
    author_email='andrea.esposito099@gmail.com',
    url="https://github.com/espositoandrea/Turing-Machine-Executor",
    packages=['emt'],
    install_requires=["colorama", "pyfiglet"],
)
