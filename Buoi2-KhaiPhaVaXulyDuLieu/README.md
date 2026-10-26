# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN - ĐHQG-HCM
### KHOA KHOA HỌC DỮ LIỆU & TRÍ TUỆ NHÂN TẠO
---
## BÁO CÁO THỰC HÀNH: LAB 1 - THU THẬP DỮ LIỆU TỪ WEB (WEB SCRAPING)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab1_ThuThapDuLieu_WebScraping.ipynb)

* **Học phần:** DS200 - Phân tích dữ liệu lớn (Big Data Analytics)
* **Lớp:** DS200.G11.CN2.TTNT
* **Giảng viên hướng dẫn:** ThS. Hà Minh Tân
* **Học viên / Sinh viên thực hiện:** barackvn
* **Email:** hotro.76@gmail.com

---

## 🎯 Nội dung thực hiện trong bài Lab
Bài lab giải quyết đầy đủ và chi tiết các mục yêu cầu trong tài liệu `Lab 1_ Thu thập dữ liệu.pdf`:
1. **Lý thuyết:** Giới thiệu tổng quan về giao thức HTTP/HTTPS, Web Scraping và bóc tách cây DOM.
2. **Cài đặt thư viện:** `requests`, `beautifulsoup4`, `pillow`, `pandas`, `lxml`.
3. **Thu thập tin tức:** Gửi HTTP request đến `https://vnexpress.net/bong-da` với đầy đủ User-Agent header nhằm đảm bảo tính ổn định.
4. **Trích xuất thông tin chi tiết từng bài:** Tiêu đề (`title`), tóm tắt (`abstract`/`sapo`), thời gian đăng, nội dung chi tiết.
5. **Yêu cầu 5:** Tổ chức dữ liệu vào Pandas DataFrame và xuất ra file CSV chuẩn `data_vnexpress_bongda.csv` (sử dụng bảng mã `utf-8-sig` hiển thị chuẩn tiếng Việt trên Microsoft Excel).
6. **Yêu cầu 6 (Mở rộng):** Thu thập dữ liệu từ trang báo khác (Báo Dân Trí `dantri.com.vn`), so sánh cấu trúc cây DOM và xuất `data_dantri_thethao.csv`.
