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
Mice are learning to walk on a rotor. Using body part positions over time,
can we quantify their learning?

We have two types of data, manually cleaned datasets and raw datasets

# Objectives
The dataset consists in movies of mice walking on a rotor.
Each movie contains up to five mice that are independent from each other.

The objective of the project would be to classify each mouse time series in three
categories:
- Discovery phase (might be assimilated to the learning phase)
- Learning phase
- "Learnt" phase (when the mouse has a stable behavior)

Moreover, it would be interesting to be able to compare mice against each other
and to classify different learning approaches. Two examples of learning approaches:
- "waiting and jumping"
- "rapid limb movements= stepping"

To reach the final goal, multiple sub-tasks can be identified:
- Organizing the dataset #2
- Extracting simple statistics on the mouse runs (how long it stayed, has it learned, ...)#3
- Quantifying and clustering single mouse behavior over time #4
- Comparing multiple mice behaviors #5
- Classifying the different mouse behaviors according to the type of learning #6
- Is there a preemptive behavior predicting the final learnt behavior? #7

## Objective dependencies
&rarr; #2

#2 &rarr; #3

#2 &rarr; #4

#2 &rarr; #5

(#5 & #4) &rarr; #6

#6 &rarr; #7

Legend:
- #x &rarr; #y: #x needs to be completed before #y can be started
- #x | #y: #x __or__ #y needs to be completed
- #x & #y: #x __and__ #y needs to be completed

[conda]: https://docs.conda.io/en/latest/
[mamba]: https://mamba.readthedocs.io/en/latest/
[pipenv]: https://pipenv.pypa.io/en/latest/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
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
