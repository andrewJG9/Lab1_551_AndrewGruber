import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine=create_engine(os.getenv("DATABASE_URL"))

db=scoped_session(sessionmaker(bind=engine))

def main():
    
    x=open("books.csv")

    r=csv.reader(x)
    
    for isbn, title, author, year in r:

        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn":isbn, "title":title, "author":author, "year":year})

    db.commit()



if __name__=="__main__":
    main()
