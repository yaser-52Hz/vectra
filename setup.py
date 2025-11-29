from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, find_packages
import pybind11
import platform

ext_modules = [
    Pybind11Extension(
        "vectors._vectors_core",
        [
            "src/vectors_cpp/vector_core.cpp",
            "src/vectors_cpp/python_bindings.cpp",
        ],
        include_dirs=[
            "src/vectors_cpp",
        ],
        language="c++",
    ),
]

# Compiler-specific flags
if platform.system() == "Windows":
    extra_compile_args = ["/W4", "/std:c++17"]
else:
    extra_compile_args = ["-std=c++17", "-O3", "-march=native"]

for ext in ext_modules:
    ext.extra_compile_args.extend(extra_compile_args)


setup(
    name="vectra",
    version="0.1.0",
    author="Yasser Hosseinzadeh",
    author_email="one.astro.nerd@gmail.com",
    description="Vectra - High-performance n-dimensional vector operations for scientific computing",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        "pybind11>=2.10.0",
        "numpy>=1.20.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    url="https://github.com/yasser-hosseinzadeh/vectra",
    project_urls={
        "Documentation": "https://github.com/yasser-hosseinzadeh/vectra",
        "Source": "https://github.com/yasser-hosseinzadeh/vectra",
    },
)

