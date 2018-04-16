import datetime as dt
import numpy as np
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

engine = create_engine("sqlite:///Data/belly_button_biodiversity.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
OTU = Base.classes.otu
Samples = Base.classes.samples
Samples_meta = Base.classes.samples_metadata

app = Flask(__name__)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route('/names')
def names_list():
    inspector = inspect(engine)
    sample_names = []

    columns = inspector.get_columns('samples')
    for column in columns:
        sample_names.append(column["name"])
    del sample_names[0]

    return jsonify(sample_names)

@app.route('/otu')
def otu_list():
    session = Session(engine)
    otu_descrip = session.query(OTU.lowest_taxonomic_unit_found).all()
    dataframe = pd.DataFrame(otu_descrip)
    otu_description = []
    otu_description = dataframe["lowest_taxonomic_unit_found"].values.tolist()
    return jsonify(otu_description)

@app.route('/metadata/<sample>')
def metadata_data(sample):

    session = Session(engine)
    age=[]
    bbtype = []
    ethnicity = []
    gender =[]
    location = []
    sampleid = []

    age = session.query(Samples_meta.AGE).all(),
    bbtype = session.query(Samples_meta.BBTYPE).all(),
    ethnicity = session.query(Samples_meta.ETHNICITY).all(),
    gender = session.query(Samples_meta.GENDER).all(),
    location = session.query(Samples_meta.LOCATION).all(),
    sampleid = session.query(Samples_meta.SAMPLEID).all()


    df1 = pd.DataFrame(age[0])
    df2 = pd.DataFrame(bbtype[0])
    df3 = pd.DataFrame(ethnicity[0])
    df4 = pd.DataFrame(gender[0])
    df5 = pd.DataFrame(location[0])
    df6 = pd.DataFrame(sampleid)

    meta_df = df1.join(df2).join(df3).join(df4).join(df5).join(df6)

    sample_id = sample.split('_')
    sampleid = int(sample_id[1])

    metadata = {}

    metadata ={'AGE':str(meta_df.loc[meta_df['SAMPLEID'] == sampleid]["AGE"].iloc[0]),
            'BBTYPE': meta_df.loc[meta_df['SAMPLEID'] == sampleid]["BBTYPE"].iloc[0],
            'ETHNICITY':meta_df.loc[meta_df['SAMPLEID'] == sampleid]["ETHNICITY"].iloc[0],
            'GENDER':meta_df.loc[meta_df['SAMPLEID'] == sampleid]["GENDER"].iloc[0],
            'LOCATION':meta_df.loc[meta_df['SAMPLEID'] == sampleid]["LOCATION"].iloc[0],
            'SAMPLEID':str(sampleid)}

    return jsonify (metadata)

@app.route('/wfreq/<sample>')
def wash_freq_data(sample):
    session = Session(engine)
    wash = []
    sampleid = []

    wash = session.query(Samples_meta.WFREQ).all(),
    sampleid = session.query(Samples_meta.SAMPLEID).all()

    df1 = pd.DataFrame(wash[0])
    df2 = pd.DataFrame(sampleid)
    wash_df = df1.join(df2)

    request_sample = 'BB_940'
    sample_id = request_sample.split('_')
    sampleid = int(sample_id[1])


    wash_freq= wash_df.loc[wash_df['SAMPLEID'] == sampleid]["WFREQ"].iloc[0]

    return wash_freq

@app.route('/samples/<sample>')
def sample_data(sample):

    df = pd.read_sql_query("SELECT * FROM samples",engine)
    sample_df = df.loc[df[sample] != 0][['otu_id',sample]]
    sample_df = sample_df.sort_values(sample, ascending = False)


    sample_dict = {'otu_ids':sample_df['otu_id'].tolist(), 'sample_values':sample_df[sample].tolist()}

    sample_dict_list = []
    sample_dict_list = [sample_dict]

    return jsonify(sample_dict_list)

if __name__ == '__main__':
    app.run(debug=True)
