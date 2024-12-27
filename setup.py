from setuptools import setup, find_packages

setup(
    name="domainfy",
    version="0.1.1",
    packages=find_packages(exclude=["test"]),
    install_requires=[
        "click",
        "requests",
        "urllib3",
    ],
    entry_points={
        "console_scripts": [
            "domainfy = src.domainfy.__main__:main",
        ],
    },
)
