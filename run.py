from application import app
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(loging.ERROR)

if __name__ == '__main__':
    app.run(debug=True)
