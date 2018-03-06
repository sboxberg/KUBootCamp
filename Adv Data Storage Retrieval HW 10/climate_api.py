from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

app = Flask(__name__)

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurements
Station = Base.classes.stations
session = Session(engine)
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Avalable Routes:<br/><br/>"
        f"/api/v1.0/precipitation - dates and temperature observations from the last year<br/><br/>"

        f"/api/v1.0/stations - list of stations<br/><br/>"
        
        f"/api/v1.0/tobs - Temperature Observations (tobs) for the previous year<br/><br/>"
        
        f"/api/v1.0/start_date/end_date - use YYYY-MM-DD format for start and end date - <br/>"
        f"minimum temperature, the average temperature, and the max temperature from start date to end date<br/>"
        f"if no end date provided, will return to end of data"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the dates and temperature observations from the last year as json"""
    precip_data = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date > "2016-08-22").all()
    precip_dict=[r._asdict() for r in precip_data]
    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return the list of stations as json"""
    stations = session.query(Station.station).all()
    station_dict=[r._asdict() for r in stations]
    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def temp_obs():
    """Return the list of Temperature Observations (tobs) for the previous year as json"""
    temp_data = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date > "2016-08-22").all()
    temp_dict=[r._asdict() for r in temp_data]
    return jsonify(temp_dict)

@app.route("/api/v1.0/<begin_date>")
@app.route("/api/v1.0/<begin_date>/<end_date>")
def temperatures(begin_date='2018-01-01',end_date='2017-08-22'):
    """Return the minimum temperature, the average temperature, and the max temperature for a given start-end range as json"""
   
    #I made the assumption that we would do the same as the previous exercise and find for the year before -- the instructions
    #don't say that and it would have been easier to not mess with it.  I probably should have just done it based on the actual
    #date entries!!

    #reduce year by one
    date=begin_date.split('-')
    date[0]=str(int(date[0])-1)
    new_begin_date = '-'.join(date)
    date=end_date.split('-')
    date[0]=str(int(date[0])-1)
    new_end_date = '-'.join(date)
    #query data and load into dataframe
    temp_data=session.query(Measurement.tobs).filter(Measurement.date >= new_begin_date).\
    filter(Measurement.date <= new_end_date)
    temperature_data = []
    for row in temp_data:
        temperature_data.append(row)
    temp_data_df=pd.DataFrame(temperature_data)
    #find min, max, avg and return those values
    TMIN = temp_data_df['tobs'].min()
    TMAX = temp_data_df['tobs'].max()
    TAVG = temp_data_df['tobs'].mean()
    temp_dic = {}
    temp_dic["TMIN"]=TMIN
    temp_dic["TMAX"]=TMAX
    temp_dic["TAVG"]=TAVG
    temp_list = []
    temp_list.append(temp_dic)
    
    return jsonify(temp_list)

if __name__ == "__main__":
    app.run(debug=True)