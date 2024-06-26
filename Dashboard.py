import streamlit as st
from streamlit_lottie import st_lottie
import time
import datetime 
import requests
import math
import random
from annotated_text import annotated_text
import numpy as numpy
import json
import requests
import streamlit_authenticator as stauth 
import re
from deta import Deta
from streamlit_calendar import calendar


st.title("TGYYMP")
with st.sidebar:
    st.title("TGYYMP")
    
tab_titles = [
    "About Us",
    "Questionnaire",
    "Calender",
    "Cross Section",
    "Fitness Tracker",
    "Visuals & Content",
    "Nutrition",
    "Body Composition",
    "Cognitive Performance "

]
tabs = st.tabs(tab_titles)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

##TAB1 (ABOUT US)
with tabs[0]:
    st.title("TGYYMP")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

col1, col2 , col3 = st.columns(3)
col1.metric("Average Daily Vistors", "74" , "28%")
col2.metric("Active Users", "1,103" , "23%")
col3.metric("User Satisfaction", "1.5x" , "4%")


Heart_Url = "https://lottie.host/7903bfb8-305c-44f9-9b43-2ba0de1897a6/UeNFDFWrkB.json"
lottie_Heart = load_lottieurl(Heart_Url)
#st_lottie(lottie_Heart, speed=2, reverse=False, loop=True, quality="medium", height=100, width=100,
    #key=None)

Symbol_Url = "https://lottie.host/09b8d866-34a4-4f9c-98cf-889920678ddd/w96EI5835r.json"
lottie_Symbol = load_lottieurl(Symbol_Url)

lottie_url_hello = "https://lottie.host/728462af-3e70-44b9-ac15-26da4edb9d78/zB5U2gBCXU.json"
lottie_hello = load_lottieurl(lottie_url_hello)

Camera_Url = "https://lottie.host/6c4f7a87-e6e9-483e-8510-ff62be45bf00/wAPBeI8IaE.json"
lottie_Camera = load_lottieurl(Camera_Url)

Tracker_Url = "https://lottie.host/8f47544e-b5c4-4d65-8d36-6c3d3c5688b9/nqDM9Gviwd.json"
lottie_Tracker = load_lottieurl(Tracker_Url)

##Check Us out on Youtube.
st.title("The tailored fitness logbook experience") 
st_lottie(lottie_Symbol, speed=2, reverse=False, loop=True, quality="medium", height=100, width=100,
    key=None) 
st.subheader("At TGYYMP we are committed to delivering optimal user experience, so you’ll be encouraged to improve your existing training, weight loss and recovery while you develop new techniques and reach your desired goals.")
st.title("Proprietary visuals and content")
st_lottie(lottie_Camera, speed=2, reverse=False, loop=True, quality="medium", height=100, width=100,
    key=None)
st.subheader("Upload content or take a snapshot of your sessions or current training program, exclusively for you to complement your growth. The body achieves what the mind believes!")
st.title("Meal planning")
st_lottie(lottie_hello, speed=2, reverse=False, loop=True, quality="high", height=150, width=150,
    key=None)
st.subheader("Find your ultimate meal prep plan using TGYYMP functionality and discover many alternatives for satisfying your needs and your goals. Manage your meals daily and weekly, stay on trend and plan ahead!")
st.title("A fitness logbook on demand")
st_lottie(lottie_Heart, speed=2, reverse=False, loop=True, quality="medium", height=150, width=150,
    key=None)
st.subheader("TGYYMP cross-section and cognitive performance should aid you too your ideal body composition.")
st.title("Track performance and statistics")
st_lottie(lottie_Tracker, speed=2, reverse=False, loop=True, quality="medium", height=100, width=100,
    key=None)
st.subheader("Documentation of performance is imperative for future growth. Stay in touch with your adequate weight composition and share your achievements on other social platforms #TGYYMP. Plus, you can edit your SMART goals performance in the ‘Gallery’ page.")
annotated_text("SOME PEOPLE ", ("WANT", "#8ef"),"IT TO HAPPEN" )
annotated_text("SOME PEOPLE ", ("WISH", "#8ef") , "IT WOULD HAPPEN.")
annotated_text("OTHERS" , ("MAKE", "#8ef") ,"IT HAPPEN.") 
DETA_KEY = "a01kqvdgtag_QfV2f8qK1HS7uBATcgV8uezx4hdgkGcV"

