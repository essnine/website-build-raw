import os
import logging
from flask import Flask, send_from_directory


app = Flask("sitewiki")
app.template_folder ="."


@app.get("/")
@app.get("/<path:path>")
def get_page(path="Home.html"):
	try:
		return send_from_directory(directory="./",path=path)
	except Exception as exc:
		logging.exception(str(exc))
		return "Something went wrong", 422

if __name__ == '__main__':
	app.run(port=8080)