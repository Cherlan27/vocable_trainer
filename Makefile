SHELL := powershell.exe
.SHELLFLAGS := -NoProfile -Command

PYTHON := .\backend\.venv\Scripts\python.exe
COMPOSE := docker compose -f docker-compose.yaml

.PHONY: backend frontend llm_server dev

backend:
	& $(PYTHON) backend\src\main.py

frontend:
	cd frontend; npm run dev

llm_server:
	$(COMPOSE) up llm_service

dev:
	Start-Process powershell -ArgumentList "& '$(PYTHON)' backend\src\main.py"
	Start-Process powershell -ArgumentList "cd frontend; npm run dev"
	Start-Process powershell -ArgumentList "$(COMPOSE) up llm_service"
