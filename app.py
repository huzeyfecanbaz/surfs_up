#import dependencies for Flask, datetime, pandas, and numpy
from flask import Flask,jsonify
import datetime as dt
from itsdangerous import json
import pandas as pd
import numpy as np
from requests import session

#import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, engine_from_config,func

#setup the database engine
engine=create_engine('sqlite:///hawaii.sqlite')

#setup the classes by using Base
Base=automap_base()

#reflect the tables
Base.prepare(engine,reflect=True)

#save the references to each table. references are Measurement, Station
Measurement=Base.classes.measurement
Station=Base.classes.station

#create a session link
session=Session(engine)

#now define the app for the Flask
#Create flask application called app
app=Flask(__name__)

# define a welcome root
@app.route("/")
def welcome():
    return('''
    
    Welcome wo the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#create the precipitation route
#add the line of code that calculates the date one year ago from the most recent date in the database
#write a query to get the date and precipitation for the previous year
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year=dt.date(2017,8,23)-dt.timedelta(days=365)
    precipitation=session.query(Measurement.date,Measurement.prcp).\
        filter(Measurement.date>=prev_year).all()
    #using jsonify, create a dictionary with the date as the key and the precipitation as the value
    precip={date:prcp for date, prcp in precipitation}
    return jsonify(precip)

#create stations route
@app.route('/api/v1.0/stations')
def stations():
    results=session.query(Station.station).all()
    stations=list(np.ravel(results))
    return jsonify(stations=stations)

#monthly temperatire route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year=dt.date(2017,8,23)-dt.timedelta(days=365)
    results=session.query(Measurement.tobs).\
        filter(Measurement.station=='USC00519281').\
        filter(Measurement.date>=prev_year).all()
    temps=list(np.ravel(results))
    #unravel the results into one-dimensional array and convert that array to a list
    return jsonify(temps=temps)

#statistics route
#this route needs to provide both start and end date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
