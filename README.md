# ML Lab Industrial Code

A simple project to experiment with exposing an ML-model as a REST API.

## Case
Determine (classify) a given organization's industrial code based on 'formaal' as given by user.

## Machine learning theory
The task at hand is considered a task of text classification (aka categorization). As such we are going to represent the formaal as a feature vector X. We must consider whether to apply a process of feature selection to speed up the classification.

Once we have chosen a set of features, we can apply any of the supervised learning techniques:
* k-nearest-neighbors,
* support vector machines,
* decision trees,
* naive Bayes, and
* logistic regression.

## Workflow
* Batch train a model on data
* Expose model as API
* Monitor and gather metrics
* Evaluate performance
* Update model

## Solution architecture
TODO
## Solution
The solution is a simple python project that implements a script for training a model as well as a server that exposes the api.
### Project structure
```
-- helloMLAPI
  -- data                 # contains the data
    -- organizations.csv
  -- models               # contains the models trained on the data
    -- xyz.py
    -- xyz.pckl           # a persisted model
  -- api
    -- server.py          # the api
    -- Dockerfile
  -- test
    -- test.py
  README.md
```
### Requirements
* Flask ([Python micro web framework](http://flask.pocoo.org/))
* sklearn ([scikit-learn](http://scikit-learn.org/stable/))
* pickle ([Python object serialization](https://docs.python.org/2.7/library/pickle.html)), or
* joblib ([Scikit learn model persistence](http://scikit-learn.org/stable/modules/model_persistence.html))
### Deploy
To start the server locally:
```
cd api
python server.py
```
### Docker
TODO: Describe how to build and start the api as a dockerized service
## Usage locally
Once the server is running, you can use it with e.g. curl:
```
curl \
  --include \
  --header "Content-Type: application/json"  \
  --request POST \
  --data '{"formaal":"Turer i skog og mark"}' \
  --url http://localhost:5000 \
  --write-out "\n"
```
Response should include a list of industrial codes and descriptions that matches the formaal. The list will be sorted best match first.

## Credits
* http://blog.socratesk.com/blog/2018/01/29/expose-ML-model-as-REST-API
* https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa
* [Russel and Norvig(2010): Artificial Intelligence. A Modern Approach. Third Edition.](http://aima.cs.berkeley.edu/)
