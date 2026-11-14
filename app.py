import streamlit as st

st.set_page_config(
    page_title="Smart Plant Watering Assistant",
    page_icon="🌱"
)

st.title("🌱 Smart Plant Watering Assistant")
st.write("Monitor your plant's soil moisture.")

plant = st.text_input("Enter Plant Name")

moisture = st.slider(
    "Soil Moisture (%)", 0, 100, 40
)

if st.button("Analyse"):
    st.subheader("Analysis Result")
    st.write("Plant:", plant)
    st.metric("Moisture", f"{moisture}%")

    if moisture < 30:
        st.error("Soil is Dry! Water the plant.")
    elif moisture < 60:
        st.warning("Soil moisture is Moderate.")
    else:
        st.success("Soil is Wet! No watering needed now.")
