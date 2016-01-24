LONGITUDE="-0.07"
LATITUDE="47.70"


start:
	rm /var/www/html/24h/tmp/*
	python3 -m src --longitude=$(LONGITUDE) --latitude=$(LATITUDE)

a: all
all: rmcache start


rmcache:
	rm ressources/tobjects.pkl



