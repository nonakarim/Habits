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

if "positive_habits_values" not in st.session_state:
    st.session_state.positive_habits_values = [False] * len(positive_habits)
if "count_positive_done" not in st.session_state:
    st.session_state.count_positive_done= 0

if "negative_habits_values" not in st.session_state:
    st.session_state.negative_habits_values = [False] * len(negative_habits)
if "count_negative_done" not in st.session_state:
    st.session_state.count_negative_done= 0


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
                for index, habit in enumerate(positive_habits):
                    key = f"positive_habit_{index}"

                    if key not in st.session_state:
                        st.session_state[key] = st.session_state.positive_habits_values[index]

                    st.checkbox(f"**{habit}**", key=key)

                    st.session_state.positive_habits_values[index] = st.session_state[key]

                    st.divider()

                st.session_state.count_positive_done = sum(st.session_state.positive_habits_values)

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
                for index, habit in enumerate(negative_habits):
                    key = f"negative_positive_habit_{index}"

                    if key not in st.session_state:
                        st.session_state[key] = st.session_state.negative_habits_values[index]

                    st.checkbox(f"**{habit}**", key=key)

                    st.session_state.negative_habits_values[index] = st.session_state[key]

                    st.divider()

                st.session_state.count_negative_done = sum(st.session_state.negative_habits_values)


progress= st.button("📶 Check out progress")

if progress:
    st.switch_page("pages/progress.py")