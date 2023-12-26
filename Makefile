build:
	docker build -t talana-kombat .

run:
	docker run -it talana-kombat

run-compose:
	docker-compose build && docker-compose run --rm talana-kombat

test:
	docker run -it talana-kombat pytest tests/ -s
