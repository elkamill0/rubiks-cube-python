# Makefile

run:
	streamlit run app.py

# Opcjonalnie: czyść cache Streamlit
clean:
	streamlit cache clear


build:
	python setup.py build
	python setup.py install