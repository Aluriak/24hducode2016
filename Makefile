
start:
	python3 -m src --longitude="-0.07" --latitude="47.70"

a: all
all: rmcache start


rmcache:
	rm ressources/tobjects.pkl



