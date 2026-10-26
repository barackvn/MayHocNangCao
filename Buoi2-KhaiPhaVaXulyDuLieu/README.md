# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN - ĐHQG-HCM
### KHOA KHOA HỌC DỮ LIỆU & TRÍ TUỆ NHÂN TẠO
---
## HỌC PHẦN: DS200 - PHÂN TÍCH DỮ LIỆU LỚN (BIG DATA ANALYTICS)
### BÁO CÁO CÁC BÀI THỰC HÀNH BUỔI 2: KHAI PHÁ VÀ TIỀN XỬ LÝ DỮ LIỆU

* **Lớp:** DS200.G11.CN2.TTNT
* **Giảng viên hướng dẫn:** ThS. Hà Minh Tân
* **Học viên / Sinh viên thực hiện:** barackvn
* **Email:** hotro.76@gmail.com

---

## 📚 DANH SÁCH BÀI THỰC HÀNH

### 1. Lab 1: Thu Thập Dữ Liệu Từ Web (Web Scraping)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab1_ThuThapDuLieu_WebScraping.ipynb)

* **Tập tin notebook:** [Lab1_ThuThapDuLieu_WebScraping.ipynb](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab1_ThuThapDuLieu_WebScraping.ipynb)
* **Tài liệu đề bài:** `Lab 1_ Thu thập dữ liệu.pdf`
* **Nội dung thực hiện:**
  - Khai phá mã nguồn và bóc tách cây HTML DOM bằng `requests` và `BeautifulSoup4`.
  - Thu thập danh sách tin tức bóng đá từ VnExpress (`https://vnexpress.net/bong-da`).
  - Bóc tách chi tiết: tiêu đề, tóm tắt, thời gian xuất bản, nội dung bài viết.
  - **Yêu cầu 5:** Xuất dữ liệu dạng bảng sang tệp tin `data_vnexpress_bongda.csv` chuẩn mã hóa `utf-8-sig`.
  - **Yêu cầu 6 (Mở rộng):** Thu thập dữ liệu từ Báo Dân Trí (`dantri.com.vn`), so sánh cấu trúc DOM và xuất `data_dantri_thethao.csv`.

---

### 2. Lab 2: Làm Việc Với Dữ Liệu Bị Thiếu Trong Thư Viện Pandas (Missing Data)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab2_1_XuLyDuLieuKhuyetThieu_MissingData.ipynb)

* **Tập tin notebook:** [Lab2_1_XuLyDuLieuKhuyetThieu_MissingData.ipynb](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab2_1_XuLyDuLieuKhuyetThieu_MissingData.ipynb)
* **Tài liệu đề bài:** `Lab 2_1 Missing Data.pdf`
* **Tập dữ liệu thực tế:** [employees.csv](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/employees.csv) (1000 dòng, 8 thuộc tính)
* **Nội dung thực hiện:**
  - **Lý thuyết:** Giữ nguyên bản định nghĩa Missing Data, nguyên nhân và 3 loại khuyết thiếu: MCAR, MAR, MNAR.
  - **Mục 1:** Phát hiện dữ liệu thiếu trong DataFrame bằng `df.isnull()`.
  - **Mục 2:** Làm việc với tập dữ liệu thực tế `employees.csv`, lọc các bản ghi có `Gender = NaN` (145 bản ghi).
  - **Mục 3.1 (`fillna`):** Điền giá trị hằng số (`0`) và điền giá trị liền trước (`method='pad'`).
  - **Mục 3.2 (`replace`):** Thay thế giá trị NaN bằng giá trị quy ước (`-88`).
  - **Mục 3.3 (`interpolate`):** Sử dụng hàm interpolate() để điền các giá trị còn thiếu bằng phương pháp tuyến tính (`linear`).

---

### 3. Lab 3: Làm Sạch Dữ Liệu (Data Cleaning)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab3_Clearning_Data.ipynb)

* **Tập tin notebook:** [Lab3_Clearning_Data.ipynb](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab3_Clearning_Data.ipynb)
* **Tài liệu đề bài:** `Lab 3_Clearning Data.pdf`
* **Tập dữ liệu thực hành & bài tập:**
  - [data.csv](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/data.csv) (dữ liệu nhân viên, địa chỉ thực hành phần II)
  - [property_data.csv](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/property_data.csv) (dữ liệu bất động sản bài tập phần III)
* **Nội dung thực hiện:**
  - **Lý thuyết:** Giữ nguyên bản nội dung lý thuyết và các thao tác làm sạch dữ liệu của Thầy.
  - **Phần II - Thực hành:**
    - Lấy dữ liệu dataset từ Google Drive / GitHub.
    - Viết thường (`lower`), viết hoa (`upper`), viết hoa chữ cái đầu (`title`) tên các cột.
    - Thay thế khoảng trắng bằng dấu gạch dưới `_` trong tên cột.
    - Đổi tên cột (`rename`), gán tên cột theo vị trí index (`columns.values`).
    - Lọc cột loại trừ (`!=`, `~isin`), lọc cột theo từ khóa (`filter(like=...)`), ký tự kết thúc (`endswith`, `regex`).
    - Chọn một nhóm tên cột theo chỉ mục slice.
  - **Phần III - Bài tập:**
    - 2.1: Đọc tệp `property_data.csv` vào DataFrame, xử lý các định dạng missing `["n/a", "na", "--"]`.
    - 2.2: Tìm trong DataFrame những dữ liệu bị thiếu (`isnull`).
    - 2.3: Xem cột `NUM_BEDROOMS` và tìm những giá trị `NaN`.
    - 2.4: Tính tổng số giá trị còn thiếu trong toàn bộ DataFrame (10 giá trị).
    - 2.5: Điền giá trị `126` vào ô bị thiếu trong cột `ST_NUM`.
    - 2.6: Thay thế missing values trong cột `NUM_BEDROOMS` bằng giá trị trung vị (`median = 2.5`).
