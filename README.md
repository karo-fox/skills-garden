# skills-garden
REST API for my personal project.

## Try it out live [here](https://skills-garden.herokuapp.com/)!

It is proven that efficient learning requires repeating the material. I designed this app to help myself with studying. It features:
- garden: the place when you can store topics, categorized in fields
- sources: to each topic you can add text source or an url link
- schedule: the app will keep track of what you've learned & plan revisions for your topics
- journal: here you can write and describe your learning process. It also logs actions taken by the system

## Authorization
To test the API you'll have to create an account (through `users/register/` endpoint) and then get your authentication token (through `users/token/`).
Then you can use the API, you just have to provide the token.

In swagger, just click "Authorize" and type "Token " + your authentication token

## Technologies used
- Django
- Django REST framework
