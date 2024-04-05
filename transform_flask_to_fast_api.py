from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    """Return a simple HTML tag."""
    return "<p>Hello, World!</p>"
