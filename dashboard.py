import streamlit as st
from edgar import set_identity, Company


def main():
    st.title("EDGAR Company Lookup Tool")

    # Section 1: Set Identity
    st.header("1. Set Your EDGAR Identity")
    email = st.text_input("Enter your email address for EDGAR access:")

    if email:
        try:
            set_identity(email)
            st.success(f"Identity set successfully with email: {email}")
        except Exception as e:
            st.error(f"Error setting identity: {str(e)}")

    # Section 2: Company Lookup
    st.header("2. Lookup Company Information")
    ticker = st.text_input("Enter a company ticker symbol (e.g., AAPL):").upper()

    if ticker:
        try:
            company = Company(ticker)
            st.subheader(f"Company Information for {ticker}")
            st.write(f"**Company Name:** {company.name}")

            # You can add more company information here if needed
            # st.write(f"**CIK:** {company.cik}")
            # st.write(f"**Exchange:** {company.exchange}")

        except Exception as e:
            st.error(f"Error retrieving company information: {str(e)}")


if __name__ == "__main__":
    main()