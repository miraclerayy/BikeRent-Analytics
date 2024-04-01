import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv("data_clean.csv")

# Isi title ini tentang dashboard data apa
st.set_page_config(page_title="Bike Sharing Data Analysis", page_icon="🚲")

# Tambahkan logo biar bagus
st.sidebar.image("biking.png", use_column_width=True)
st.title("Bike Sharing Dashboards")

# Raw Data yang belum di visualisasi
st.sidebar.subheader('Raw Data')
st.sidebar.write(day_df.head())

# Sidebar untuk filter data berdasarkan musim
season_filter = st.sidebar.selectbox('Filter berdasarkan musim', options=['Spring', 'Summer', 'Fall', 'Winter'])

# Filter data berdasarkan musim yang dipilih
filtered_data = day_df[day_df['season'] == season_filter]

# Visualisasi distribusi variabel
st.sidebar.subheader('Distribusi Variabel')
selected_variable = st.sidebar.selectbox("Pilih Variabel", options=['temperature', 'humidity', 'windspeed', 'cnt'])
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data[selected_variable], bins=20, kde=True, color='skyblue')
plt.xlabel(selected_variable.capitalize())
plt.ylabel('Frequency')
st.pyplot()

# Visualisasi pola musiman
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_data, x='month', y='cnt', hue='season', palette='Set2', marker='o')
plt.title('Sewa Sepeda berdasarkan Musim')
plt.xlabel('Month')
plt.ylabel('Bike Rentals')
plt.xticks(rotation=45)
plt.legend(title='Season', loc='upper right')
st.pyplot()

# Visualisasi pola hubungan antara hari kerja dan hari libur
plt.figure(figsize=(8, 6))
sns.barplot(data=filtered_data, x='workingday', y='cnt', hue='holiday', palette='Set2')
plt.title('Pengaruh Hari Libur dan Hari Kerja')
plt.xlabel('Hari Kerja')
plt.ylabel('Bike Rentals')
plt.legend(title='Libur', loc='upper right')
st.pyplot()

# Tambahkan penjelasan tambahan
if selected_variable == 'temperature':
    st.markdown("""
    ### Penjelasan Distribusi Variabel (Temperatur)
    Grafik ini menampilkan distribusi frekuensi peminjaman sepeda berdasarkan variabel suhu. 
    Ini memberikan wawasan tentang preferensi pengguna terhadap kondisi cuaca tertentu, yang dapat membantu dalam 
    merencanakan strategi operasional atau pemasaran sepeda Anda.
    """)
elif selected_variable == 'humidity':
    st.markdown("""
    ### Penjelasan Distribusi Variabel (Kelembaban)
    Grafik ini menampilkan distribusi frekuensi peminjaman sepeda berdasarkan variabel kelembaban. 
    Ini memberikan wawasan tentang preferensi pengguna terhadap kelembaban udara, yang dapat membantu dalam 
    merencanakan strategi operasional atau pemasaran sepeda Anda.
    """)
elif selected_variable == 'windspeed':
    st.markdown("""
    ### Penjelasan Distribusi Variabel (Kecepatan Angin)
    Grafik ini menampilkan distribusi frekuensi peminjaman sepeda berdasarkan variabel kecepatan angin. 
    Ini memberikan wawasan tentang preferensi pengguna terhadap kondisi angin, yang dapat membantu dalam 
    merencanakan strategi operasional atau pemasaran sepeda Anda.
    """)
elif selected_variable == 'cnt':
    st.markdown("""
    ### Penjelasan Distribusi Variabel (Jumlah Peminjaman Sepeda)
    Grafik ini menampilkan distribusi frekuensi jumlah peminjaman sepeda. 
    Ini memberikan gambaran tentang pola umum peminjaman sepeda, yang dapat digunakan untuk 
    merencanakan stok dan layanan Anda.
    """)

# Penjelasan tentang perbedaan musim
if season_filter == 'Spring':
    st.markdown("""
    ### Penjelasan tentang hubungan musim (Spring)
    Musim semi ditandai dengan suhu yang moderat dan alam yang mekar, yang mungkin menarik lebih banyak orang untuk beraktivitas di luar seperti bersepeda. Oleh karena itu, peminjaman sepeda cenderung meningkat selama musim semi.
    """)
elif season_filter == 'Summer':
    st.markdown("""
    ### Penjelasan tentang hubungan musim (Summer)
    Musim panas biasanya dikaitkan dengan cuaca hangat dan hari yang lebih panjang, membuatnya waktu yang ideal untuk aktivitas di luar seperti bersepeda. Akibatnya, peminjaman sepeda biasanya mencapai puncaknya selama bulan-bulan musim panas.
    """)
elif season_filter == 'Fall':
    st.markdown("""
    ### Penjelasan tentang hubungan musim (Fall)
    Musim gugur, juga dikenal sebagai musim gugur, ditandai dengan suhu yang lebih dingin dan dedaunan yang berwarna-warni. Meskipun peminjaman sepeda mungkin sedikit menurun dibandingkan musim panas, mereka tetap populer selama musim gugur.
    """)
elif season_filter == 'Winter':
    st.markdown("""
    ### Penjelasan tentang hubungan musim (Winter)
    Musim dingin ditandai dengan suhu dingin dan kadang-kadang kondisi cuaca yang tidak menguntungkan untuk bersepeda, seperti salju atau hujan. Akibatnya, peminjaman sepeda biasanya menurun selama bulan-bulan musim dingin.
    """)

# Hari libur dan Hari kerja
if 'workingday' in filtered_data.columns:
    st.markdown("""
    ### Perbedaan Hari Libur dan Hari Kerja terhadap Sewa
    
Visualisasi ini menggambarkan dampak hari kerja dan hari libur terhadap peminjaman sepeda. Secara umum, peminjaman sepeda dapat bervariasi berdasarkan apakah itu hari kerja atau hari libur. Batang-batang tersebut mewakili jumlah total peminjaman sepeda pada hari kerja (0) dan hari libur (1).
    """)
else:
    st.markdown("""
    ERROR
    """)

# Copyright
st.markdown("""
## Bike Sharing Dashboards

Copyright © 2022 Christian Miracle Rumawung. All Rights Reserved.
""")
