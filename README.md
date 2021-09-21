# skills-garden
REST API for my personal project.

## Try it out live [here](https://skills-garden.herokuapp.com/)!

It is proven that efficient learning requires repeating the material. I designed this app to help myself with studying. It features:

### garden
Here you can create **fields** which are simple categories, e.g. Maths, or Physics. To each field you can add **topics**, such as Geometry or Gravity.
  
### sources
To each of your topics you can add **sources**, which can be either text notes or url links.

### schedule
This part takes care of your **reviews**, which are planned according to your fields settings.

### journal
Here you can keep track of your progress by adding **entries**. Some entries will also be added automatically, so you can see what aactions you have taken.
    
    

## Authorization
To test the API you'll have to create an account (through `users/register/` endpoint) and then get your authentication token (through `users/token/`).
Then you can use the API, you just have to provide the token.

In swagger, just click "Authorize" and type "Token " + your authentication token

## Technologies used
- Django
- Django REST framework
