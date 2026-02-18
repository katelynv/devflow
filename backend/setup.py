from setuptools import setup, find_packages

setup(
  name="devflow",
  packages=find_packages(),
  install_requires=[
    "fastapi",
    "uvicorn",
    "pydantic",
  ],
)