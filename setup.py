import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json-beautifier",
    version="0.0.1",
    description="A simple json formatter.",
    author="Greg Peterson",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pyside2'],
    python_requires='>=3',
    entry_points={
        'gui_scripts': [
            'json_beautifier = json_beautifier.main:main',
        ],
    },
)
