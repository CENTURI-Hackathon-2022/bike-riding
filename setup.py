from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='bike-riding',
    author='Leo Guignard',
    author_email='leo.guignard@univ-amu.fr',
    version='0.0.1',
    description='Bike riding',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CENTURI-Hackathon-2022/bike-riding',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    py_modules = [],
    install_requires=['pandas', 'ffmpeg', 'imageio',
                      'matplotlib', 'numpy', 'scikit-learn',
                      'imageio-ffmpeg', 'ipython', 'jupyter'],
)