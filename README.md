# Django SOTP 🔐

![CI](https://github.com/israelabraham/django-sotp/actions/workflows/django.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/django-sotp.svg)](https://badge.fury.io/py/django-sotp)

Generate a secured base32 one time password to authenticate your user!

## Abstract 📑

Django SOTP does just two things, and does them really well.

- One - it is stupidly secured and simple to integrate
- Two - it clears out OTPs at the elapsed time

## Installation ⏳

Installing django-sotp is very easy, you'll be using (I'd recommend you use a virtual environment, so you don't break your system) the command pip.

Here's how to go about it:

```bash
pip install django-sotp
```

Next is, adding the installed packages to your project:

```python
INSTALLED_APPS = [
    ...
    'sotp',
]
```

Since `django-sotp` depends on a particular package to clear out the OTPs at the elapsed time. We'd have to include another package to our installed apps.

```python
INSTALLED_APPS = [
    ...
    'sotp',
    'django_apscheduler', # added package ;-)
]
```

Now you've done it, all you need to do is add the time which you want the generated OTPs to expire:

```python
SOTP_TIME_EXPIRATION = 5 # in minutes
```

Yesss. Next is to make migrations and migrate to your database and you're good to go!

```python
python manage.py makemigrations && python manage.py migrate
```

Congratulations! You're all set! Let's jump right into how to start using it.

## How-To Use 📝

You've got ```django-sotp``` installed and ready to use, here's how to start using it!

- Step 1: Import the library to the file `(.py)` you want to use:

 ```python
 from sotp.services import GenerateSOTP
 ```

- Step 2: Instantiate the class:

```python
otp = GenerateSOTP()
```

- Step 3: Call the `generate_otp` logic (method) directly in the file, and pass the user's email; since generate_otp requires the user email address to generate the otp code.

```python
# Generates otp code for the user
otp.generate_otp(user_email=user.email) 
```

- Step 4: A base32 secured token and code has been generated, and saved to the secured_otps table. Oh, let's not forget about the scheduler that has been called to remove the user otp and token after the ```SOTP_TIME_EXPIRATION``` has elapsed! 🤝

- Last Step (maybe?): You can call the function anywhere, anytime.

If you are still finding it difficult to use this package, kindly check the [example app](https://github.com/israelabraham/django-sotp/tree/main/example) I made for reference, or [create an issue](https://github.com/israelabraham/django-sotp/issues) and state the problem you are experiencing!

## Shell Example 🥁

If you'd like to test out the package on your django shell..

- Step 1: Run the command:

```python
python manage.py shell
```

- Step 2: Import the libray directly on the shell:

```python
from sotp.services import GenerateSOTP
```

- Step 3: Call the generate_otp method, don't forget to add a user email address:

```python
secured_otp = otp.generate_otp(user_email="test@email.com") # email should exist :-)
```

- Step 4: A Token and OTP is generated, and saved to secured_otps database.

```python
{'totp': '5ZCLA7UQVXFP2B5WL5OZG4QDFDJ4GL65', 'OTP': '957092'}
```
