from mypyc.build import mypycify
from setuptools import setup

setup(
    name="lcs",
    packages=["lcs"],
    ext_modules=mypycify(["lcs/mypyc_.py"])
)
