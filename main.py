import flask

# ----

app = flask.Flask(__name__)

@app.get("/")
def root():
    return {"text": "hello!"}

@app.get("/echo")
def echo():
    request_data = {}
    for key, value in flask.request.args.items():
        request_data[key] = value
    return request_data

@app.post("/form")
def form():
    request_data = {}
    for key, value in flask.request.args.items():
        request_data[key] = value
    form_data = {}
    for key, value in flask.request.form.items():
        form_data[key] = value
    return {"url_params": request_data, "form": form_data}


app.run(debug=True)
