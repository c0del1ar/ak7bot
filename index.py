from telebot import TeleBot

app = TeleBot(__name__)
apikey = "2050081411:AAGC0kDky61MvI-qTrXMfnqqR2lnxzX0bJ4"
menuny = [".song",".gambar",".musik",".maker"]

@app.route(".menu")
def menu(msg):
    reply = msg['chat']['id']
    msg = "List Menu: \n\n"
    for a in menuny:
        msg += a+"\n"
    msg += "\nSilahkan dipilih"

    app.send_message(reply,msg)


if __name__ == '__main__':
    app.config['api_key'] = apikey
    app.poll(debug=True)
