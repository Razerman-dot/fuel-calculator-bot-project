import streamlit as st

# Load custom CSS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

st.title("⛽ Fuel Expense & Distance Calculator")
st.write("Easily calculate your weekly and monthly transport or fuel cost!")

mode = st.radio("Choose calculation mode:", [
                "Distance (for car owners)", "Fare (for public transport users)"])

if mode == "Distance (for car owners)":
    days = st.number_input(
        "How many days do you travel in a week?", min_value=1, max_value=7, value=5)
    km_per_litre = st.number_input(
        "Enter your car's fuel efficiency (km per litre):", min_value=1.0, value=15.0)
    fuel_price = st.number_input(
        "Enter current fuel price per litre (₦):", min_value=1.0, value=700.0)

    total_cost = 0.0
    st.subheader("Enter your daily distances:")
    for i in range(int(days)):
        distance = st.number_input(
            f"Day {i+1} distance (km):", min_value=0.0, value=10.0, key=f"day{i}")
        fuel_used = distance / km_per_litre
        cost = fuel_used * fuel_price
        total_cost += cost

    if st.button("Calculate Total"):
        weekly = total_cost
        monthly = weekly * 4
        st.success(f"Total transport this week = ₦{weekly:,.2f}")
        st.info(f"Estimated monthly transport = ₦{monthly:,.2f}")
        st.caption("💡 Remember to plan ahead and budget wisely!")

elif mode == "Fare (for public transport users)":
    daily_fare = st.number_input(
        "Enter your daily transport cost (₦):", min_value=0.0, value=1000.0)
    days = st.number_input(
        "How many days do you travel in a week?", min_value=1, max_value=7, value=5)

    if st.button("Calculate Total"):
        weekly = daily_fare * days
        monthly = weekly * 4
        st.success(f"Total transport this week = ₦{weekly:,.2f}")
        st.info(f"Estimated monthly transport = ₦{monthly:,.2f}")
        st.caption("🚍 Stay smart — track your fares and plan ahead!")
