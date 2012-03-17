all:
	touch db.sqlite
	./manage.py syncdb
rundebug:
	./manage.py runserver	
clean:
	rm -f db.sqlite *.pyc

