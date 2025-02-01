from setuptools import find_packages, setup

setup(
    name="kestration",
    packages=find_packages(exclude=["kestration_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
