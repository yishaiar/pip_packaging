from setuptools import setup, find_packages

# Read the long description from a separate README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="example_package_YOUR_USERNAME_HERE",
    version="0.0.1",
    author="Yishai Arieli",
    author_email="yishai.arieli@mail.huji.ac.il",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Use 'text/x-rst' if you use reStructuredText
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas==2.2.3",
        "numba"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
