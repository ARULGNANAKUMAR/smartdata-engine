from setuptools import setup, find_packages

setup(
    name="althenaxavier",
    version="1.0.0",
    author="Arul Gnanakumar",
    author_email="arulgnanakumar@gmail.com",
    description="Industrial-grade AI-powered big data processing engine",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ARULGNANAKUMAR/smartdata-engine",

    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=open("requirements.txt").read().splitlines(),

    entry_points={
        "console_scripts": [
            "althenaxavier=cli:main",
        ],
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