deta = Deta(DETA_KEY)

db = deta.Base("StreamlitAuth1")
#Signup/Login
def insert_user(email, username, password):

    """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:

    """
    date_joined = str(datetime.datetime.now())

    return db.put({"key": email, "username":username, "password": password, "date_joined": date_joined})

insert_user("test@outlook.com", "test1", "123456")

def fetch_users():
    """
    Fetch Users
    :return Dictionary of Users:
    """
    users = db.fetch()
    return users.items

def get_user_emails():
    """
    Fetch User Emails
    :return List of user emails:
    """
    users = db.fetch()
    emails = []
    for user in users.items:
        emails.append(user["key"])
    return emails

def get_usernames():
    """
    Fetch Usernames
    :return List of user usernames:
    """
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user["key"])
    return usernames

def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-z0-9-]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    if re.match(pattern, email):
        return True
    return False

def validate_username(username):
    """
    Checks Validity of userName
    :param username:
    :return True if username is valid else False:
    """

    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False
st.title(":green[Premium] Users")
st.subheader(":green[Sign up] to have access to more TGYYMP info on:")
st.subheader("Adequate body composition, weight loss, weight gain and nutrition goals.")
def sign_up():
    with st.form(key="signup", clear_on_submit=True):
        st.subheader(":green[Sign up]")
        email = st.text_input(":blue[Email]", placeholder="Enter Your Email")
        username = st.text_input(":blue[Username]", placeholder="Enter Your Username")
        password1 = st.text_input(":blue[Password]", placeholder="Enter Your Password" , type="password")
        password2 = st.text_input(":blue[Confirm Password]", placeholder="Confirm Your password" , type="password")
        st.form_submit_button("Sign up")

        if email:
            if validate_email(email):
                if email not in get_user_emails():
                    if validate_username(username):
                        if username not in get_usernames():
                            if len(username) >=2:
                                if len(password1) >= 6:
                                    if password1 == password2:
                                        hashed_password = stauth.Hasher([password2]).generate()
                                        insert_user(email, username, hashed_password[0])
                                        st.success("Account created successfully!")
                                    else:
                                        st.warning("Password Do Not Match")
                                             
                                else:
                                    st.warning("Password is too short")
                                    
                            else:
                                st.warning("Username is too short")
                                
                        else:
                           st.warning("Username Already Exists")    

                    else:
                        ("Invaild username")
                else:
                    ("Email Already exists!")
            else:
                st.warning("Invalid Email")

                                      
sign_up()
#Login

##TAB2(QUESTIONNAIRE)
#col20 , col21 , col22 = st.columns(3)
with tabs[1]:
    goals = st.radio ("What is your goal?", ["Muscle Gain", "Weight Loss"],
    captions = ["Bulking ", "Intensive Cardio",])
    Fitness_Level = st.radio ("What is your fitness Level?", ["Beginner", "Intermediate" , "Advanced"],
    captions = ["Once per week" , "3-4 times weekly ", "Train Daily",])
    Motivation = st.radio ("What is your motivation?", ["Improving your health", "Building strength and endurance" , "Boosting"])
    txt_Motivation = st.text_area("Motivational Comment")
    Body_Type  = st.radio ("What is your body type?" , [" Ectomorph(Skinny)", "Mesomorph(Regular)", "Endomorph(Extra)"])
    Desired_body = st.radio ("What is your desired body type?" , ["Cut(Shredded/Lean)" , "Bulky(Muscular/Large Frame)"])
    txt_body_type = st.text_area("Body Type Comment")
    options_areas = st.multiselect("What are your target areas?", ["Arms", "Abdominal", "Shoulders", "Pecs","Back", "Legs"])
    Active_lifestyle = st.radio ("Do you have a very active lifestyle?" , ["No" , "Somewhat" , "Yes"])
    Miles_coverage = st.radio ("How much miles have you ran in the past month?" , ["0-5 miles" , "5-10 miles" , "10+ miles"])
    Training_location = st.radio ("Desired training location?" , ["Gym", "Home"])
