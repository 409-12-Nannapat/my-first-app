import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

vat = price * 0.07
 net_price = price - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
st.divider()
st.write("นางสาวนันท์นภัส คงสมแสง เลขที่ 12  ม.4/9")
