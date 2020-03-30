# Covid-See10 Challenge

This is a resource for people who want to stay active during the coronavirus quarantine in a fun and engaging way. Instagram challenges have been trending (e.g. see ten pushups, do ten pushups), so we made an app where you can see all the challenges, add to the list, and complete them every day.

When completed, you can submit a video or photo as proof. You can also view other people and the challenges they have joined. Eventually, a time limit will be placed on the challenges, allowing only 24 hours to complete it. 

## Getting Started

This is the backend for the app, and it is written in Python/Django. It pairs with the frontend (https://github.com/miriamgrigsby/covidSee10ChallengeFront) which utilizes React Native. You will need to have Python3 installed, and this project uses Pipenv. Fork and clone this repo for use.

### Prerequisites

Once the repo has been forked and cloned, you will need to run
```
pipenv shell
```
to open start the virtual environment. After, run `pipenv install`

```
django
```
```
djangorestframework
```
```
django-cors-headers
```
```
django-rest-knox
```
```
Pillow
```
```
psycopg2
```
```
psycopg2-binary
```
```
django-heroku
```

## Deployment

This backend repo is deployed on Heroku (https://covid-see10.herokuapp.com/). Endpoints are:
* /api/challenges - all REST requests for challenges
* /api/userchallenges - GET all user/challenge associations
* /api/completedchallenges - GET all completed challenge objects that users have created
* /api/userprofiles - GET all profiles

## Authors

* **Alexis Chilinski** - [Website](www.alexischilinski.com) - backend author
* **Miriam Grigsby** - [GitHub](https://github.com/miriamgrigsby) - frontend author

## Acknowledgments

* Miriam and her diligence and dedication to projects