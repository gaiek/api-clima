.PHONY: setup dev up down

setup:
	uv venv
	uv pip install fastapi[standard] redis requests pydantic
	uv pip install python-dotenv

dev:
	uv run fastapi dev app/main.py

up:
	docker compose up --build -d

down:
	docker compose down