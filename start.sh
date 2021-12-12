source env/bin/activate
python3 -m pip install -r requirements.txt
export QUART_APP=main
export QUART_ENV=development
quart run