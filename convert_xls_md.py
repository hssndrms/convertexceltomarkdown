import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Excel → Markdown Dönüştürücü",
    page_icon="🙃",  # Emoji kullanabilir
    layout="centered"
)

st.title("Excel → Markdown Dönüştürücü")

# Checkbox: İlk satır başlık mı?
has_header = st.checkbox("İlk satır başlık olarak kullanılsın", value=True)

# Kullanıcının veri girişi
input_data = st.text_area("Excel'den kopyaladığınız veriyi buraya yapıştırın:")

convert = st.button("Dönüştür",icon=":material/table_convert:")

if convert or input_data:
    if input_data is None or input_data.strip() == "":
        st.error("Önce tablo verisi yapıştırın")
        st.stop()
    try:
        # Satırları ayır
        rows = [row.split('\t') for row in input_data.splitlines()]

        if has_header:
            # İlk satır başlık olarak al
            header = rows[0]
            data_rows = rows[1:]
            df = pd.DataFrame(data_rows, columns=header)
        else:
            df = pd.DataFrame(rows)

        # Markdown formatına çevir
        markdown = df.to_markdown(index=False, tablefmt="github")

        # Markdown'u göster
        st.subheader("Markdown Formatı")
        st.code(markdown, language="markdown")

    except Exception as e:
        st.error(f"Hata oluştu: {e}")