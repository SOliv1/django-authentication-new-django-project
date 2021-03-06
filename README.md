<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome Sara Oliver,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod reminders

`npm install -g heroku`

`pip3 install django`

`django-admin startproject django_auth .`

`django-admin startapp accounts`
go to settings *installed apps* and pop in a string 'accounts`

`python manage.py migrate`

should run -all *ok*

then check with the following:

`python3 manage.py runserver`

quit server with CONTROL -C

`python3 manage.py createsuperuser`
Email address:
Password:
Password again:
Superuser created successfully.

`python3 manage.py runserver`

I had issues and then made aware i am using wrong version of django and reinstall with version 1.11.24` in line with video instructions: 

`pip3 install django==1.11.24`

`pip install --upgrade requirements.txt`

Log into the admin panel:
https://8000-d44dcedd-d3c3-47b5-8998-62a3d7582fef.ws-eu01.gitpod.io/admin/

## Bootstrap

https://getbootstrap.com/
* grab cdn links and add to the head of the base html
* componanents / navbar
* `pip3 install django_forms_bootstrap`
* include this in your settings / installed apps ('django_forms_bootstrap',)
* add {% bootstrap tags %} in the registration html page
* create static folder / inside that create css folder / inside that create styles.css
    and add link in base html and add {% load staticfiles%} above the html tag in base.html
__//__________//
To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

to open bascr file:
`gp open /home/gitpod/.bashrc`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
