import sys

try:
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
except:
    sys.exit("[!] Por favor, instale a biblioteca sqlalchemy com o comando: sudo pip install sqlalchemy")

engine = create_engine("sqlite:///banco.db")
Base = declarative_base()

class Usuario(Base):
    __table__ = 'usuarios'
    id = Column(Integer, primary_key= True)
    nome = Column(String)

if __name__ == 'main':
    Base.metadata.create_all(engine)