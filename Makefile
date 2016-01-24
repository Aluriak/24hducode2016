
start:
	python3 -m src

a: all
all: rmcache start


rmcache:
	rm ressources/tobjects.pkl



