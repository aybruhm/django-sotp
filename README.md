Django SOTP 🔐
================

Generate a secured base32 one time password to authenticate your user!

<br />

## Case Study 📑

Before I mention why you should use django-sotp in your next project, have you every had to build from scratch; every time, a layer of your authentication system?

Ah, yesss - me too, I know the feeling. With django-sotp, you won't have to worry about figuring out how to build that layer of your authentication infrastructure. That's right, this package does everything you'd need, or not.

Django SOTP does just two things, and it does them really well.

- One - it is stupidly secured and simple to integrate
- Two - it clears out OTPs at elapsed time

Damn yes, you saw right! You don't have to worry about making the last reason happen, it's been done for you. All you need to do is figure out how to implement it onto your system. Super cool, yes? I knowwwwww.

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
SOTP_TIME_EXPIRATION = 5 # in minutes
```

Now, you set the email address that you want to use to send emails to your user(s):

```
SOTP_FROM_EMAIL = "from@email.com" # replace the email
```

Yesss. That's all of it? Of course, not! Don't forget to make migrations and migrate to your database and you're good to go!!

```
python manage.py makemigrations && python manage.py migrate
```

Congratulations, buddy! You're all set! Let's jump right into how to start using it.

<br />

## How-To Use 📝

You've got ```django-sotp``` installed and ready to use, here's how to start using it! 

 - Step 1: Import the library to the file you want to use
 ```
 from sotp.services import GenerateSOTP
 ```
 - Step 2: Instantiate the class 
 ```
 otp = GenerateSOTP()
 ```
 - Step 3: Call the `generate_otp` logic (method) directly in the logics or views file, and pass the user's email; since generate_otp requires the user email address to generate the otp code.
 ```
 # Generate otp code for user
 otp.generate_otp(user_email=user.email) 
 ```
 - Step 4: Everything will be handled for you 🤓. A base32 secured token and code has been created, saved and sent to the user! Oh, let's not forget about the scheduler that has been called to remove the user otp and token after the ```SOTP_TIME_EXPIRATION``` has elapsed! 🤝
 - Last Step (maybe?): You can call the function anywhere, anytime. 

If you are still finding it difficult to use this package, kindly check the [example app](https://github.com/israelabraham/django-sotp/tree/main/example) I made for reference, or [create an issue](https://github.com/israelabraham/django-sotp/issues) and state the problem you are experiencing!

<br />

## Shell Example 🥁 

Try to test out this baby on your shell? Let's go then!
 - Step 1: Run the command:
 ```
 python manage.py shell
 ```
 - Step 2: Import the libray directly on the shell:
 ```
 from sotp.services import GenerateSOTP
 ``` 
 - Step 3: Call the generate_otp method, don't forget to add a user email address:
  ```
  otp.generate_otp(user_email="test@email.com")
  ```
 - Step 4: Token and OTP is generated, sent to user via email, and saved to database. 
 ```
 Content-Type: text/plain; charset="utf-8"
 MIME-Version: 1.0
 Content-Transfer-Encoding: 7bit
 Subject: Confirm OTP
 From: noreply@abram.tech
 To: test@email.com
 Date: Tue, 07 Jun 2022 12:04:37 -0000
 Message-ID: <165460347795.27037.15319720132602712964@sonOdin> 

 Use this secured OTP to authenticate your account
 OTP: 957092
 -------------------------------------------------------------------------------
 Scheduler started...
 {'totp': '5ZCLA7UQVXFP2B5WL5OZG4QDFDJ4GL65', 'OTP': '957092'}
 ```