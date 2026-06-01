import streamlit as st

# قاعدة بيانات محلية (تم إدراج القائمة التي زودتني بها)
JAPAN_BINS = {
    "377783": "American Express Japan",
    "453450": "Visa Credit",
    "454153": "Visa Credit",
    "454294": "Visa Credit",
    "489784": "Visa Credit",
    "490714": "CITI CARDS JAPAN (Classic)",
    "490715": "CITI CARDS JAPAN (Gold)",
    "498001": "Visa Credit",
    "520867": "Mastercard Credit",
    "525013": "Mastercard Credit",
    "530232": "Mastercard Credit",
    "533491": "Mastercard Credit"
}

st.title("محول بيانات السجلات")
st.title("برمجة: علي يحيى")

input_data = st.text_area("ألصق البيانات هنا:", height=200)

if st.button("تحويل وتصنيف"):
    if input_data:
        lines = input_data.strip().split('\n')
        all_results = []
        japanese_results = []
        
        for line in lines:
            if '|' in line:
                parts = line.split('|')
                try:
                    card_num = parts[0]
                    expiry = parts[1].split('/')
                    month = expiry[0]
                    year = "20" + expiry[1]
                    cvv = parts[2]
                    
                    formatted_line = f"{card_num}|{month}|{year}|{cvv}"
                    all_results.append(formatted_line)
                    
                    # الفحص يعتمد الآن فقط على القائمة المحلية
                    bank_name = JAPAN_BINS.get(card_num[:6])
                    if bank_name:
                        japanese_results.append(f"{formatted_line} | {bank_name}")
                        
                except:
                    continue
        
        st.subheader(f"النتائج الكاملة ({len(all_results)}):")
        st.code("\n".join(all_results))
        
        st.subheader(f"البنوك اليابانية المكتشفة ({len(japanese_results)}):")
        if japanese_results:
            st.code("\n".join(japanese_results))
        else:
            st.info("لم يتم العثور على سجلات تطابق القائمة المحلية.")
