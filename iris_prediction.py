# yes done by me and gpt 

import streamlit as st
import pandas as pd 
import numpy as np

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target
target_names = iris.target_names

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])



# SESSION STATE INITIALIZATION  
if 'name' not in st.session_state:
    st.session_state.name = None
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
st.set_page_config(page_title="Iris Species Predictor ", page_icon="🌸")
#  GREETING FORM  
if st.session_state.name is None:
    st.title("🌸 Iris Species Predictor")
    
    with st.container():
        st.markdown("""
        ### Welcome to the Botanical AI Lab
        This intelligent system uses Machine Learning to identify Iris flower species 
        based on the precise dimensions of their sepals and petals.
        """)
        
        with st.form("greet_form"):
            name_input = st.text_input("Enter your name to start the analysis:")
            submit_name = st.form_submit_button("Launch Predictor →")
            
            if submit_name and name_input:
                st.session_state.name = name_input
                st.rerun()
            elif submit_name and not name_input:
                st.warning("Please provide a name to personalize your experience.")

# MAIN APP ---
else:
    # HEADER & GREETING  
    st.title("🌸 Iris Species Predictor")
    
    # Professional Greeting Message
    with st.chat_message("assistant", avatar="🌿"):
        st.write(f"**Hello, {st.session_state.name}!** 👋")
        st.write("I'm ready to help you identify these species. This model analyzes the leaf-like structures (sepals) and the inner petals to give you a precise classification.")

    # Logout option in sidebar
    st.sidebar.title("User Profile")
    st.sidebar.info(f"Logged in as: {st.session_state.name}")
    if st.sidebar.button("Exit / Change User"):
        st.session_state.name = None
        st.session_state.submitted = False
        st.rerun()

    # 
    if not st.session_state.submitted:
        st.header("Predict Classification")
        
        with st.form("prediction_form"):
            st.write("Adjust the sliders to match your flower's measurements:")
            
            col1, col2 = st.columns(2)
            with col1:
                sl = st.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
                sw = st.slider("Sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
            with col2:
                pl = st.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
                pw =  st.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))
            
            if st.form_submit_button("Run Classification Analysis"):
                st.session_state.user_data = [[sl, sw, pl, pw]]
                st.session_state.submitted = True
                st.rerun()

    else:
        # THE RESULTS
        st.header("Prediction Result")
        input_data = st.session_state.user_data
        prediction = model.predict(input_data)
        predicted_name = target_names[prediction[0]].capitalize()
        # Result Display
        st.success(f"### Identification Complete: **{predicted_name}**")
        st.markdown(f"**{st.session_state.name}**, based on the dimensions provided, the model is confident this is an *Iris {predicted_name}*.")

        # Show the metrics summary
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Sepal L", f"{input_data[0][0]} cm")
        col2.metric("Sepal W", f"{input_data[0][1]} cm")
        col3.metric("Petal L", f"{input_data[0][2]} cm")
        col4.metric("Petal W", f"{input_data[0][3]} cm")
        st.balloons()
        st.divider()
        if st.button("🔄 Restart for New Flower"):
            st.session_state.submitted = False
            st.rerun()








# little help from gpt




# import streamlit as st
# import pandas as pd 

# from sklearn.datasets import load_iris
# from sklearn.ensemble import RandomForestClassifier


# iris=load_iris()
# iris_data=iris.data
# iris_target=iris.target
# target_names=iris.target_names

# df=pd.DataFrame(iris_data,columns=iris.feature_names)
# df["species"]=iris_target




# model=RandomForestClassifier()
# model.fit(df.iloc[:,:-1],df['species'])

# # This keeps track of whether to show the form or the result
# if 'submitted' not in st.session_state:
#     st.session_state.submitted = False
# if 'user_data' not in st.session_state:
#     st.session_state.user_data = None

# if "name" not in st.session_state:
#     st.session_state.name=None



