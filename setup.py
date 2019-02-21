from setuptools import setup
from turing_machine_executor import __version__ as version

with open("README.md", "r") as f:
    long_description = f.read()
    f.close()

setup(
    name="turing_machine_executor",
    version=version,
    description="A Turing Machine executor",
    license="MIT",
    long_description=long_description,
    author='Andrea Esposito',
    author_email='andrea.esposito099@gmail.com',
    url="https://github.com/espositoandrea/Turing-Machine-Executor",
    packages=['turing_machine_executor'],
    install_requires=["colorama", "pyfiglet"],
    entry_points={
        'console_scripts': [
            'emt = turing_machine_executor.__main__:run',
            'turing-machine-executor = turing_machine_executor.__main__:run',
        ],
    },
)
