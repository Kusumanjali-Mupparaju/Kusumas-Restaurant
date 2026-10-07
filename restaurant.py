import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Kusuma's Restaurant Bill Generator",
    page_icon="🍽️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff1eb, #ace0f9);
}

.main-title {
    text-align: center;
    color: #8B0000;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #555555;
    font-size: 18px;
    margin-bottom: 25px;
}

.bill-box {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
    margin-top: 20px;
}

.total-box {
    background: linear-gradient(90deg, #ff9966, #ff5e62);
    color: white;
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}

.item-box {
    background: #fff8f5;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
}

</style>
""", unsafe_allow_html=True)


# ---------------- RESTAURANT MENU ----------------
menu = {
    "🍕 Pizza": 250,
    "🍔 Burger": 150,
    "🍝 Pasta": 180,
    "🍟 French Fries": 100,
    "🥪 Sandwich": 120,
    "🍗 Chicken Biryani": 220,
    "🥗 Veg Biryani": 180,
    "🥤 Soft Drink": 60,
    "🍨 Ice Cream": 90,
    "☕ Coffee": 70
}


# ---------------- TITLE ----------------
st.markdown(
    "<div class='main-title'>🍽️ Kusuma's Restaurant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>✨ Restaurant Bill Generator ✨</div>",
    unsafe_allow_html=True
)


# ---------------- CUSTOMER DETAILS ----------------
st.subheader("👤 Customer Details")

customer_name = st.text_input(
    "Customer Name",
    placeholder="Enter customer name"
)


# ---------------- FOOD SELECTION ----------------
st.subheader("🍴 Select Your Food")

selected_items = []

for item, price in menu.items():

    col1, col2, col3 = st.columns([2.5, 1, 1])

    with col1:
        selected = st.checkbox(
            f"{item} - ₹{price}",
            key=f"select_{item}"
        )

    with col2:
        quantity = st.number_input(
            "Qty",
            min_value=1,
            max_value=10,
            value=1,
            step=1,
            key=f"qty_{item}"
        )

    with col3:
        if selected:
            item_total = price * quantity
            st.write(f"₹{item_total}")

            selected_items.append(
                (item, price, quantity, item_total)
            )


# ---------------- DISCOUNT & TAX ----------------
st.subheader("💰 Bill Settings")

col1, col2 = st.columns(2)

with col1:
    discount = st.number_input(
        "🏷️ Discount (%)",
        min_value=0.0,
        max_value=50.0,
        value=0.0,
        step=1.0
    )

with col2:
    tax = st.number_input(
        "💸 GST / Tax (%)",
        min_value=0.0,
        max_value=30.0,
        value=5.0,
        step=1.0
    )


# ---------------- GENERATE BILL ----------------
if st.button("🧾 Generate Bill", use_container_width=True):

    if len(selected_items) == 0:
        st.warning("⚠️ Please select at least one food item.")

    else:

        # Calculate subtotal
        subtotal = sum(
            item[3] for item in selected_items
        )

        # Calculate discount
        discount_amount = subtotal * discount / 100

        # Amount after discount
        discounted_amount = subtotal - discount_amount

        # Calculate tax
        tax_amount = discounted_amount * tax / 100

        # Grand total
        grand_total = discounted_amount + tax_amount


        # ---------------- BILL ----------------
        st.markdown(
            "<div class='bill-box'>",
            unsafe_allow_html=True
        )

        st.markdown("## 🧾 Kusuma's Restaurant Bill")

        if customer_name:
            st.write(f"**Customer:** {customer_name}")
        else:
            st.write("**Customer:** Guest")

        st.write("---")

        # Table header
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

        with col1:
            st.write("**Item**")

        with col2:
            st.write("**Price**")

        with col3:
            st.write("**Qty**")

        with col4:
            st.write("**Total**")


        # Display items
        for item, price, quantity, total in selected_items:

            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

            with col1:
                st.write(item)

            with col2:
                st.write(f"₹{price}")

            with col3:
                st.write(quantity)

            with col4:
                st.write(f"₹{total}")


        st.write("---")

        # Bill calculations
        col1, col2 = st.columns(2)

        with col1:
            st.write("Subtotal")
            st.write(f"Discount ({discount}%)")
            st.write(f"GST / Tax ({tax}%)")

        with col2:
            st.write(f"₹{subtotal:.2f}")
            st.write(f"- ₹{discount_amount:.2f}")
            st.write(f"+ ₹{tax_amount:.2f}")


        st.write("---")

        # Grand total
        st.markdown(
            f"""
            <div class='total-box'>
                💵 Grand Total: ₹{grand_total:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

        st.success("🎉 Thank you for visiting Kusuma's Restaurant!")


# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    "<center>🍴 Fresh Food • Great Taste • Happy Customers 🍴</center>",
    unsafe_allow_html=True
)