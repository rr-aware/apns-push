from setuptools import setup, find_packages

setup(
    name="apns-push",
    version="0.1.0",
    description="APNs push sender via curl with JWT",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="iSakuragi",
    author_email="smartsakuragi@gmail.com",
    url="https://github.com/rr-aware/apns-push",
    packages=find_packages(),
    install_requires=[
        "PyJWT>=2.0.0,<3.0.0"
    ],
    python_requires=">=3.12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires=">=3.7",
)
