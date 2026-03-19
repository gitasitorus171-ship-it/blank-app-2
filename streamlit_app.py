# =============================
# STREAMLIT APP - FINAL MODERN BLUE APP
# =============================

import streamlit as st
import random

st.set_page_config(page_title="DPL Research Room", page_icon="📱", layout="wide")

# ===== SESSION STATE =====
if "data" not in st.session_state:
    st.session_state.data = {
        "Penelitian 1": {
            "Kuesioner": [],
            "Jurnal": [],
            "Teori Pendukung": [],
            "Olah Data SPSS": []
        },
        "Penelitian 2": {
            "Kuesioner": [],
            "Jurnal": [],
            "Teori Pendukung": [],
            "Olah Data SPSS": []
        }
    }

if "messages" not in st.session_state:
    st.session_state.messages = []

# ===== QUOTES AHLI =====
quotes = [
    "Hidup yang tidak diuji tidak layak dijalani. — Socrates",
    "Di tengah kesulitan terdapat kesempatan. — Albert Einstein",
    "Keunggulan adalah kebiasaan, bukan tindakan. — Aristoteles",
    "Segalanya terasa mustahil sampai selesai. — Nelson Mandela",
    "Perjalanan seribu mil dimulai dari satu langkah. — Lao Tzu",
    "Pengetahuan berbicara, tetapi kebijaksanaan mendengarkan. — Jimi Hendrix"
]

# ===== BLUE UI =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1e3a8a, #2563eb);
    color: white;
}
.card {
    background: white;
    color: black;
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 20px;
}
.title {
    font-size: 38px;
    font-weight: bold;
    text-align: center;
    color: white;
}
.quote {
    text-align: center;
    font-style: italic;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="title">📚 DPL Research Room</div>', unsafe_allow_html=True)
st.markdown(f'<div class="quote">"{random.choice(quotes)}"</div>', unsafe_allow_html=True)

# ===== NAVIGATION =====
menu = st.selectbox("Pilih Halaman", ["Home", "Penelitian 1", "Penelitian 2", "Chat"])

# ===== HOME =====
if menu == "Home":
    st.markdown("""
    <div class="card">
    <h3>Selamat Datang Ibu DPL</h3>
    <p>Ruang khusus untuk diskusi dan penyimpanan data research, i hope ibu like.</p>
    </div>
    """, unsafe_allow_html=True)

    # progress
    total = 0
    filled = 0
    for p in st.session_state.data.values():
        for sub in p.values():
            total += 1
            if sub:
                filled += 1

    progress = int((filled/total)*100) if total else 0
    st.progress(progress/100)
    st.write(f"Progress: {progress}%")

# ===== PENELITIAN =====
def halaman_penelitian(nama):
    st.markdown(f"## 📂 {nama}")

    for kategori in st.session_state.data[nama]:
        with st.expander(f"📁 {kategori}"):
            file = st.file_uploader(f"Upload ke {kategori}", key=nama+kategori)
            if file:
                st.session_state.data[nama][kategori].append(file.name)
                st.success("File ditambahkan")

            if st.session_state.data[nama][kategori]:
                for f in st.session_state.data[nama][kategori]:
                    st.write(f"📄 {f}")
            else:
                st.caption("Kosong")

# ===== ROUTING =====
if menu == "Penelitian 1":
    halaman_penelitian("Penelitian 1")

elif menu == "Penelitian 2":
    halaman_penelitian("Penelitian 2")

# ===== CHAT =====
elif menu == "Chat":
    st.markdown("## 💬 Diskusi")

    for msg in st.session_state.messages:
        st.markdown(f"<div class='card'><b>{msg['user']}</b><br>{msg['text']}</div>", unsafe_allow_html=True)

    msg = st.text_input("Pesan...")
    if st.button("Kirim"):
        if msg:
            st.session_state.messages.append({"user": "Mahasiswa", "text": msg})
            st.rerun()

# ===== FOOTER =====
st.markdown("---")
st.caption("Private Research Room")




