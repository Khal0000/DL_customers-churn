import streamlit as st
import requests

### Set page 
st.set_page_config(
    page_title="Khalisul_Akbar-Batch 10",
    page_icon="📉",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://github.com/Khal0000",
        'About': "# This is my first dashboarb!!!"
    }
)

st.markdown("<h1 style='text-align: center; color:  #ff957f ;'>Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("""<hr style="height:10px;border:none;color:#ff957f;background-color:#333;" /> """, unsafe_allow_html=True) 


st.sidebar.image("output-seomagnifier(3).png", width=300)
# st.sidebar.markdown("""<hr style="height:0px ; border:none ; color:#ff957f ; background-color:#333;" /> """, unsafe_allow_html=True)

st.sidebar.subheader('Demograpic :')
gender = st.sidebar.selectbox("Gender", ["Male","Female"])
age = st.sidebar.slider("Age", 0, 130, 0)

seniorcitizen = st.sidebar.selectbox("Older than 65 Yo ? (Y : 1 , N :0)", ["1","0"])  # Needed
partner = st.sidebar.selectbox("Marrried ? ", ["Yes","No"])  # Needed
dependent = st.sidebar.selectbox("Lives with any Dependents ?", ["Yes","No"])  # Needed

st.sidebar.write('---------------------------------------------------\n\n\n')
st.sidebar.subheader('Services :')

tenure = st.sidebar.slider("Tenure (in month)", 0, 100, 0) #Needed

phone_serv = st.sidebar.selectbox("Phone Service", ["Yes","No"])
internet_serv = st.sidebar.selectbox("Internet Service", ["Yes","No"])

online_security = st.sidebar.selectbox("Online Security", ["Yes","No"])  # Needed
tech_support = st.sidebar.selectbox("Technical Support", ["Yes","No"])  # Needed
contract = st.sidebar.radio("Contract Type", ["Month-to-month", "One year", "Two year"])  # Needed
paperless = st.sidebar.selectbox("Paperless billing", ["Yes","No"])  # Needed

st.sidebar.write('---------------------------------------------------\n\n\n')
st.sidebar.subheader('Payment :')

payment = st.sidebar.radio("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)",
 "Credit card (automatic)"])  # Needed
monthly_charge = st.sidebar.number_input("Monthly Charge", 0.0, 1000.0, 0.0) #Needed
Total_charge = st.sidebar.number_input("Total Charge", 0.0, 100000.0, 0.0) #Needed
st.sidebar.write('---------------------------------------------------\n\n\n')

submit = st.sidebar.button("Predict")

# inference
data = {"SeniorCitizen" : seniorcitizen,
         "Partner" : partner,
         "Dependents" : dependent, 
         "tenure" : tenure,
         "OnlineSecurity" : online_security,
         "TechSupport" : tech_support,
          "Contract" : contract,
          "PaperlessBilling" : paperless,
          "PaymentMethod" : payment,
          "MonthlyCharges" : monthly_charge,
           "TotalCharges" : Total_charge}

URL = "https://h8-kbackend.herokuapp.com/predict"

col1, col2 = st.columns([2, 2])

with col1:
    st.image("pngegg.png", width=300)

    # submit = st.button("Predict")
    
with col2:
    # komunikasi
    st.markdown("<h3 style='text-align: center; color:  #34eb95 ;'>What is Churn Rate ?</h3>", unsafe_allow_html=True)

    st.write("Source : [Investopedia](https://www.investopedia.com/terms/c/churnrate.asp)")
    st.write(' According to (Frankenfeild, Jake.2022)  : The churn rate, also known as the rate of attrition or customer churn, is the rate at which customers stop doing business with an entity. It is most commonly expressed as the percentage of service subscribers who discontinue their subscriptions within a given time period.')




st.write('---------------------------------------------------')
st.markdown("<h3 style='text-align: left; color:  #34eb95 ;'>Advantages and Disadvantages of Churn Rate </h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left; color:  white ;'>Advantages :</h3>", unsafe_allow_html=True)
st.write("One of many advantages for a company to be able to predict the churn rate is that it provides clarity on how well the business is retaining customers, or in other word how good the quality of the service the business is providing, as well as its usefulness.")
st.markdown("<h5 style='text-align: left; color:  white ;'>Disadvantages :</h3>", unsafe_allow_html=True)
st.write("On the other hand the limitation of the churn rate is that it does not specify which types of customers are leaving.")
st.write('---------------------------------------------------')
# komunikasi
r = requests.post(URL, json=data)
res = r.json()
st.markdown("<h3 style='text-align: left; color:  #34eb95 ;'>Prediction Result : </h3>", unsafe_allow_html=True)
st.write('---------------------------------------------------')
if res['code'] == 200 and submit:
    # st.subheader('Your Result is :')
    st.markdown(f"<h6 style='text-align: left; color: white ; font-size: 130;'>From the provided information, the model predict that the customer will probably :</h6>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: #ff957f; font-size: 100px;'>{res['result']['classes']}</h3>", unsafe_allow_html=True)
 