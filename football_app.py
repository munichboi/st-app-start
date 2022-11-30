import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
warnings.filterwarnings('ignore')

ks=pd.read_csv("key_stats.csv")
gl=pd.read_csv("goals.csv")
dfn=pd.read_csv("defending.csv")
atkg=pd.read_csv("attacking.csv")
gk=pd.read_csv("goalkeeping.csv")
dsp=pd.read_csv("disciplinary.csv")
atm=pd.read_csv("attempts.csv")
dis=pd.read_csv("distributon.csv")

st.write("hello")
with st.sidebar:
    selectfile = st.radio(
        "Choose a CSV file",
        FILES.keys()
    )
    st.write(selectfile)

selectedfile = FILES[selectfile]

st.title(selectfile)
if selectfile == "ENB2012":
    df = pd.read_excel(selectedfile)
else:
    df = pd.read_csv(selectedfile)
st.dataframe(df)

if selectfile == "natural2021":
    st.title("แหล่งธรรมชาติของประเทศไทย")
    
    st.header("แสดงข้อมูลจำนวนตามการแบ่งกลุ่ม")
    option = st.selectbox('เลือกชื่อ Column', df.columns)
    st.write('คุณเลือก:', option)
    fig, ax = plt.subplots(figsize=(10,5))
    sns.countplot(x=df[option])
    st.pyplot(fig)

    st.header("แสดงความสัมพันธ์ของแหล่งธรรมชาติ")
    option_x = st.radio(
    'เลือกแกน X',
    ["ประเภทแหล่งธรรมชาติ", "จังหวัด", "ภาค"])
    option_y = st.radio(
    'เลือกแกน Y',
    ["ประเภทแหล่งธรรมชาติ", "จังหวัด", "ภาค"])

    fig, ax = plt.subplots(figsize=(10,5))
    sns.scatterplot(x=option_x, y=option_y,
                    linewidth=0,
                    data=df, hue="ระดับความสำคัญ")
    st.pyplot(fig)

    fig = sns.displot(data=df, x="ประเภทแหล่งธรรมชาติ", hue="ระดับความสำคัญ")
    st.pyplot(fig)

    sns.set_theme(style="darkgrid")

    fig = sns.lineplot(x="ประเภทแหล่งธรรมชาติ", y="จังหวัด",
             hue="ภาค", style="ระดับความสำคัญ",
             data=df)
else:
    pass