##TAB3(CROSS SECTION)
with tabs[3]:
    st.text("CROSS SECTION")
#colored_header(
    #label="",
      #  description="CROSS SECTION",
        #color_name="red-70",
   # )
#Cross section
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

Yoga_Url = "https://lottie.host/3e916808-c338-4191-ab43-67e3f083867b/PmeXwN6AlL.json"
Yoga_1 = load_lottieurl(Yoga_Url)

col4, col5, col6, col7, col8 = st.columns(5)

with col4:
    on = st.toggle('Yoga')
    st_lottie(Yoga_1, speed=4, reverse=False, loop=True, quality="medium", height=100, width=100,
    key=None
)
#on = st.toggle('Yoga')

Cardio_Url = "https://lottie.host/6720d5e0-f57b-467a-906b-5b85ab2c00c7/L3TnBeknK8.json"
Cardio_1 = load_lottieurl(Cardio_Url)

with col5:
    on = st.toggle('Cardio')
    st_lottie(Cardio_1, speed=4, reverse=False, loop=True, quality="high", height=135, width=135,
    key=None
)

Weights_Url = "https://lottie.host/74943121-7c90-4ad6-bec2-6deea0590f86/fPy500fqof.json"
Weights_1 = load_lottieurl(Weights_Url)

with col6:
    on = st.toggle('Strength Training')
    st_lottie(Weights_1, speed=4, reverse=False, loop=True, quality="low", height=110, width=110,
    key=None
)

Crossfit_Url = "https://lottie.host/e26e9cc2-9fb3-452d-81fc-0042c13c8ec2/74KnWcMuYV.json"
Crossfit_1 = load_lottieurl(Crossfit_Url)

with col7:
    on = st.toggle('CrossFit')
    st_lottie(Crossfit_1, speed=1, reverse=False, loop=True, quality="low", height=110, width=110,
    key=None
)
Sauna_Url = "https://lottie.host/2f5f72da-ade5-4396-94f5-deb19bad0655/CslW8ZEhF6.json"
Sauna_1 = load_lottieurl(Sauna_Url)

with col8:
    on = st.toggle('Hot Therapy')
    st_lottie(Sauna_1, speed=1, reverse=False, loop=True, quality="low", height=90, width=90,
    key=None
)
Boxing_Url = "https://lottie.host/a4ecf7bf-8507-4ac3-bb25-9cd89bac2e1a/XnkUA0TRm1.json"
Boxing_1 = load_lottieurl(Boxing_Url)

with col4:
    on = st.toggle("Boxing")
    st_lottie(Boxing_1, speed=1, reverse=False, loop=True, quality="low", height=90, width=100,
    key=None
)

Tennis_Url = "https://lottie.host/ea0f29ff-fd48-4170-b1bf-2a54d001e03f/iQgCMWeG3G.json"
Tennis_1 = load_lottieurl(Tennis_Url)

with col5:
    on = st.toggle('Tennis')
    st_lottie(Tennis_1, speed=1, reverse=False, loop=True, quality="low", height=65, width=90,
    key=None
)

Swim_Url = "https://lottie.host/07e1d834-7db8-46fc-9b49-b1d2f5839029/n7g3oFawji.json"
Swim_1 = load_lottieurl(Swim_Url)

with col6:
    on = st.toggle('Swimming')
    st_lottie(Swim_1 , speed=1, reverse=False, loop=True, quality="low", height=140, width=120,
    key=None
)
Cycling_Url = "https://lottie.host/1d458232-95fe-437f-aad5-9d1e4a628c84/BbIoU3wgkW.json"
Cycling_1 = load_lottieurl(Cycling_Url)

with col7:
    on = st.toggle('Cycling')
    st_lottie(Cycling_1, speed=1, reverse=False, loop=True, quality="low", height=100, width=100,
    key=None
)

Cold_Url = "https://lottie.host/c590f1a3-1ea1-49fb-9e01-88fa7b02b5b9/wuItKY33RU.json"
Cold_1 = load_lottieurl(Cold_Url)

with col8:
    on = st.toggle('Cold Therapy')
    st_lottie(Cold_1, speed=1, reverse=False, loop=True, quality="low", height=100, width=100,
    key=None
)

