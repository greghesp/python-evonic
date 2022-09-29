import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyevonic",
    version="0.0.12",
    author="Greg Hesp",
    author_email="greg.hesp+pyevonic@gmail.com",
    description="A wrapper for the Evoflame API v1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greghesp/python-evonic",
    REQUIRED=["aiohttp"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)