# Python Flask app with OpenCV and SciPy on Heroku

This is an application to measure size of objects on input image.

Related sources: [Measuring size of objects in an image with OpenCV](https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/), [Heroku buildpack with Python, OpenCV, Numpy and Scipy](https://github.com/diogojc/heroku-buildpack-python-opencv-scipy)

## Prerequisite
- A free Heroku account
- Ubuntu 16.04
- Python 2.7


## Installation
First, [Install the Heroku Command Line Interface (CLI)](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) and log in using the email address and password you used when creating your Heroku account:
```
heroku login
```

Clone the application into your directory:
```
git clone "https://github.com/DaoDear/heroku-imgproc.git"
cd heroku-imgproc
``` 

Pipenv installed locally by running `pip install pipenv`.

Use Pipenv to create a virtualenv (Python 2.7) and install your dependencies:
```
pipenv --two
pipenv install
```

Then, activate the virtualenv.
```
pipenv shell
```

Create an app on Heroku, which prepares Heroku to receive your source code. Also, set your heroku to use cedar14 to enable required library for image processing:
```
heroku create
heroku stack:set cedar-14 -a <app name>
```
(Note: Heroku generates a random name for your app, or you can pass a parameter to specify your own app name.)

Download heroku buildpack to set up python with opencv from https://github.com/diogojc/heroku-buildpack-python-opencv-scipy by:
```
heroku buildpacks:set https://github.com/diogojc/heroku-buildpack-python-opencv-scipy -a <app name>
```

Then deploy your code:
```
git push heroku master
```

Open your application on heroku: 
```
heroku open
```

If you want to use image processing function, you can put `/view` after your app url.
