from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy.pool import NullPool


engine = None


def init_db_engine(connect_str):
    global engine, Session
    engine = create_engine(connect_str, poolclass=NullPool)
    Session = scoped_session(
        sessionmaker(bind=engine)
    )


@contextmanager
def mb_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
