# import streamlit as st
# import pandas as pd 
# import numpy as np 

# # top most title
# st.title("E-commerce  web browser")
# st.write("today i am learning the streamlit app")

# st.title("store  web browser")
# st.write("today in my store i have lots of the items")

# name = st.chat_input("your name is ")
# st.write(f"{name} Aditya singh is with u")


# list_1=[x for x in range(10)]
# list_2=[x**2 for x in range(10)]
# list_3=[x**3 for x in range(10)]
# list_4=[x**4 for x in range(10)]
# df=pd.DataFrame({'num':list_1,'square_num':list_2,'cube_num':list_3,'quad_num':list_4})



# st.write("i have analysis of the number")
# st.write(df)


# st.dataframe(df, hide_index=True)



# st.line_chart(df)









import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Hello Streamlit")

## Diplay a Simple Text
st.write("This is a imple text")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)


##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data) 