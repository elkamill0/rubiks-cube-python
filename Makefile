# Makefile

run:
	streamlit run new_app.py --server.port 8501 --server.headless true & 
	streamlit run app.py --server.port 8502 --server.headless true

stop:
	pkill -f "streamlit"
