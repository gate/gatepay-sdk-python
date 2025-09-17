
from setuptools import setup, find_packages

setup(
    name="gatepay-sdk-python",
    version="0.1.0",
    description="GatePay SDK for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # 列出项目依赖，例如:
        # "requests>=2.25.0",
        "pytest==7.2.0",
        "pydantic==1.9.1",
        "camel-converter==3.0.0",
        "httpx==0.24.1"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)