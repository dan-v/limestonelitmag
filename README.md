Limestone lit mag
=========

This is the code that produced the website
<pre>
	http://limestonelitmag.com
</pre>

Feel free to grab or use any of the back end django work as well as the front end CSS/HTML bootstrap work. 



Steps on installation
======================
* First pull down the code using git clone
* Open up <i>limestonelitmag/settings.py</i> and edit the DATABASES field to match the database you're using. (in this case I am using a postgres db) Need a
* Name
* User
* Password
<pre>
	DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }

}
</pre>