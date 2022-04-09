# skills-garden
## Try it out live [here](https://skills-garden.herokuapp.com/)!

It is proven that efficient learning requires repeating the material. I designed this app to help myself with studying. It features:

### garden
Here you can create **fields** which are simple categories, e.g. Maths, or Physics. You can add **topics**, such as Geometry or Gravity, to each field.
  
### sources
**Sources** can be added to each of your topics in the form of text notes or links.

### schedule
This part takes care of your **reviews**, which are planned according to your fields settings.

### journal
Here you can keep track of your progress by adding **entries**. Some entries will also be added automatically, so you can see what aactions you have taken.
    
    

## Authorization
To test the API you'll have to create an account (through `users/register/` endpoint) and then get your authentication token (through `users/token/`).
Then you can use the API, you just have to provide the access token.

In swagger, just click "Authorize" and type "Bearer " + your access token (there's a space in between).

To refresh the token, go to `users/token/refresh/` and provide refresh token. You will receive access token.

## Technologies used
- Django
- Django REST framework
