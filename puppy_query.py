import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from puppies import Puppy, Shelter

print "\nVersion: ", sqlalchemy.__version__

engine = create_engine('sqlite:///puppyshelter.db', echo=False)

# Query all of the puppies and return the results
# in ascending alphabetical order
conn = engine.connect()
all_puppies = select([Puppy.label('pup')]).order_by("pup")
result = conn.execute(all_puppies)
row = result.fetchone()

for row in result:
	print row

conn.close()
