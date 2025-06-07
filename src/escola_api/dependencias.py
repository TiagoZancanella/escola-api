from src.escola_api.database.banco_dados import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



