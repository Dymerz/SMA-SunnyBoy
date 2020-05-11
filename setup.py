import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SMA-SunnyBoy", # Replace with your own username
    version="0.0.5",
    author="Urbain Corentin",
    author_email="corentin.urbain96@gmail.com",
    description="A simple data retrieving for SMA SunnyBoy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dymerz/SMA-SunnyBoy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
	test_suite='nose.collector',
    tests_require=['nose'],
)