with col4:
    title = st.text_input('Type your workout', '')
    st.write('', title)
    option = st.selectbox(
    'GYYM Fit',
    ('Nike', 'Puma','Adidas','Under Armour','New balance','Asics','Fila','Reebok','Lululemon Athletica','Jordan Brand','Columbia Sportswear', 'Others'))
    
    #agree = st.checkbox('I agree')
with col5:
    t = st.time_input('Session Start', datetime.time(8, 00))
    t = st.time_input('Session End', datetime.time(10, 00))
with col7:
    BDY_COM = st.radio(
    "Pick your strength",
    ["Upper Body", "Lower body", "Core Body"],
    index=None,)
    st.write("You selected:", BDY_COM)
    agree = st.checkbox('Cross Section Complete')
 
with col8:
    #agree = st.checkbox('Workout complete')
    if agree:
        st.metric(label="Dashboard Usage", value ="50%", delta="30%",
    )
st.divider()
##TAB3(CALENDAR) 
with tabs[2]:
    st.title("Demo for streamlit-calendar📆")

mode = st.selectbox(
    "Calendar Mode:",
    (
        "daygrid",
        "timegrid",
        "timeline",
        "resource-daygrid",
        "resource-timegrid",
        "resource-timeline",
        "list",
        "multimonth",
    ),
)

events = [
    {
        "title": "Event 1",
        "color": "#FF6C6C",
        "start": "2023-07-03",
        "end": "2023-07-05",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "color": "#FFBD45",
        "start": "2023-07-01",
        "end": "2023-07-10",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "color": "#FF4B4B",
        "start": "2023-07-20",
        "end": "2023-07-20",
        "resourceId": "c",
    },
    {
        "title": "Event 4",
        "color": "#FF6C6C",
        "start": "2023-07-23",
        "end": "2023-07-25",
        "resourceId": "d",
    },
    {
        "title": "Event 5",
        "color": "#FFBD45",
        "start": "2023-07-29",
        "end": "2023-07-30",
        "resourceId": "e",
    },
    {
        "title": "Event 6",
        "color": "#FF4B4B",
        "start": "2023-07-28",
        "end": "2023-07-20",
        "resourceId": "f",
    },
    {
        "title": "Event 7",
        "color": "#FF4B4B",
        "start": "2023-07-01T08:30:00",
        "end": "2023-07-01T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 8",
        "color": "#3D9DF3",
        "start": "2023-07-01T07:30:00",
        "end": "2023-07-01T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 9",
        "color": "#3DD56D",
        "start": "2023-07-02T10:40:00",
        "end": "2023-07-02T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 10",
        "color": "#FF4B4B",
        "start": "2023-07-15T08:30:00",
        "end": "2023-07-15T10:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 11",
        "color": "#3DD56D",
        "start": "2023-07-15T07:30:00",
        "end": "2023-07-15T10:30:00",
        "resourceId": "e",
    },
    {
        "title": "Event 12",
        "color": "#3D9DF3",
        "start": "2023-07-21T10:40:00",
        "end": "2023-07-21T12:30:00",
        "resourceId": "f",
    },
    {
        "title": "Event 13",
        "color": "#FF4B4B",
        "start": "2023-07-17T08:30:00",
        "end": "2023-07-17T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 14",
        "color": "#3D9DF3",
        "start": "2023-07-17T09:30:00",
        "end": "2023-07-17T11:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 15",
        "color": "#3DD56D",
        "start": "2023-07-17T10:30:00",
        "end": "2023-07-17T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 16",
        "color": "#FF6C6C",
        "start": "2023-07-17T13:30:00",
        "end": "2023-07-17T14:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 17",
        "color": "#FFBD45",
        "start": "2023-07-17T15:30:00",
        "end": "2023-07-17T16:30:00",
        "resourceId": "e",
    },
]


##(TAB4) VISUALS & CONTENT
with tabs[5]:

    #Visuals and content
    st.title("Welcome To Dashboard")
    st.divider()
    st.text("VISUALS & CONTENT")
