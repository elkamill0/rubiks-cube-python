.PHONY: run reset stop format lint test
export PYTHONPATH := src
export PYTHONPATH := src:.

run:
	uv run streamlit run app/new_app.py --server.port 8501 &
	uv run streamlit run app/app.py --server.port 8502 --server.headless true

reset:
	@echo "Cleaning ports 8501 and 8502..."
	@-kill -9 $$(lsof -t -i:8501) 2>/dev/null || true
	@-kill -9 $$(lsof -t -i:8502) 2>/dev/null || true
	uv run streamlit run new_app.py --server.port 8501 &
	uv run streamlit run app.py --server.port 8502 --server.headless true

stop:
	pkill -f "streamlit"

format:
	uv run ruff format .

lint:
	uv run ruff check --fix .

test:
	uv run pytest