import os
import streamlit as st

from src.helper import read_pickle_file, render_html,read_log_file
from src.utils import CONFIG, get_today_date

today_date = get_today_date()
log_file = f"./log/{today_date}_{CONFIG['log_file']}"
global_dict_path = f"{CONFIG['result']}{today_date}_{CONFIG['process_dict_flag']}"
global_dict = read_pickle_file(global_dict_path)
viz_html_file = f"{CONFIG['result']}{today_date}_{CONFIG['viz_html_file']}"
plot_file_path = f"{CONFIG['result']}{today_date}_actual_vs_predicted.png"

def display_status(topic, status):
    st.sidebar.write(f"**{topic}**")
    
    if status:
        st.sidebar.markdown('<p style="color:green;font-size:70px">&#10004;</p>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown('<p style="color:red;font-size:50px">&#10060;</p>', unsafe_allow_html=True)

topics = list(global_dict.keys())
statuses = list(global_dict.values())

st.set_page_config(layout="wide")

st.sidebar.title(today_date)

st.sidebar.title("Pipeline Monitoring Dashboard")
for topic, status in zip(topics, statuses):
    display_status(topic, status)

if not global_dict["data_pipeline"] or not global_dict["api"] or not global_dict["model_process"]:
    
    if st.button("View Log"):
        st.title("Log File Viewer")
        log_content = read_log_file(log_file)
        st.text(log_content)

st.title("Visualization")
if global_dict["data_pipeline"]:
    
    st.write("Click below buttons to visualize data:")
    if st.button("Visualize Data"):

        if os.path.exists(viz_html_file):
            html_content = render_html(viz_html_file)
            st.components.v1.html(html_content, height=5800)

if global_dict["model_process"]:
    if st.button("Test Result"):
        st.image(plot_file_path, caption="Test Result", use_column_width=True)



