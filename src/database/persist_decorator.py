from database import db

def persist_decorator(function : callable):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        db.connection.commit()

    return wrapper
