"""
Setup script for Industrial Safety Monitoring API
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="industrial-safety-api",
    version="1.0.0",
    author="Safety Team",
    author_email="safety@example.com",
    description="Smart Industrial Safety Monitoring API using FastAPI and Computer Vision",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/industrial-safety-api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: FastAPI",
        "Intended Audience :: Manufacturing",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
        "docker": [
            "docker>=6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "industrial-safety-api=main:app",
        ],
    },
)
