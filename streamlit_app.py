import streamlit as st
st.title(" محول بيانات البطاقات" \
"")
st.title(" " \
"برمجة علي يحيى")
st.title("شلونك ضرغام شخبارك")
st.write("االزك  البيانات هنا:")

# خانة إدخال البيانات
input_data = st.text_area("البيانات الأصلية:", height=200)

if st.button("تحويل"):
    if input_data:
        lines = input_data.split('\n')
        output_lines = []
        
        for line in lines:
            if '|' in line:
                parts = line.split('|')
                try:
                    card_num = parts[0]
                    expiry = parts[1].split('/')
                    month = expiry[0]
                    year = "20" + expiry[1]
                    cvv = parts[2]
                    output_lines.append(f"{card_num}|{month}|{year}|{cvv}")
                except IndexError:
                    continue
        
        # عرض النتيجة
        st.write("النتائج:")
        st.code("\n".join(output_lines))
    else:
        st.warning("يرجى لصق البيانات أولاً!")
