from setuptools import setup, find_packages
import os

# Load the long description from your README.md file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="motion_code",
    version="0.1.0",
    description="Forecasting radio‐movement models for TSM simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    url="https://github.com/yourusername/motion_code",
    packages=find_packages(include=["motion_code", "motion_code.*"]),
    python_requires=">=3.8",
    install_requires=[
        "jax",
        "matplotlib",
        "numpy",
        "pandas",
        "scikit-learn",
        "scipy",
        "sktime",
        "tqdm",
        "einops",
        "local-attention",
        "patool",
        "reformer-pytorch",
        "sympy",
        "torch",
        "PyWavelets"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)