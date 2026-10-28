import streamlit as st

positive_habits = ["🏋️‍♀️Workout", "👩‍💻Code", "📚Study"]
negative_habits = ["📺Watch youtube", "🎮Game"]

if "count_positive_done" not in st.session_state:
    st.session_state.count_positive_done = 0

if "count_negative_done" not in st.session_state:
    st.session_state.count_negative_done = 0

positive_done = st.session_state.count_positive_done
negative_done = st.session_state.count_negative_done

st.title("📊 Your Progress")

st.subheader("Positive Habits")
st.progress(positive_done / len(positive_habits)و f"{positive_done} / 3 Negative Habits Completed")

st.subheader("Negative Habits")
st.progress(negative_done / len(negative_habits), f"{negative_done} / 2 Negative Habits Completed")


st.divider()
habits= st.button("🌱 Check out habits")

if habits:
    st.switch_page("habits.py")