from flask import Flask
import psycopg2
from healthcheck import HealthCheck

app = Flask(__name__)

health = HealthCheck(app, "/healthcheck")

@app.route('/')
def hello_world():
    return 'Hello, World!'

def test_db_connection():
  from sqlalchemy import create_engine
  db_string = "postgres://admin:admin@localhost:5434/admin" 
  db = create_engine(db_string)
  # Create 
  db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
  db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")
  # Read
  result_set = db.execute("SELECT * FROM films")  
  for r in result_set:  
      print(r)
  # Update
  db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")
  # Delete
  db.execute("DELETE FROM films WHERE year='2016'")
  return True, "Success"

def test_sum():
  if 1 + 2 == 3:
    return True, "3"

health.add_check(test_db_connection)
health.add_check(test_sum)

if __name__ == "__main__":
  # test_db_connection()
  app.run(debug=True)