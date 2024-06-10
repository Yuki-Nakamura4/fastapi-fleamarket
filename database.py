from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://fastapiuser:fastapipass@0.0.0.0:5432/fleamarket"

# create_engine関数でSQLAlchemyエンジンを作成
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

# sessionmaker関数でセッションを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base関数でベースクラスを作成
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()