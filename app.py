import streamlit as st
import qrcode as qr

st.title("🔳 Scanova QR Generator")

# page icon and title
st.set_page_config(
    page_title= "Scanova QR Generator",
    page_icon= "🔳"
)

url = st.text_input("Enter the URL")

# Download Type
qr_type = st.selectbox("Download Type: ", ("png", "jpg", "jpeg"))

# when someone clicks the button the code inside will run
if st.button("Generate QR"):
    
    if url:

        # create QR
        make_qr = qr.make(url)

        # save QR
        if (qr_type == "png"):
            make_qr.save("qr_code.png")
        elif (qr_type == "jpg"):
            make_qr.save("qr_code.jpg")
        elif (qr_type == "jpeg"):
            make_qr.save("qr_code.jpeg")

        st.success("QR Code Generated!")

        # Display QR

        if (qr_type == "png"):
            st.image("qr_code.png", caption= "Your QR Code")
        elif (qr_type == "jpg"):
            st.image("qr_code.jpg", caption= "Your QR Code")
        elif (qr_type == "jpeg"):
            st.image("qr_code.jpeg", caption= "Your QR Code")

        # download button
        if (qr_type == "png"):
            with open("qr_code.png", "rb") as file:
                st.download_button(
                    label="Download QR Code",
                    data=file,
                    file_name="qr_code.png",
                     mime="image/png"
                )
        elif (qr_type == "jpg"):
            with open("qr_code.jpg", "rb") as file:
                st.download_button(
                    label="Download QR Code",
                    data=file,
                    file_name="qr_code.jpg",
                    mime="image/jpg"
                )
        elif (qr_type == "jpeg"):
                with open("qr_code.jpeg", "rb") as file:
                    st.download_button(
                        label="Download QR Code",
                        data=file,
                        file_name="qr_code.jpeg",
                        mime="image/jpeg"
                )
    else:
        st.warning("Please enter a URL first")        