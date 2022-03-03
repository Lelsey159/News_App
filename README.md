News
News is a web application that displays a list of various news sources. On choosing a news source, it will preview the top news articles of the day. Clicking a news article > > will redirect the user to read it fully from the news source. It achieves this by using the News API.

Demo-Link
Demo https://kivazm.herokuapp.com/

Author
Lesley Hope

Description
News is a web application that displays a list of various news sources. On choosing a news source, it will preview the top news articles of the day. Clicking a news article > > will redirect the user to read it fully from the news source. It achieves this by using the News API.

User Stories
As a user I would like:
to see various news sources and select the ones I prefer
to see all the news articles from that news source
to see the image, description and time the news article was created.
to click on an article and read it fully from the news source.

Prerequisites
Python3.9

How to use
Click (https://leshys.herokuapp.com/)
Click any News source you'd like

Setup/Installation
git clone hhttps://github.com/Lelsey159/News_App.git
$ cd News
$ python -m venv virtual (install virtual environment)
$ source virtual/bin/activate
$ python -m pip install -r requirements.txt (install all dependencies)
Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
$ ./start.sh

Contact Information
Email me at [lesleyhope159@gmail.com]

Technologies Used
Python3.9
Flask framework
Bootstrap
License
MIT License:
Copyright (c) 2022 Lesley Hope