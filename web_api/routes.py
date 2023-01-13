from flask import Flask, request, abort, render_template

from app.components.complex.decryption import Decryption
from app.components.complex.encryption import Encryption
from system.constants import HttpStatus

app = Flask(__name__)


@app.get('/')
def show_stub():
    return render_template('stub.html')


@app.post('/encrypt')
def encrypt():
    req_txt = request.form.get('text')

    if not req_txt:
        abort(HttpStatus.BAD_REQUEST)

    try:
        data = Encryption(req_txt)

        return {
            'text': data.encrypted_txt,
            'key': data.key
        }
    except ValueError:
        abort(HttpStatus.INTERNAL_SERVER_ERROR)


@app.post('/decrypt')
def decrypt():
    encrypted_text = request.form.get('text')
    encryption_key = request.form.get('key')

    if len(request.form) != 2 or not encrypted_text or not encryption_key:
        abort(HttpStatus.BAD_REQUEST)

    data = Decryption(encrypted_text, encryption_key)

    return {
        'text': data.original_txt
    }
