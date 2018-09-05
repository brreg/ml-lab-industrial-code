# helloMLAPI

A simple project to experiment with exposing an ML-model as a REST API.

## Case
Determine (classify) a given organization's industrial code based on 'formaal' as given by user.

## Workflow
* Batch train a model on data
* Expose model as API
* Monitor and gather metrics
* Evaluate performance
* Update model

## Solution architecture

## Solution

### Project structure
```
-- helloMLAPI
  -- api
    -- data                 # contains the data
      -- organizations.csv
    -- models               # contains the model trained on the data
      -- xyz.py
      -- xyz.pckl           # the persisted model
  -- server.py               # the api
  -- Dockerfile
  -- test
    -- test.py
  README.md
```
### Requirements
* Flask ([Python micro web framework](http://flask.pocoo.org/))
* pickle ([Python object serialization](https://docs.python.org/2.7/library/pickle.html))
* sklearn ([scikit-learn](http://scikit-learn.org/stable/))
### Deploy

### Docker

## Usage locally
With curl:
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
