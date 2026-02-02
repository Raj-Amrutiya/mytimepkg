from setuptools import setup, find_packages

setup(
    name="mytimepkg-raj",
    version="1.0.0",
    author="Raj Amrutiya",
    author_email="your-email@gmail.com",
    description="Simple Python time utility package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7",
)
