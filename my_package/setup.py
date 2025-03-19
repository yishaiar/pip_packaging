
# # Setup script to install the package

# from setuptools import setup, find_packages

# setup(
#     name="my_package",  # Name of the package
#     version="0.1",      # Initial version
#     packages=find_packages(where="pip_package"),  # Look for packages under the pip_package directory
#     package_dir={"": "pip_package"},  # Specifies the location of the root package
#     install_requires=[],  # List dependencies here (if any)
#     author="Your Name",
#     author_email="your.email@example.com",
#     description="A simple example package with a function and a class",
#     long_description=open("README.md").read(),  # Optional: Long description from a readme file
#     long_description_content_type="text/markdown",
#     url="https://github.com/yourusername/my_package",  # If you have a repo
#     classifiers=[  # Some classifiers for the package
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
# )



# Setup script to install the package

from setuptools import setup, find_packages

setup(
    name="my_package",  # Name of the package
    version="0.1",      # Initial version
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[],  # List dependencies here (if any)
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example package with a function and a class",
    long_description=open("README.md").read(),  # Optional: Long description from a readme file
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",  # If you have a repo
    classifiers=[  # Some classifiers for the package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
