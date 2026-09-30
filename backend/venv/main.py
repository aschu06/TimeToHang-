from fastapi import FastAPI 
from database import get_database
from database import create_tables

app = FastAPI()
create_tables()

@app.get("/")

def home():
    return {"message": "app backend is running :3"}

#@      connects the fastapi to the function
#app    the actual api
#.post  a request
#.get   reading of data
#"/.../"url path



#-------------------- Events --------------------------------


# Create a new event
@app.post("/events")
def create_event(title: str, start_date: str, end_date: str):
    data = get_database()
    cursor = data.execute(
        "INSERT INTO events (title, start_date, end_date) VALUES (?, ?, ?)",            ##adds a row with the title and dates,? gets filled iwth actual values 
        (title, start_date, end_date)
    )
    new_row_id = cursor.lastrowid                                                           ##gets the ID number assigned to that new row 
    data.commit()
    data.close()
    return {"id": new_row_id}                                                               ##returns that new row id                             

# Look up an event by its ID
@app.get("/events/{event_id}")
def get_event(event_id: int):
    data = get_database()
    cursor = data.execute("SELECT * FROM events WHERE id = ?", (event_id,))                ##finds the event by its ID
    row = cursor.fetchall()                                                                ##list of all matching rows 
    data.close()

    if len(row) == 0:                                                                      ##no event found
        return {"error": "Event not found"}
                                                                         
    return {
        "id": row[0][0],
        "title": row[0][1],
        "start_date": row[0][2],
        "end_date": row[0][3]
    }


# ------------------ People -----------------------

# Add a person to an event
@app.post("/events/{event_id}/person")
def add_person(event_id: int, name: str):
    data = get_database()                                                 #open the database to access
    cursor = data.execute(                                                  #run sql command
        "INSERT INTO person (event_id, name) VALUES (?, ?)",          #add the new person
        (event_id, name)                                                    #with their values 
    )
    new_id = cursor.lastrowid                                               #get the id num database gave this person
    data.commit()
    data.close()
    return {"id": new_id}                                                   #return that id back


#------------------ Availability -------------------

@app.post("/person/{person_id}/availability")
def add_availability(person_id: int, start_time: str, end_time: str):
    data = get_database()
    data.execute("INSERT INTO availability (person_id, start_time, end_time) VALUES (?,?,?)",(person_id,start_time,end_time))
    data.commit()
    data.close()
    return {"message":"Free Time saved"}


@app.get("/events/{event_id}/availability") 
def get_availability(event_id:int):
    data = get_database()
    result = data.execute(
        "SELECT person.name, availability.start_time, availability.end_time "
        "FROM person, availability "
        "WHERE person.id = availability.person_id AND person.event_id = ?",(event_id,)
    )
    rows = result.fetchall()
    data.close()

    output = []
    for row in rows:
        output.append({"name": row[0], "start_time": row[1], "end_time": row[2]})
    return output









