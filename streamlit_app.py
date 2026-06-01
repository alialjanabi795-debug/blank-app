import streamlit as st
from binlookup import BinLookup

# إعداد الأداة
bin_api = BinLookup()

st.title("محول بيانات السجلات")
st.title("برمجة: علي يحيى")
st.write("أهلاً بك يا ضرغام، الأداة الآن تدعم التصنيف التلقائي الذكي.")

input_data = st.text_area("ألصق البيانات هنا:", height=200)

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
                    
                    # استعلام ذكي عبر binlookup
                    bin_info = bin_api.get(card_num[:6])
                    if bin_info and bin_info.country and bin_info.country.name == "Japan":
                        japanese_results.append(f"{formatted_line} | {bin_info.bank.name if bin_info.bank else 'Unknown Bank'}")
                        
                except Exception:
                    continue
        
        # عرض النتائج
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"النتائج الكاملة ({len(all_results)}):")
            st.code("\n".join(all_results))
            
        with col2:
            st.subheader(f"البنوك اليابانية فقط ({len(japanese_results)}):")
            if japanese_results:
                st.code("\n".join(japanese_results))
            else:
                st.info("لم يتم العثور على سجلات يابانية.")
    else:
        st.warning("يرجى لصق البيانات أولاً!")
