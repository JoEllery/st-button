
import streamlit as st
import numpy as np


# First, set the title of the page. This is what will show up on your browser tab.
# We do this by calling the set_page_config method and telling it what title we want to use.
st.set_page_config(page_title="Lucky Number Generator")

# Next, we'll write a title, which will be visible in the web app.
st.header("Lucky Number Generator")

# Next, a small explanation of what the app does:
st.write("Click the button below to get your lucky number for the day!")

# Now, we tell the app what to do when it recieves input.
# The button returns a boolean (true) when clicked. So if the button is clicked...
if st.button("Get my lucky number!"):

  # Print a random lucky number!
  lucky_num = np.random.randint(low=0, high=100)
  st.write("Your lucky number is: " + str(lucky_num))

