from distutils.core import setup, Extension
from distutils import sysconfig

with open("README.md", "r") as f:
    long_description = f.read()

cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

sfc_module = Extension(
    'potentials', sources = ['./hydrogels/theory/models/_cxx/potentials.cpp'],
    include_dirs=['pybind11/include', './hydrogels/theory/models/_cxx/'],
    language='c++',
    extra_compile_args = cpp_args,
    )

setup(
    name="hydrogels",
    version="0.0.2",
    author="Debesh Mandal",
    description="Package for creating and analysing hydrogels in ReaDDy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debeshmandal/hydrogels",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
