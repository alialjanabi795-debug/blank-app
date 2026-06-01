import streamlit as st
import requests

st.title("محول بيانات السجلات")
st.title("برمجة: علي يحيى")

input_data = st.text_area("ألصق البيانات هنا:", height=200)

def get_bank_info(bin_number):
    try:
        # استخدام API عام لجلب معلومات البنك
        response = requests.get(f"https://lookup.binlist.net/{bin_number}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get('bank', {}).get('name', 'غير معروف'), data.get('country', {}).get('name', 'غير معروف')
    except:
        return "خطأ في الاتصال", "غير معروف"
    return "غير معروف", "غير معروف"

if st.button("تحويل وتصنيف ذكي"):
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
                    
                    # استعلام مباشر عن البنك
                    bank_name, country = get_bank_info(card_num[:6])
                    
                    if country == "Japan":
                        japanese_results.append(f"{formatted_line} | {bank_name}")
                        
                except:
                    continue
        
        st.subheader(f"النتائج الكاملة ({len(all_results)}):")
        st.code("\n".join(all_results))
        
        st.subheader(f"البنوك اليابانية فقط ({len(japanese_results)}):")
        if japanese_results:
            st.code("\n".join(japanese_results))
        else:
            st.info("لم يتم العثور على سجلات يابانية.")
