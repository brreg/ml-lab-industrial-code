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

### Requirements
* Flask
*
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
Response should include a list of industrial codes that matches the formaal.

## Credits
* http://blog.socratesk.com/blog/2018/01/29/expose-ML-model-as-REST-API