#colored_header(
    #label="",
        #description="VISUALS & CONTENT",
        #color_name="red-70",
   # )

    col1, col2, col3 = st.columns([2,2,1])
    camera_photo = col1.camera_input("Pre & Post workout photo")
    uploaded_photo = col2.file_uploader("Upload Content")


    with st.expander("Visuals") :
        if camera_photo :
          st.image(camera_photo)
          st.write("The perfect Caption!")
   
with st.expander("Content") :
    if uploaded_photo:
        st.image(uploaded_photo)
        st.write("Content Uploaded ... Congrats!")

Visuals_content = st.checkbox('Visuals & Content Complete')
progress_bar = col1.progress(0)
for perc_completed in range(100):
    time.sleep(0.01)
    progress_bar.progress(perc_completed+1)

     

with col3:
    TGYYMP_date = st.date_input("Today's Date ", datetime.date(2024, 6, 1))
    if Visuals_content:
        st.metric(label="Dashboard Usage", value ="20%", delta="20%",
    )
st.divider()
 
#Visuals and content

st.divider()
with tabs[7]:
    st.text("BODY COMPOSTION")
#colored_header(
   # label="",
     #   description="BODY COMPOSITION",
        #color_name="red-70",
    #)
    
col9, col10, col11, col12 =st.columns(4)
#Session-State
def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046
with col9:
    st.write("lbs/kg")
    pounds = st.number_input("Pounds:", key="lbs", on_change = lbs_to_kg)
    kilogram = st.number_input("Kilograms:", key="kg", on_change = kg_to_lbs)

def Cm_to_Feet():
    st.session_state.Feet = st.session_state.Cm/30.48
def Feet_to_Cm():
    st.session_state.Cm = st.session_state.Feet*30.48
with col10:
    st.write("ft/cm")
    Foot = st.number_input("Foot:", key="Feet", on_change = Feet_to_Cm)
    Centimeter = st.number_input("Centimeter:", key="Cm", on_change = Cm_to_Feet)

def Cen_to_inches():
    st.session_state.inches = st.session_state.Cen/2.54
def inches_to_Cen():
    st.session_state.Cen = st.session_state.inches*2.54
with col11:
    st.write("Inch/cm")
    Inches = st.number_input("Inches:", key="inches", on_change = inches_to_Cen)
    Centimeter_1 = st.number_input("Centimeter:", key="Cen", on_change = Cen_to_inches )
    
#Calculate Imperial metrics(BMI)
with col9:
    st.write("Body Mass Index(BMI)")
    #st.expander(explaining bmi)
    Height_BMI = st.number_input('Enter height in inches: ')
    Weight_BMI = st.number_input('Enter weight in pounds: ')
    try:
        bmi = Weight_BMI/(Height_BMI**2) * 703
    except:
        bmi = 0
with col9:
    if (bmi < 16):
        st.write("Your severly underweight" , bmi)
    elif (bmi >= 16 and bmi < 18.5):
         st.write("Your underweight - Body Mass Index : " , bmi)
    elif (bmi >= 18.5 and bmi < 25):
        st.write("Your healthy - Body Mass Index kg :" , bmi)
    elif (bmi >= 25 and bmi < 30):
        st.write("Your Overweight - Body Mass Index :" , bmi)
    elif (bmi >= 30):
        st.write("Your Obese - Body Mass Index :" , bmi)

with col10:
    st.write("Body Adipose Index(BAI)")
    #st.expander explaining adipose index
    HipCir_BAI = st.number_input('Enter hip circumference in Centimeters: ')
    Height_BAI = st.number_input('Enter height in feet: ')
    try:
        bai = HipCir_BAI/(Height_BAI)*math.sqrt(Height_BAI) - 18
    except:
        bai = 0
    st.write("Body Adipose Index % : " , bai)
with col11:
    st.write("Basal Metabolic Rate(BMR)")
    #st.expander explaining BMR
    Height_BMR = st.number_input('Enter height in Centimeters: ')
    Weight_BMR= st.number_input('Enter weight in kg: ')
    Age_years = st.number_input('Enter Age: ')
    Men_BMR = 88.362 + (13.397*Weight_BMR) + (4.799*Height_BMR) - (5.677*Age_years)
    Women_BMR = 447.593 + (9.247*Weight_BMR) + (3.098*Height_BMR) - (4.330*Age_years)
    Male = st.checkbox('Male BMR')
    Female = st.checkbox('Female BMR')
    if Male :
        st.write(" Your BMR is " , Men_BMR , "kcal")
    if Female:
        st.write(" Your BMR is " , Women_BMR , "kcal")
