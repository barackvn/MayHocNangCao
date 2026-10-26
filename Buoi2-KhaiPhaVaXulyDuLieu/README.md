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

### 2. Lab 2.1: Xử Lý Dữ Liệu Khuyết Thiếu Trong Pandas (Missing Data)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab2_1_XuLyDuLieuKhuyetThieu_MissingData.ipynb)

* **Tập tin notebook:** [Lab2_1_XuLyDuLieuKhuyetThieu_MissingData.ipynb](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab2_1_XuLyDuLieuKhuyetThieu_MissingData.ipynb)
* **Tài liệu đề bài:** `Lab 2_1 Missing Data.pdf`
* **Tập dữ liệu thực tế:** [employees.csv](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/employees.csv) (1000 dòng, 8 thuộc tính)
* **Nội dung thực hiện:**
  - **Lý thuyết:** Phân loại 3 cơ chế khuyết thiếu: MCAR (hoàn toàn ngẫu nhiên), MAR (ngẫu nhiên có điều kiện), MNAR (không ngẫu nhiên).
  - **Mục 1:** Phát hiện dữ liệu thiếu trong DataFrame bằng `isnull()` và thống kê số lượng NaN.
  - **Mục 2:** Làm việc với tập dữ liệu thực tế `employees.csv`, lọc các bản ghi có `Gender = NaN` (145 bản ghi).
  - **Mục 3.1 (`fillna`):** Điền giá trị hằng số (`0`) và điền giá trị liền trước (`method='pad'`).
  - **Mục 3.2 (`replace`):** Thay thế giá trị NaN bằng giá trị đại diện quy ước (`-88`).
  - **Mục 3.3 (`interpolate`):** Nội suy tuyến tính đa biến (`method='linear'`) lấp đầy khoảng trống dữ liệu một cách mượt mà và tự nhiên.
  - **Đánh giá & So sánh:** Tổng hợp bảng ưu nhược điểm của các phương pháp xử lý dữ liệu khuyết thiếu trong phân tích dữ liệu lớn.
