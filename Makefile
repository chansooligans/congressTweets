.PHONY: tests_all test-file book serve

tests_all:
	poetry run pytest -v -rP

test-file:
	poetry run pytest -v -rP $(file)

book:
	poetry run jb build book

serve:
	python -m http.server -d book/_build/html $(port)

selenium:
	docker run --name selenium -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.9.1-20230508