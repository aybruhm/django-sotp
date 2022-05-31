Django SOTP 🔐
================

Generate a secured base32 one time password to authenticate your user!

<br />

## Case Study 📑

Before I tell you one reason why you should use django-sotp in your next project, have you every had to build from scratch every time a layer of your authentication system?

- stupidly secured and simple to integrate
- clears out OTPs at elapsed time

That's right, you don't have to worry about making the last reason asynchronous, it's been done for you. All you need to do is figured out how to implement it onto your system.

<br />

## Installation ⏳

Installing django-sotp is very easy, you'll be using (I'd recommend you use a virtual environment, so you don't break your system) the command pip.

Here's how to go about it:

```
pip install django-sotp
```

Next is, adding the installed packages to your project:

```
INSTALLED_APPS = [
    ...
    'sotp',    
]
```

Now you've done it, all you need to do is add the time which you want your OTPs to expire:

```
SOTP_TIME_EXPIRATION = 15 # in minutes
```

Yesss. That's all of it? Of course, not! Don't forget to make migrations and migrate to your database and you're good to go!!

```
python manage.py makemigrations && python manage.py migrate
```

Congratulations, buddy! You're all set! Let's jump right into how to start using it.

<br />

## How-To Use 📝

<br />

## Shell Example 🥁