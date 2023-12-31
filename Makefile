build:
	docker rmi talana-kombat -f && docker build -t talana-kombat .

run:
	docker run --name talana-kombat -it talana-kombat

down:
	docker stop talana-kombat

run-compose:
	$(MAKE) build && docker-compose run --name talana-kombat --rm talana-kombat

down-compose:
	docker-compose down

test:
	docker run -it talana-kombat pytest tests/ -s
