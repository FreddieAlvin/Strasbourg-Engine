# Shortcuts for macOS/Linux. On Windows (no make), run the commands shown in README.md.
PY ?= python3

.PHONY: all up down reset prepare index smoke

all: up prepare index smoke

up:
	docker compose up -d --wait

down:
	docker compose down

reset:            ## wipe Solr completely (cores + data)
	docker compose down -v

prepare:
	$(PY) src/prepare.py

index:
	$(PY) src/index.py

smoke:
	$(PY) src/search.py "overcrowded cell detention" --rows 5
