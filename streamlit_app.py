import streamlit as st

# Initializing session state for global variables
if "sp" not in st.session_state:
    st.session_state.sp = {'indomie': 7500, 'rice': 10000, 'bread': 1000, 'hollandia': 9500}
    st.session_state.cp = {'indomie': 5500, 'rice': 8700, 'bread': 800, 'hollandia': 6900}
    st.session_state.sp_items_mrn = []
    st.session_state.cp_items_mrn = []
    st.session_state.sp_items_evn = []
    st.session_state.cp_items_evn = []
    st.session_state.sold = []

# Helper functions
def record_sale(shift, product, qty):
    try:
        sp_val = st.session_state.sp[product] * qty
        cp_val = st.session_state.cp[product] * qty
        if shift == "morning":
            st.session_state.sp_items_mrn.append(sp_val)
            st.session_state.cp_items_mrn.append(cp_val)
        else:
            st.session_state.sp_items_evn.append(sp_val)
            st.session_state.cp_items_evn.append(cp_val)
        st.session_state.sold.append(product)
        return True
    except KeyError:
        return False

def calculate_sales(shift):
    if shift == "morning":
        return sum(st.session_state.sp_items_mrn), sum(st.session_state.cp_items_mrn)
    else:
        return sum(st.session_state.sp_items_evn), sum(st.session_state.cp_items_evn)

def calculate_profit(shift):
    sales, cost = calculate_sales(shift)
    return sales - cost

def calculate_tips(shift):
    sales, _ = calculate_sales(shift)
    return 0.02 * sales

def total_summary():
    total_sales = sum(st.session_state.sp_items_mrn) + sum(st.session_state.sp_items_evn)
    total_cost = sum(st.session_state.cp_items_mrn) + sum(st.session_state.cp_items_evn)
    return total_sales, total_cost, total_sales - total_cost, 0.02 * total_sales

# UI starts here
st.sidebar.title("Inventory Role Menu")
role = st.sidebar.radio("Who are you?", ["Manager", "Morning Shift", "Evening Shift"])

st.title("🛒 Ikedi Jacobs Inventory Management System")

if role == "Manager":
    st.subheader("Manager Dashboard")
    option = st.selectbox("Choose an Option", ["View Total Sales", "View Total Salary", "View Total Profit", "View Total Tips"])

    if option == "View Total Sales":
        total_sales, total_cost, _, _ = total_summary()
        st.write(f"🧾 **Total Sales:** ₦{total_sales}")
        st.write(f"📦 **Total Cost:** ₦{total_cost}")

    elif option == "View Total Salary":
        mrn_rate = st.number_input("Morning Rate", min_value=0.0)
        mrn_hours = st.number_input("Morning Hours", min_value=0.0)
        evn_rate = st.number_input("Evening Rate", min_value=0.0)
        evn_hours = st.number_input("Evening Hours", min_value=0.0)
        if st.button("Calculate Salary"):
            total_salary = (mrn_rate * mrn_hours) + (evn_rate * evn_hours)
            st.write(f"💸 **Total Salary for Today:** ₦{total_salary}")

    elif option == "View Total Profit":
        st.write(f"💰 **Total Profit:** ₦{calculate_profit('morning') + calculate_profit('evening')}")

    elif option == "View Total Tips":
        st.write(f"🎁 **Total Tips:** ₦{calculate_tips('morning') + calculate_tips('evening')}")

else:
    shift = "morning" if role == "Morning Shift" else "evening"
    st.subheader(f"{role} Dashboard")
    option = st.selectbox("Select Action", ["Enter Sales", "View Sales", "Add Product", "Calculate Salary", "View Profit", "View Tips"])

    if option == "Enter Sales":
        product = st.selectbox("Product", list(st.session_state.sp.keys()))
        qty = st.number_input("Quantity", min_value=1)
        if st.button("Submit Sale"):
            if record_sale(shift, product, qty):
                st.success(f"{qty} units of {product} sold.")
            else:
                st.error("Product not found in inventory.")

    elif option == "View Sales":
        sales, cost = calculate_sales(shift)
        st.write(f"🧾 **Sales:** ₦{sales}")
        st.write(f"📦 **Cost:** ₦{cost}")
        st.write(f"📃 Products Sold: {', '.join(st.session_state.sold)}")

    elif option == "Add Product":
        name = st.text_input("Product Name").lower()
        sp = st.number_input("Selling Price", min_value=0)
        cp = st.number_input("Cost Price", min_value=0)
        if st.button("Add Product"):
            st.session_state.sp[name] = sp
            st.session_state.cp[name] = cp
            st.success(f"{name} added to inventory.")

    elif option == "Calculate Salary":
        rate = st.number_input("Hourly Rate", min_value=0.0)
        hours = st.number_input("Hours Worked", min_value=0.0)
        if st.button("Calculate"):
            st.write(f"💵 **Your salary today is ₦{rate * hours}**")

    elif option == "View Profit":
        st.write(f"💰 **Profit:** ₦{calculate_profit(shift)}")

    elif option == "View Tips":
        st.write(f"🎁 **Tips:** ₦{calculate_tips(shift)}")