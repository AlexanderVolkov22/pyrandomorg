import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["requests<=2.21.0", "aiohttp<=3.7.3"]

setuptools.setup(
    name="pyrandomorg",
    version="0.0.1",
    author="AlexanderVolkov22",
    author_email="alexanderedit22@gmail.com",
    description="Simple Async Library For Random.org API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexanderVolkov22/pyrandomorg",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
