import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coffeece",
    version="0.1.1",
    author="FARBEX97",
    author_email="fernandoarbexcv@gmail.com",
    description="Python useful classes for office work automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FARBEX97/coffeece",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)