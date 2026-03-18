.PHONY: setup dev up down

setup:
	uv venv
	uv pip install fastapi[standard] redis requests pydantic
	uv pip install python-dotenv

up:
	docker compose up --build -d

dev:
	uv run fastapi dev app/main.py

down:
	docker compose down