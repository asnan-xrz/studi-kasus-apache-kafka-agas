# Tugas Big Data Kelas B - Studi Kasus Apache Kafka

| Nama Lengkap              | NRP           |
| :-----------------------: | :-----------: |
| Agas Ananta Wijaya        | 5027221004    |

## Soal
Topik: Pengumpulan Data Sensor IoT dengan Apache Kafka
Latar Belakang Masalah:
Sebuah pabrik memiliki beberapa mesin yang dilengkapi sensor suhu. Data suhu dari setiap mesin perlu dipantau secara real-time untuk menghindari overheating. Setiap sensor akan mengirimkan data suhu setiap detik, dan pabrik membutuhkan sistem yang dapat mengumpulkan, menyimpan, dan menganalisis data suhu ini.

Studi Kasus Sederhana:
- Pabrik membutuhkan aliran data sensor yang dapat diteruskan ke layanan analitik atau dashboard secara langsung.
- Apache Kafka akan digunakan untuk menerima dan mengalirkan data suhu, sementara PySpark akan digunakan untuk mengolah dan memfilter data tersebut.

Tugas:
1. Buat Topik Kafka untuk Data Suhu:
- Buat topik di Apache Kafka bernama "sensor-suhu" yang akan menerima data suhu dari sensor-sensor mesin.

2. Simulasikan Data Suhu dengan Producer:
- Buat producer sederhana yang mensimulasikan data suhu dari beberapa sensor mesin (misalnya, 3 sensor berbeda).
- Setiap data suhu berisi ID sensor dan suhu saat ini (misalnya, sensor_id: S1, suhu: 70°C), dan dikirim setiap detik ke topik "sensor-suhu".

3. Konsumsi dan Olah Data dengan PySpark:
- Buat consumer di PySpark yang membaca data dari topik "sensor-suhu".
- Filter data suhu yang berada di atas 80°C, sebagai indikator suhu yang perlu diperhatikan.

4. Output dan Analisis:
- Cetak data yang suhu-nya melebihi 80°C sebagai tanda peringatan sederhana di console.

## Dokumentasi dan Pengerjaan
1. Pengerjaan tugas ini memerlukan beberapa instalasi seperti Java 11, Apache Spark, Hadoop, dan Kafka. Setelah dipastikan semua terinstal dengan baik, kita bisa membuka cmd pada folder ```C:\kafka\kafka_2.13-3.8.1``` lalu mengetikkan command ```.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties``` untuk memulai zookeper server.

image-1

2. Selanjutnya kita buka cmd baru pada folder yang sama ```C:\kafka\kafka_2.13-3.8.1``` lalu mengetikkan command ```.\bin\windows\kafka-server-start.bat .\config\server.properties``` untuk memulai kafka server.

image-2

3. Buka cmd baru lagi pada folder yang sama, lalu ketikkan  ```kafka-topics.bat --create --bootstrap-server localhost:9092 --topic sensor-suhu``` untuk membuat topic baru bernama "sensor-suhu"

image-3

4. Setelah itu kita bisa langsung mensimulasikan data suhu dengan producer sederhana dengan membuat program ```kafka_producer_script.py``` dan meletakkannya pada folder ```C:\kafka\kafka_2.13-3.8.1```. Lalu mengetikkan command ```python3 kafka_producer_script.py``` untuk menjalankan programnya pada python3.

image-4

5. Kemudian kita jalankan program ```spark-consumer.py``` dengan mengetikkan command ```spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 .\spark-consumer.py```

image-5

6. Program sudah berjalan dengan cukup baik, ketika data suhu berada di atas 80°C, maka data akan di cetak pada consumer seperti yang terlihat pada image-5. Lalu ketika suhu berada di bawah 80°C, maka data tidak akan di cetak seperti berikut

image-6

7.  
