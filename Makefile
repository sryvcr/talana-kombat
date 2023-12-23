build:
	docker build -t talana-kombat .

run:
	docker run -it talana-kombat

test:
	docker run -it talana-kombat pytest tests/ -s
