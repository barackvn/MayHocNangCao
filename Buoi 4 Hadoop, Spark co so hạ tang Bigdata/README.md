# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN - ĐHQG-HCM
### KHOA KHOA HỌC DỮ LIỆU & TRÍ TUỆ NHÂN TẠO
---
## HỌC PHẦN: DS200 - PHÂN TÍCH DỮ LIỆU LỚN (BIG DATA ANALYTICS)
### BÁO CÁO CÁC BÀI THỰC HÀNH BUỔI 4: HADOOP, SPARK & CƠ SỞ HẠ TẦNG BIG DATA

* **Lớp:** DS200.G11.CN2.TTNT
* **Giảng viên hướng dẫn:** ThS. Hà Minh Tân
* **Học viên / Sinh viên thực hiện:** Dương Quốc Thương
* **STT:** 66
* **Email:** hotro.76@gmail.com
* **GitHub Repository:** [https://github.com/barackvn/MayHocNangCao](https://github.com/barackvn/MayHocNangCao)

---

## 📚 DANH SÁCH BÀI THỰC HÀNH

### 1. Lab 5: Xử Lý Dữ Liệu Văn Bản - NLP & Tokenization (Data Preprocessing - Part 2)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/barackvn/MayHocNangCao/blob/main/Buoi%204%20Hadoop,%20Spark%20co%20so%20h%E1%BA%A1%20tang%20Bigdata/Lab5_DataPreprocessing_p2_NLP_Tokenization.ipynb)

* **Tập tin notebook:** [Lab5_DataPreprocessing_p2_NLP_Tokenization.ipynb](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi%204%20Hadoop,%20Spark%20co%20so%20h%E1%BA%A1%20tang%20Bigdata/Lab5_DataPreprocessing_p2_NLP_Tokenization.ipynb) *(hoặc alias [Lab5_Data_preprocessing_p2.ipynb](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi%204%20Hadoop,%20Spark%20co%20so%20h%E1%BA%A1%20tang%20Bigdata/Lab5_Data_preprocessing_p2.ipynb))*
* **Tài liệu đề bài:** `Lab 5_Data preprocessing_p2.docx`
* **Tài liệu thực hành:** 
  - `thebook.pdf`: Giáo trình *"Introduction to Machine Learning"* (Alex Smola & S.V.N. Vishwanathan) - [Link Google Drive gốc](https://drive.google.com/file/d/1iMJLPfliCWIpxR8mOqMWoM4j8ZMGxIIU/view?usp=sharing)
  - `Copy of Slide 2 GFS and Hadoop.pdf`: Bài giảng Hệ thống tệp phân tán Google File System (GFS) & Apache Hadoop.
* **Nội dung thực hiện chi tiết:**
  - **I – Lý thuyết:**
    - Khái niệm về dữ liệu phi cấu trúc và phương pháp truy xuất dữ liệu từ tệp PDF.
    - Kỹ thuật **Tokenization** (Tách từ & Tách câu).
    - Ý nghĩa và phương pháp loại bỏ **Stop Words** (Từ dừng).
    - So sánh sự khác biệt giữa **Stemming** (Rút gọn gốc từ heuristic) và **Lemmatization** (Chuẩn hóa từ nguyên dựa trên từ điển ngữ pháp).
  - **II – Thực hành:**
    - Bước 1: Nạp tệp tài liệu `thebook.pdf` (tự động tải về khi chạy trên môi trường Google Colab).
    - Bước 2: Đọc file PDF bằng thư viện `PyPDF2` và trích xuất nội dung văn bản trang index 10 (Chương 1: Introduction).
    - Bước 3: Chuyển toàn bộ văn bản về chữ thường (`.lower()`) và tìm vị trí xuất hiện của từ `"over"` (vị trí 15).
    - Bước 4: Cắt bỏ đoạn văn bản tiêu đề trước vị trí 15 (`result[15:]`).
    - Bước 5: Thay thế và loại bỏ các tiêu đề phân mục không cần thiết (`'1.1 a taste of machine learning'`, `'1.1.1 applications'`).
    - Bước 6: Định vị chuỗi kết thúc `"to achieve this goal"` (vị trí 1981).
    - Bước 7: Cắt lấy đoạn văn bản chuẩn từ đầu đến vị trí 1981.
    - Bước 8: Khám phá danh sách stopwords đa ngôn ngữ trong `nltk.corpus.stopwords`.
    - Bước 9: Phân tách văn bản thành danh sách các câu đơn lẻ bằng `sent_tokenize`.
    - Bước 10: Phân tách văn bản thành danh sách các từ và ký hiệu bằng `word_tokenize`.
    - Bước 11: Viết hàm loại bỏ từ dừng và đo lường tỉ lệ giảm thiểu kích thước từ vựng.
    - Bước 12: Áp dụng thuật toán Stemming với `SnowballStemmer`.
    - Bước 13: Áp dụng kỹ thuật Lemmatization với `WordNetLemmatizer` (POS tagging: `'v'`).
  - **III – Bài tập mở rộng:**
    - Áp dụng toàn bộ quy trình tiền xử lý văn bản NLP trên tài liệu PDF bài giảng thực tế: `Copy of Slide 2 GFS and Hadoop.pdf`.
    - Thống kê tần số phân phối từ vựng (`FreqDist`) và vẽ biểu đồ cột Top 15 từ khóa xuất hiện nhiều nhất sau khi đã loại bỏ từ dừng.
