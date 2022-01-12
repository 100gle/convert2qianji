import pathlib
from setuptools import setup, find_packages

ROOT = pathlib.Path(__file__).parent
requires = (ROOT / "requirements.txt").read_text().splitlines()

setup(
    name="qianji",
    version="0.1",
    author="100gle",
    url="https://github.com/100gle/convert2qianji",
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        "console_scripts": [
            'qianji-cli=qianji.main:cli'
        ]
    }
)
