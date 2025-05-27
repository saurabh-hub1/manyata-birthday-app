
import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Happy Birthday Manyata!", page_icon="🎉", layout="centered")

# Load image
img = Image.open("manyata.jpeg")
st.image(img, width=250)

# Title and intro
st.markdown("<h1 style='text-align: center; color: #d63384;'>Happy 21st Birthday, Manyata!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>From someone who loves you more than words can say.</h3>", unsafe_allow_html=True)

# Love letter
if st.button("Read Your Love Letter"):
    poem = '''
    **To the One Who Lights My World**

    Today’s your day, my love, my light,  
    A star that makes my dark skies bright.  
    With every smile, with every touch,  
    You show me love, and oh, how much.

    Your laughter is my favorite song,  
    With you, my heart feels right, feels strong.  
    Each moment shared, both big and small,  
    You're the most precious gift of all.

    You bloom with grace, a rare delight,  
    More radiant than the moon at night.  
    No words can truly quite convey  
    The joy you bring me every day.

    So on your birthday, here’s my vow:  
    To cherish you then, now, and how—  
    Forevermore, I’ll hold you dear,  
    With love that grows each passing year.
    '''
    st.markdown(poem)

# Quiz
st.markdown("## Let's Play a Birthday Quiz!")

questions = {
    "What is Manyata’s favorite color?": "pink",
    "Which song makes you think of her?": "perfect",
    "How old is she turning today?": "21",
    "Who loves her the most?": "me"
}

score = 0
for question, correct_answer in questions.items():
    user_answer = st.text_input(question, key=question).lower().strip()
    if user_answer and user_answer == correct_answer:
        score += 1

if st.button("Submit Quiz"):
    st.success(f"You got {score}/{len(questions)} right! Perfect match – just like you two!")
    st.balloons()
