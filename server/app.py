from werkzeug.exceptions import NotFound

...

@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: The requested resource does not exist.",
        404
    )

    return response

app.register_error_handler(404, handle_not_found)