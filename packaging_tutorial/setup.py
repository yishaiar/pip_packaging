from setuptools import setup, find_packages

setup(
    name="example_package_YOUR_USERNAME_HERE",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,  # Make sure this is True
    install_requires=[
        # Your dependencies here
    ],
    test_suite="tests",
)
