import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="async-lru-iamsinghrajat", # Replace with your own username
    version="0.0.1",
    author="Rajat Singh",
    author_email="iamsinghrajat@gmail.com",
    description="An asyncio LRU Cache",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamsinghrajat/AsyncioLRU",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)