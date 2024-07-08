import streamlit as st
import pandas as pd

# Load the DataFrame globally
df = pd.read_csv("Business.csv")

# Page for Know Product by Name
def Name():
    st.subheader("Product")
    product_names = df['Product_Name']
    selected_product = st.selectbox("Select a product:", product_names)
    selected_row = df[df['Product_Name'] == selected_product]

    if st.button("Show Product Data"):
        st.subheader(f"Product Details: {selected_product}")
        st.text(f"DP Price: {selected_row['DP Price'].values[0]}")
        st.text(f"MRP Price: {selected_row['MRP'].values[0]}")

    if st.button("Show Full Details"):
        st.write(selected_row)

# Page for Know Product by Code
def Code():
    st.subheader("Product")
    product_ids = df['Product_Id']
    selected_product = st.selectbox("Select a Product:", product_ids)
    selected_row = df[df['Product_Id'] == selected_product]

    if st.button("Show Product Data"):
        st.subheader(f"Product Details: {selected_product}")
        st.text(f"DP Price: {selected_row['DP Price'].values[0]}")
        st.text(f"MRP Price: {selected_row['MRP'].values[0]}")

    if st.button("Show Full Details"):
        st.write(selected_row)

# Main option page
def option_page():
    st.title("OPTIONS")
    option = st.radio("Choose an option:", ["Name", "Code"])

    if option == "Name":
        Name()
    elif option == "Code":
        Code()

# Main function to run the app
def main():
    option_page()

if __name__ == "__main__":
    main()

