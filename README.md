# It's like riding a bike

This project is about mice learning to stay on a rotor

# Getting started

## Installing the dependencies
To install Python and the required dependencies we strongly recommend to use
[conda], [mamba] or [pipenv].

## Installing conda

Conda can be installed multiple ways. There is no recommendations about how to
but one can read [there](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
for a likely exhaustive list on ways to install conda.

Note that Anaconda is not necessarily recommended, [miniconda] might be a better
alternative.

Moreover, it is advised to start jupyter notebooks from a shell/terminal/prompt
to be able to better see the error messages.

## Installing the dependencies

Once conda is installed (or your favorite environment manager), you can create
and activate your environment:
```shell
conda create -n bike-riding
conda activate bike-riding
```

Then, there is a `setup.py` file with the basic dependencies present within this
repository. It means that you can easily install all the likely necessary
dependencies using [pip]. It might be necessary to install it first:
```shell
conda install pip
```

Then, it is possible to install the dependencies, from the placozoa-tracking
folder the following way:
```shell
pip install .
```

### List of dependencies:
Here is the list of dependencies that will be installed:
- [numpy] : basic library for array manipulation
- [matplotlib] : basic library to plot figures
- [scikit-learn] : one of the basic libraries for data analysis
- [ipython] : interactive python terminal
- [jupyter] : python notebook
- [napari] : 3D image visualizer
- [pandas] : data array management
- [imageio] : reading movies

# Road Map

# Problems that this software is trying to solve
Mice are learning to walk on a rotor, can we detect the learning phase?

# Objectives
__TODO__

## Objective dependencies
__TODO__

Legend:
- #x &rarr; #y: #x needs to be completed before #y can be started
- #x | #y: #x __or__ #y needs to be completed
- #x & #y: #x __and__ #y needs to be completed

[conda]: https://docs.conda.io/en/latest/
[mamba]: https://mamba.readthedocs.io/en/latest/
[pipenv]: https://pipenv.pypa.io/en/latest/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[placozoa]: https://en.wikipedia.org/wiki/Placozo
[pip]: https://pypi.org/project/pip
[numpy]: https://numpy.org
[scipy]: https://scipy.org
[matplotlib]: https://matplotlib.org
[scikit-image]: https://scikit-image.org
[scikit-learn]: https://scikit-learn.org
[tifffile]: https://pypi.org/project/tifffile
[ipython]: https://ipython.org
[jupyter]: https://jupyter.org
[napari]: https://napari.org
[pandas]: https://pandas.pydata.org
[imageio]: https://imageio.readthedocs.io/en/stable/

<!-- strategies motrices apprises, optimisation

Coordonnee des targets au cours du temps pour 4/5 souris
Reeatribuer les cibles aux bonnes souris

Plusieurs comportements pour rester sur la roue -->