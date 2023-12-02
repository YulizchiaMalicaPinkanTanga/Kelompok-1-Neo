import streamlit as st

def main():
    st.title("Selamat Datang di SolarGuard🌞")
    st.subheader("Membantu Anda Mengoptimalkan Jadwal Pemeliharaan Panel Surya Agar Lebih Efektif Dan Efisien")

    st.image("logoo.jpg", caption="SolarGuard", use_column_width=True)

    st.markdown("""
        <div style="text-align: justify;">
        SolarGuard adalah sebuah aplikasi canggih yang menggabungkan kecerdasan buatan dengan analisis anomaly pada output energi yang dihasilkan oleh panel surya di PLTS. 
        Aplikasi ini dirancang untuk membantu teknisi mengetahui kapan waktu untuk melakukan maintenance pada panel surya yang telah terpasang agar keluaran energi yang dihasilkan selalu optimal. 
        SolarGuard akan menganalisis data keluaran energi dari panel surya, dan apabila terdapat anomaly atau keanehan pada data keluaran salah satu atau beberapa panel surya.
        Berdasarkan analisis tersebut, aplikasi akan memberikan rekomendasi jadwal pelaksanaan maintenance untuk panel surya sehingga dapat meningkatkan efisiensi dari panel surya di PLTS.
    """, unsafe_allow_html=True)

    st.write("### Fitur Utama:")
    st.write("- 📅 Input Data")
    st.write("- 📊 Diplay Data")
    st.write("- 📊 Predict Data")
    st.write("- 🔔 Anomaly Detector and Maintenance Warning")

    st.write("### Prosedur Pemakaian SolarGuard:")
    st.markdown("""
        1. **Input dataset:**
            - Ubah nama folder yang ingin anda prediksi dan cari anomalinya menjadi "plant_generation_data"
            - Klik tombol "Browse file" untuk mengakses fitur ini.
            - Input dataset yang telah diubah nama.
            - Simpan dataset dengan Klik tombol "save file".

        2. **Display Data:**
            - Klik tombol "Display Data" untuk menunjukkan grafik dari dataset.

        3. **Predict Data:**
            - Klik tombol "Predict Data" untuk dilakukan prediksi data.
            - Prediksi data dilakukan untuk mengetahui kondisi akan akan terjadi pada panel surya di hari berikutnya berdasarkan grafik keluaran.

        4. **Anomaly Detector and Maintenance Warning:**
            - Klik tombol "Anomaly Detector and Maintenance Warning" .
            - Apabila diperlukan pemeliharaan segera maka akan muncul peringatan otomatis.""")
    
    # formulir pendaftaran
    st.write("### Bergabunglah Bersama Kami!")
    with st.form("form_pendaftaran"):
        nama_pengguna = st.text_input("Nama Pengguna:")
        email_pengguna = st.text_input("Alamat Email:")
        kata_sandi = st.text_input("Kata Sandi:", type="password")
        konfirmasi_kata_sandi = st.text_input("Konfirmasi Kata Sandi:", type="password")

        submitted = st.form_submit_button("Bergabung Sekarang")

        if submitted:
            # Proses formulir pendaftaran di sini 
            if kata_sandi != konfirmasi_kata_sandi:
                st.warning("Kata sandi dan konfirmasi kata sandi tidak cocok. Silakan coba lagi.")
            else:
                st.success(f"Terima kasih, {nama_pengguna}! Anda telah berhasil bergabung dengan SolarGuard.")

    st.write("### Hubungi Kami")
    st.markdown("""
        Jika Anda memiliki pertanyaan atau memerlukan bantuan, jangan ragu untuk menghubungi tim kami.
        ✉️ [Hubungi Kami](mailto:yulizchiamalica@gmail.com)""")

if __name__ == "__main__":
    main()