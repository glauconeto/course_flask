from flask import Flask, request

app = Flask(__name__)


@app.route('/form')
def formulario():
    return (
        "<form action='/receiver' method='post' enctype='multipart/formdata>"
            "<label for='username'>Username:</label>"
            "<input type='text' name='username' />"
            "<label for='cor'>Cor:</label>"
            "<input type='text' name='cor' />"
            "<input type='file' name='foto' />""<br>"
            "<input type='submit' value='envia ai!!' />"
        "</form>"
    )

@app.route("/receiver", methods=['post'])
def receiver():
    __import__("ipdb").set_trace()
    return f"{request.values['username']}"