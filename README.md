<p align="center">
  <img src="http://adlr.org/wp-content/uploads/2014/07/logo_ucm.png"
  height="200"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="http://informatica.ucm.es/data/cont/media/www/pag-78821/escudofdigrande.png"
  height="200"/>
  </p>

# Application of Machine Learning Algorithms for Bipolar Disorder Crisis Prediction
This is the project for my bachelor's thesis. The goal of this project is to apply different Machine Learning algorithms to patient data in order to create a prediction model that in the future will give psychiatrists a second opinion on whether their patients might be tending towards a depression or mania episode, or if they are staying in a normal state.

This project consists in:
  * A notebook made with *Jupyter Notebook* that contains the whole process of data cleaning and visualization as well as the application of different Machine Learning algorithms to predict the state of the patient.
  * A python script that uses one of the classifiers dumped from the notebook and gives a prediction of the possible state a patient could be tending towards given the input of the doctor.

## Motivations

This project springs from the [Bip4cast](https://bip4cast.org/) project, which studies the appearance of crisis in patients with Bipolar Disorder in order to predict them. The goal of the Bip4cast project is to be able to react in time and avoid the symptoms before the patients start to suffer from them.

## License
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Used technologies/frameworks

The following technologies and frameworks are used on the project:
- [Python](https://www.python.org/)
- [Jupyter Notebook](http://jupyter.org/)

## Code example

The following code snippet shows the application of a *Random Forest* algorithm to create a classifier:

```
X_train, X_test, y_train, y_test = train_test_split(
      interviews_episodes.loc[:, interviews_episodes.columns != "episode"], 
      interviews_episodes["episode"], test_size=0.3
)
                                              
clf = RandomForestClassifier(n_jobs=-1)
clf.fit(X_train, y_train)
scores = cross_val_score(clf, X_test, y_test)
print "Model accuracy: ", scores.mean()
```

## Prerequisites

If you are running Linux on your computer you can install and configure *pip* for an easier installation of the libraries:

```sh
$ sudo apt-get install python-pip python-dev build-essential
$ sudo pip install --upgrade pip
```

### Notebook

In order to run the *Jupyter Notebook* notebook you need to have python 2.7 installed on your computer and install *Jupyter Notebook*, which you can do with *pip*:
```sh
$ pip install jupyter
```

The required python libraries are:
* pandas
* numpy
* seaborn
* matplotlib
* IPython
* pydotplus
* cPickle

In order to install them, run:
```sh
$ pip install pandas
$ pip install numpy
$ pip install seaborn
$ pip install matplotlib
$ pip install IPython
$ pip install pydotplus
$ pip install cPickle
```

For the notebook to work, the data that you import needs to have the same format as the files in the data folder.

### Python script

In order to run the python script you need to have python 2.7 installed on your computer. The required python libraries are:
* numpy
* sklearn
* termcolor

In order to install them you can 
```sh
$ pip install numpy
$ pip install sklearn
$ pip install termcolor
```

## Execution

To execute the Bipolar Disorder Crisis Prediction python script just run:
```sh
$ python state_prediction.py
```
