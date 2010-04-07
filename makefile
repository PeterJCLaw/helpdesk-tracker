all:
	touch db.sqlite
	./manage.py syncdb
rundebug:
	./manage.py runserver	
