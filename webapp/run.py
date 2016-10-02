from weight import app

if __name__ == "__main__":
    app.run(host=app.config.get("HOST", "localhost"))
