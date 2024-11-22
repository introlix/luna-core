from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="luna-core",
    version="0.0.1",
    author="Satyam Mishra",
    author_email="introlixai@gmail.com",
    description="Luna-Core is official API for Luna",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)