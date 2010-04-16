all:
	touch db.sqlite
	./manage.py syncdb
rundebug:
	./manage.py runserver	
clean:
	rm db.sqlite *.pyc

