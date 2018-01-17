#Python Flask app with OpenCV and SciPy on Heroku

This is an application to measure size of objects on input image.

Related sources:
- [Measuring size of objects in an image with OpenCV](https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/)
- [Heroku buildpack with Python, OpenCV, Numpy and Scipy](https://github.com/diogojc/heroku-buildpack-python-opencv-scipy)

##Prerequisite
- A free Heroku account.
- Python 2.7


##Installation
1. [Install the Heroku Command Line Interface (CLI)](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
2. Log in using the email address and password you used when creating your Heroku account:
   ```
   heroku login
   ```
3. Clone the application into your directory:
   ```
   git clone "https://daodear@bitbucket.org/muictsenior/heroku-imgproc.git"
   cd heroku-imgproc
   ``` 
3. Pipenv installed locally by running `pip install pipenv`.
4. Use Pipenv to create a virtualenv (Python 2.7) and install your dependencies:
   ```
   pipenv --two
   pipenv install
   ```
5. Then, activate the virtualenv.
   ```
   pipenv shell
   ```
6. Create an app on Heroku, which prepares Heroku to receive your source code:
   ```
   heroku create
   ```
   Heroku generates a random name for your app, or you can pass a parameter to specify your own app name.
7. Download heroku buildpack to set up python with opencv from https://github.com/diogojc/heroku-buildpack-python-opencv-scipy by:
   ```
   heroku buildpacks:set https://github.com/diogojc/heroku-buildpack-python-opencv-scipy -a <myapp>
   ```
8. Then deploy your code:
   ```
   git push heroku master
   ```
9. Open your application on heroku: `heroku open`