# if st.session_state.name is None:
#     st.title("Welcome to the Iris Lab 🌿")
#     with st.form("greet_form"):
#         name=st.text_input("Please enter your name to begin:")
#         submit_button=st.form_submit_button("Enter App")

#         if submit_button and name:
#             st.session_state.name = name
#             st.rerun()
#         elif submit_button and not name:
#             st.warning("please enter the name")
# else:
    
#     st.title("🌸 Iris Species Predictor")
#     st.markdown("this model predict the species using leaves dimension spale and petal")
#     with st.expander("Explore the Data 🔍"):
#         st.title(f"Hello, {st.session_state.name}! 👋")
#         st.markdown(f"welcome to Iris Species Predictor ")
#         df['species_name']=target_names[iris_target]
#         st.write("Ye dataset 3 types ke Iris flowers ko differentiate karta hai.")
#         unique_samples_df = df.groupby('species').head(1)
#         st.dataframe(unique_samples_df)
#         # Join the list into a single string separated by ", "
#         formatted_names = ", ".join(target_names)
#         st.markdown(f"We will predict: **{formatted_names}**")



#     # Create the form
#     if not st.session_state.submitted:
#         st.header("Predict Classification")
#         with st.form("prediction_form"):
#             st.write("Adjust the features to make a prediction:")
            
#             col1, col2 = st.columns(2)
#             with col1:
#                 sl = st.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
#                 sw = st.slider("Sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
#             with col2:
#                 pl = st.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
#                 pw = st.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))
            
#             submitted = st.form_submit_button("Predict")

#             if submitted:
#                 st.session_state.user_data = [[sl, sw, pl, pw]]
#                 st.session_state.submitted = True
#                 st.rerun() # Refresh to swap the UI immediately

#     else:
#         st.header("Prediction Result")
#         input_data = st.session_state.user_data
        
#         prediction = model.predict(input_data)
#         predicted_name = target_names[prediction[0]]    
        
#         st.success(f"### Prediction: **{predicted_name.upper()}**")
#         st.markdown(f"The **{predicted_name}** has the following dimensions:")
        
#         col1, col2, col3, col4 = st.columns(4)
#         col1.metric("Sepal L", input_data[0][0])
#         col2.metric("Sepal W", input_data[0][1])
#         col3.metric("Petal L", input_data[0][2])
#         col4.metric("Petal W", input_data[0][3])
        
#         st.balloons()
        
#         st.divider()
        

#         if st.button("🔄 Make another prediction"):
#             st.session_state.submitted = False
#             st.rerun()
    

















# what i have written 






# # with st.form("prediction_form"):
# #     st.write("Adjust the features to make a prediction:")
# #     input_data=[[]]
# #     # Define the 4 sliders
# #     # Syntax: st.slider(label, min_value, max_value, default_value)
# #     col1,col2=st.columns(2)
    
# #     with col1:
# #         sepal_length = st.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
# #         sepal_width = st.slider("Sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
# #         input_data[0].append(sepal_length)
# #         input_data[0].append(sepal_width)
# #     with col2:
# #         petal_length = st.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
# #         petal_width = st.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))
# #         input_data[0].append(petal_length)
# #         input_data[0].append(petal_width)
# #     # Every form must have a submit button
# #     submitted = st.form_submit_button("Predict")

# # if submitted:
# #     prediction =model.predict(input_data)
# #     predicted_name=target_names[prediction[0]]    
# #     st.divider()
# #     # 1. Big bold result
# #     st.success(f"### Prediction: **{predicted_name.upper()}**")
# #     st.markdown(f"the {predicted_name} have leaves dimension of:")
# #     col1, col2, col3, col4 = st.columns(4)
# #     col1.metric("Sepal L", input_data[0][0])
# #     col2.metric("Sepal W", input_data[0][1])
# #     col3.metric("Petal L", input_data[0][2])
# #     col4.metric("Petal W", input_data[0][3])
# #     st.balloons() 





