build:
	docker build -t talana-kombat .

run:
	docker run -it talana-kombat

test:
	pytest tests/ -s
