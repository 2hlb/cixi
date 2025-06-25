from setuptools import setup, find_packages

setup(
    name="cixi",
    version="1.0.0",
    description="💮 豁免川普税的终极方案 - The ultimate solution to exempt Trump tariffs",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/2hlb/cixi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
    keywords=['cixi','trump','tariff','solution'],
)