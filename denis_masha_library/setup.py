from setuptools import setup, find_packages

setup(
    name="denis_masha_library",
    version="0.1",
    description="Functions for hw4",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Maria Simakova",
    author_email="maria.simakova@bse.eu",
    url="https://github.com/mariasimakova/denis_masha_hw4",  
    packages=find_packages(),
    install_requires=[
        "pathlib",
        "pandas",
        "geopy",
        "scikit-learn",
        "matplotlib",
    ],
    python_requires='>=3.12',
)