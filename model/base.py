from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

class Base(DeclarativeBase):

	# Database engin information
	host = 'localhost:5432'
	user = 'postgres'
	password = '24882533'
	database = 'testdb'

	# Establish Connection
	engine = create_engine("postgresql://postgres:24882533@localhost:5432/testdb")
	connect = engine.connect()