import streamlit as st

st.title("📋 Smart Habit Tracker")
st.divider()

st.html("""
<style>
/* Positive habits */
.st-key-positive_habits_box {
    background-color: #ffff;
    padding: 20px !important;
    border-radius: 30px !important;
}

/* Negative habits */
.st-key-negative_habits_box {
    background-color: #ffff;
    padding: 20px !important;
    border-radius: 30px !important;
}

/* Inner containers */
.st-key-positive_habits_box [data-testid="stVerticalBlock"],
.st-key-negative_habits_box [data-testid="stVerticalBlock"] {
    background-color: #ffff;
}
</style>
""")

positive_habits= ["🏋️‍♀️Workout", "👩‍💻Code", "📚Study"]
negative_habits= ["📺Watch youtube", "🎮Game"]

col1, col2= st.columns([6, 6])

with col1:
    with st.container(key= "positive_habits_box"):
        with st.container(border= True):
            st.subheader("Positive Habits")
            with st.container(border=True):
                st.markdown(
                    """
                    <style>
                    [data-baseweb="checkbox"] [data-testid="stWidgetLabel"] p {
                        font-size: 1.2rem; 
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                for i in positive_habits:
                    st.checkbox(f"**{i}**")
                    st.divider()

st.divider()

with col2:
    with st.container(key= "negative_habits_box"):
        with st.container(border= True):
            st.subheader("Negative Habits")
            with st.container(border=True):
                st.markdown(
                    """
                    <style>
                    [data-baseweb="checkbox"] [data-testid="stWidgetLabel"] p {
                        font-size: 1.2rem; 
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                for i in negative_habits:
                    st.checkbox(f"**{i}**")
                    st.divider()

progress= st.button("📶 Check out progress")

if progress:
    st.switch_page("pages/progress.py")