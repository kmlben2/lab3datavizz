### ouvrir le first_app.py (lab2) : streamlit run first_app.py
### ouvrir le component (lab3) : streamlit run __init__.py

import streamlit as st
# importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd 
import time

st.title("Camélia's Lab3 :wave:")

###### LAB3 - PART 1

import os
# Create a folder for the pipeline step files
st_folder = 'st_app_solution'
os.makedirs(st_folder, exist_ok=True)

print(st_folder)

st.text("Welcome. In the following page, we'll make a lot of data viz")
st.markdown('Data vizualisation is **_really_ cool** :+1::sob:')
# st.caption("let's start with this formula")
# st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)''')
# st.write('Personnaly, I prefer manipulating data :sunglasses:')

# st.write(1234)
# st.write(pd.DataFrame({ 'first column': [0, 1, 2, 3], 'second column': [10, 20, 30, 40] }))

# st.title('Part 2 of the Lab :')
# st.header("We're learning how to create headers...")
# st.subheader('...and subheaders too :wink:')

# df = pd.DataFrame({
# 'first column': [0, 1, 2, 3],
# 'second column': [10, 20, 30, 40]
# })
# st.write(df)

# chart_data = pd.DataFrame(
# np.random.randn(20, 3),
# columns=['a', 'b', 'c'])
# st.line_chart(chart_data)

# st.header('Map of Paris :blue_heart:')

# map_data = pd.DataFrame(
# np.random.randn(1000, 2) / [50, 50] + [48.8316993713378, 2.3231999874114],
# columns=['lat', 'lon'])
# st.map(map_data)

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
# chart_data

# option = st.selectbox(
# 'How many siblings do you have??',
# df['first column'])
# 'You have', option, 'siblings'

# option2 = st.sidebar.selectbox(
# 'Which number do you like best?',
# df['second column'])
# 'and your favourite number is', option2

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Patientez pour voir la suite.... {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'...Enjoy part 3 !'


###### PARTIE 3 DATA VIZUALISATION

st.set_option('deprecation.showPyplotGlobalUse', False)


st.title("Partie 3 : Data vizualisation :white_check_mark:")

import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("uber-raw-data-apr14.csv")

df["Date/Time"]=pd.to_datetime(df["Date/Time"], format = '%m/%d/%Y %H:%M:%S')

#get dom
def get_dom(dt): 
    return dt.day 
df['dom']=df["Date/Time"].map(get_dom)

#get week day
def get_weekday(dt): 
    return dt.weekday() 
df['weekday'] = df['Date/Time'].map(get_weekday)

#premier histogramme avec dom
fig, ax = plt.subplots()

def hist1():
    ax.hist(x=df['dom'], bins=20, rwidth=0.8, range=(0.5,30.5))
    ax.set_xlabel("Date of the month")
    ax.set_ylabel("Frequency")
hist1()

st.caption("**In this third part, you can click on buttons such as the one bellow, to display graphs :arrow_down: ** ")

def data4():
    agree4 = st.button("Click to see the histogram of the frequency in function of the Date of the month")
    if agree4:
        st.pyplot(fig)
data4()

#function for Grouping the data by date of month (dom)
def count_rows(rows): 
    return len(rows)

#groupby1 + affichage
def groupBy():
    grpby=df.groupby(df['dom']).apply(count_rows)
    ax.set_xlabel("Date of the month")
    ax.set_ylabel("Frequency")
    st.bar_chart(data=grpby)
groupBy()

#groupby2 sorted + affichage
# grpby2=grpby.sort_values()
# ax.set_xlabel("Date of the month")
# ax.set_ylabel("Frequency")
# st.bar_chart(data=grpby2)

@st.cache

def load_data(nrows):
    data = pd.read_csv('uber-raw-data-apr14.csv', nrows=nrows)
    return data

data_load_state = st.text("Loading data...")
uber_data = load_data(1000)

st.subheader("Uber raw data")
st.write(uber_data)

#Bar Chart

def data1():
    agree = st.button("Click to see Longitude and Latitude bar charts")
    if agree:
        df = pd.DataFrame(uber_data[:300], columns = ["Lon","Lat"])
        df.hist()
        plt.show()
        st.pyplot()
data1()

# #Line Chart
# st.line_chart(df["Lon","Lat"])

def data2():
    agree2 = st.button("Click to see chart data of Longitude and Latitude")
    if agree2:
        chart_data = pd.DataFrame(uber_data[:40], columns=["Lon", "Lat"])
        st.area_chart(chart_data)
data2()



import time
import datetime
import streamlit.components.v1 as components

def log(func):

    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Called function : " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper

@log
@st.cache(suppress_st_warning=True)
def data3(name):
    agree3 = st.button("Click to see the evolution of Date/Time")
    if agree3:
        st.bar_chart(uber_data["Date/Time"])
data3("data3")

import streamlit as st
import time

##caching example1
def expensive_computation(a, b):
    time.sleep(2)  # 👈 This makes the function take 2s to run
    return a * b

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)

###### LAB3 - PART 2

import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://images.unsplash.com/photo-1536257104079-aa99c6460a5a?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bGFuZHNjYXBlc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80", width=500, height=500)
components.iframe("https://lh3.googleusercontent.com/4mVNVUybMXXJ5k-PuXHwqwBFDLUZbAuSxa7xcypndKhFZ9RPEGVcoXpU9mLQL6lGg3z3Cvp5pJFWDXwKiYDPWOH9zQ=w640-h400-e365-rj-sc0x00ffffff", width=500, height=500)

