.PHONY: tests_all test-file serve selenium streamlit

tests_all:
	poetry run pytest -v -rP

test-file:
	poetry run pytest -v -rP $(file)

serve:
	mkdocs gh-deploy

selenium:
	docker run --name selenium -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.9.1-20230508

streamlit:
	streamlit run scripts/search/streamlit.py --server.port 8001
