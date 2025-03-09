from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

URL = "postgresql://alexandrbalashov:1349@localhost/hw"
engine = create_engine(URL)
LocalSession = sessionmaker(bind=engine)
session = LocalSession()