Section_complete  = st.checkbox('Body Composition Complete')
with col12:
    if Section_complete :
        st.metric(label="Dashboard Usage", value ="80%", delta="30%",)
   

st.divider()
st.text("COGNITIVE PERFORMANCE")
#colored_header(
    #label="",
       # description="COGNITIVE PERFORMANCE",
       # color_name="red-70",
#)

col13, col14 , col15 = st.columns(3)
#Yellow_1 = st.color_picker('Focus Endurance | Reaction Time | Alertness |', "#E3F900")
with col13:
    #st.expander explaining conginitive performance
    Yellow_1 = st.color_picker('Focus Endurance | Reaction Time | Alertness |', "#E3F900")
    Focus_En = random.uniform(55,82)
    Not_FocusEnd = random.uniform(45,62)
    reaction_time = random.uniform(55,82)
    Non_reaction_time = random.uniform(45,62)
    Alert_ness = random.uniform(55,82)
    Non_alertness = random.uniform(45,62)

    if Height_BMI >= 68 and Height_BMI < 73.62 or Weight_BMI >= 124 and Weight_BMI < 176.37 :
        st.write("Focus Endurance (%) : " , Focus_En)
        st.write("Reaction Time (%) : " , reaction_time)
        st.write("Alertness (%) : " , Alert_ness)

    
    else:
        st.write("Focus Endurance (%) : " , Not_FocusEnd)
        st.write("Reaction Time (%) : ", Non_reaction_time)
        st.write("Alertness (%) : " , Non_alertness)    
    
with col14:
    Blue_1 = st.color_picker('Reflexive Strength | Accuracy | Agility |', "#00F9D2")
    Reflexive_strength = random.uniform(55,82)
    Non_reflexive = random.uniform(45,62)   
    Accuracy = random.uniform(55,82)
    Non_Accuracy = random.uniform(45,62)
    Agility = random.uniform(55,82)
    Non_Agility = random.uniform(45,62)

    if Men_BMR >=1600 and Men_BMR < 1800 or Women_BMR >= 1300 and Women_BMR < 1500 :
        st.write("Reflexive Strength (%) : " , Reflexive_strength)
        st.write(" Accuracy (%) : " , Accuracy)
        st.write("Agility (%) : " , Agility)

    else:
        st.write("Reflexive Strength (%) : " , Non_reflexive)
        st.write(" Accuracy (%) : " ,  Non_Accuracy)
        st.write("Agility (%) : " , Non_Agility)

with col15:
    Red_1 = st.color_picker('Sleep Recovery | Executive Functions | Attention |', "#F90000")
    Sleep_recovery = random.uniform(55,82)
    Non_sleep = random.uniform(45,62)
    Executive_functions = random.uniform(55,82)   
    Non_exective_functions = random.uniform(45,62)
    Attention = random.uniform(55,82)
    Non_Attention = random.uniform(45,62)

        
    if bai >=21 and bai < 38 : 
        st.write("Sleep Recovery (%) : " , Sleep_recovery)
        st.write(" Executive Functions (%) : " , Executive_functions)
        st.write("Attenttion (%) : " , Attention)

    else:
        st.write("Sleep Recovery (%) : " , Non_sleep)
        st.write(" Executive Functions (%) : " , Non_exective_functions)
        st.write("Attention (%) : " , Non_Attention)

with st.expander("Overview"):
    st.write("**BMI** ~ Focus Endurance | Reaction Time | Alertness |;",
    "**BMR** ~ Reflexive Strength | Accuracy | Agility | ; ",
    "**BAI**(Visceral Fat percentage) ~ Sleep Recovery | Executive Functions | Attention |;" ,
    "<**Colour Change Optional**>")

Cog_complete  = st.checkbox('Cognitive Performance Complete')
with col15:
    if Cog_complete :
        st.metric(label="Dashboard Usage", value ="100%", delta="20%",)

st.divider()
