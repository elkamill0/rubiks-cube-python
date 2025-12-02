# Makefile

run:
	streamlit run new_app.py --server.port 8501 & 
	streamlit run app.py --server.port 8502 --server.headless true

stop:
	pkill -f "streamlit"
