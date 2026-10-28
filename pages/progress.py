import streamlit as st
from habits import positive_habits
from habits import negative_habits

st.title("📋 Smart Habit Tracker")
st.divider()

st.progress(
    st.session_state.count_positive_done / len(positive_habits),
    text=f"{st.session_state.count_positive_done} / {len(positive_habits)} positive habits completed"
)

st.progress(
    st.session_state.count_negative_done / len(negative_habits),
    text=f"{st.session_state.count_negative_done} / {len(negative_habits)} negative habits completed"
)

st.divider()
habits= st.button("🌱 Check out habits")

if habits:
    st.switch_page("habits.py")