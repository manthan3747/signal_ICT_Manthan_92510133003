import setuptools

# Try to read README, but don't fail if it doesn't exist
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A Python package for signal generation and operations"

setuptools.setup(
    name="signal-ICT-Manthan-92510133003",
    version="1.0.0",
    author="Manthan",
    author_email="manthan@example.com",
    description="A Python package for signal generation and operations in Signals and Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "matplotlib",
    ],
)