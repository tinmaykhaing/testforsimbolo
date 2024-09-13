import streamlit as st
st.image("flower-shop.PNG")
# App title
st.markdown("<h1 style='text-align: center; color: hotpink;'>Welcome to Khaing's Floral Shop</h1>", unsafe_allow_html=True)

# Section 1: Shop Introduction
st.markdown("<h2 style='color: green;'>Fresh Flowers Delivered to Your Doorstep</h2>", unsafe_allow_html=True)
st.write("We offer a wide selection of beautiful flowers for all occasions. "
         "Choose your favorite flowers, customize your order, and get them delivered fresh and on time.")

# Section 2: Flower Selection
st.markdown("<h3 style='color: purple;'>Choose Your Flowers</h3>", unsafe_allow_html=True)

# Flower options and their prices
st.write("Select your favorite flowers from our collection:")
roses = st.checkbox("Roses ($2.00 each)")
tulips = st.checkbox("Tulips ($3.00 each)")
sunflowers = st.checkbox("Sunflowers ($4.50 each)")
lilies = st.checkbox("Lilies ($5.00 each)")
daisies = st.checkbox("Daisies ($2.50 each)")

# Quantity input for each flower
rose_qty = tulip_qty = sunflower_qty = lily_qty = daisy_qty = 0
if roses:
    rose_qty = st.number_input("Number of Roses", min_value=1, step=1)
if tulips:
    tulip_qty = st.number_input("Number of Tulips", min_value=1, step=1)
if sunflowers:
    sunflower_qty = st.number_input("Number of Sunflowers", min_value=1, step=1)
if lilies:
    lily_qty = st.number_input("Number of Lilies", min_value=1, step=1)
if daisies:
    daisy_qty = st.number_input("Number of Daisies", min_value=1, step=1)

# Section 3: Order Details
st.markdown("<h3 style='color: blue;'>Order Details</h3>", unsafe_allow_html=True)
name = st.text_input("Enter your name")
address = st.text_input("Enter your delivery address")
delivery_date = st.date_input("Select a delivery date")
notes = st.text_area("Additional notes (e.g., special instructions)")
uploaded_file = st.file_uploader("If you have any specific desired flower boutique photo, please upload sample image below.", type=["jpg", "jpeg", "png", "pdf"])


# Section 4: Cart and Total
st.markdown("<h3 style='color: orange;'>Your Shopping Cart</h3>", unsafe_allow_html=True)
total_cost = (rose_qty * 2.50) + (tulip_qty * 1.80) + (sunflower_qty * 1.20) + (lily_qty * 3.00) + (daisy_qty * 1.00)

if roses or tulips or sunflowers or lilies or daisies:
    st.write(f"Roses: {rose_qty} , $2.50 for each")
    st.write(f"Tulips: {tulip_qty} , $1.80 for each")
    st.write(f"Sunflowers: {sunflower_qty} , $1.20 for each")
    st.write(f"Lilies: {lily_qty} , $3.00 for each")
    st.write(f"Daisies: {daisy_qty} , $1.00 for each")
    st.markdown(f"<h4 style='color: red;'>Total: ${total_cost:.2f}</h4>", unsafe_allow_html=True)
else:
    st.write("No items added yet.")

# Section 5: Place Order Button
if st.button("Place Order"):
    if name and address:
        st.success(f"Thank you for your order, {name}! Your flowers will be delivered to {address} on {delivery_date}.")
    else:
        st.error("Please complete all order details.")

st.sidebar.markdown("<h3 style='color: teal;'>Get in Touch</h3>", unsafe_allow_html=True)
st.sidebar.write("For inquiries or support, feel free to reach out to us:")
st.sidebar.write("Email: [support@floralshop.com](mailto:support@floralshop.com)")
st.sidebar.write("Phone: +95(9)123456789")

# Sidebar: Subscribe for Updates
st.sidebar.markdown("### Subscribe for Updates")
email = st.sidebar.text_input("Enter your email address to receive updates")
if st.sidebar.button("Subscribe"):
    if email:
        st.sidebar.success("Thank you for subscribing!")
    else:
        st.sidebar.error("Please enter a valid email address.")

# Sidebar: Social Media Links
st.sidebar.markdown("### Follow Us")
st.sidebar.write("[Facebook](https://www.facebook.com/floralshop)")
st.sidebar.write("[Instagram](https://www.instagram.com/floralshop)")
st.sidebar.write("[Telegram](https://telegram.com/floralshop)")

# Footer
st.write("---")
st.write("Thank You For Shopping With Us!")
