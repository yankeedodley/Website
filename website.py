# import module
import streamlit as st
import random

# Title
st.title("Hi!")

st.header("Welcome to the ideas generator!")

if st.checkbox("Stuff we might delete"):
    if st.checkbox("The blog."):
        st.write("Creative block is a common experience for people of all creative disciplines. It's the feeling of being stuck, unable to come up with new ideas or produce your best work.")
        st.write('In this blog, we dicided to interview our friend Chunny, who recently experienced creative block.')
        st.write('Us: "So Chunny, how did creative block feel like?"')
        st.write('Chunny: "Creative block really sucks. Its like you cant think of anything. Your brain is basically dead."')
        st.write('Us: "What made you get creative block?"')
        st.write('Chunny: "Our art teacher told us to paint something, and I couldnt think of any good ideas."')
        st.write('Us: "How did you overcome it?"')
        st.write('Chunny: "I was lucky enough to have a friend who helped me. They made a website that helps people with creative block."')
        st.write('"Its great!" He says "I can think again!"')

topic = None
topics = None
topic = st.selectbox("Please select one topic to generate ideas on:",
    ['Painting', 'Music' , 'Sculptures'])

if st.button("Submit"):
    # Generate a list of unique random integers between 1 and 5
    random_numbers = random.sample(range(1, 6), 3)
    
    st.subheader("Here's some ideas:")
    if topic == "Painting":
        topics = ["Nature", "Self portrait", "Vehicles", "Abstract", "Random Paint spashes"]
        for r in random_numbers:
            st.write(topics[r - 1])

    elif topic == "Music":
        topics = ["Classical", "Fast and hard", "Slow and calming", "Start playing on istrument, Write It down", "Stuff"]
        for r in random_numbers:
            st.write(topics[r - 1])

    elif topic == "Sculptures":
        topics = ["Nature", "Humans", "Objects", "start sqishing clay balls", "Thats kinda sus"]
        for r in random_numbers:
            st.write(topics[r - 1])

    else:
        topics = ["Videogames", "Busting myths", "Try not to laugh", "I", "J"]
        
        for r in random_numbers:
            st.write(topics[r - 1])

    st.write("For more ideas, please search", topic, "on google.")
    st.subheader("Don't worry if your topic isn't perfect. Just try your best.")
st.header("How to come up with your own ideas:")
st.write("Step one: Think about what your latest peices are. What do you like?")
st.write("Step two: Write the things down.")
st.write("Step three: Make a picture related to the word.")