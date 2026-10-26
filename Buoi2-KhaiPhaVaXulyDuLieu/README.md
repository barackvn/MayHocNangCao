# 📊 DS200 - Phân tích dữ liệu lớn | Buổi 2: Lab 1 - Thu Thập Dữ Liệu Web

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/barackvn/MayHocNangCao/blob/main/Buoi2-KhaiPhaVaXulyDuLieu/Lab1_ThuThapDuLieu_WebScraping.ipynb)

> 💡 **Nhấn vào nút trên để mở và chạy trực tiếp bài Lab trên Google Colab!**

---

## 🎯 Nội dung bài Lab
Bài lab giải quyết trọn vẹn yêu cầu trong tài liệu `Lab 1_ Thu thập dữ liệu.pdf`:
1. **Lý thuyết:** Giới thiệu tổng quan về giao thức HTTP/HTTPS, Web Scraping và bóc tách cây DOM.
2. **Cài đặt thư viện:** `requests`, `beautifulsoup4`, `pillow`, `pandas`, `lxml`.
3. **Thu thập tin tức:** Gửi request đến `https://vnexpress.net/bong-da` với đầy đủ User-Agent header tránh bị chặn.
4. **Trích xuất thông tin chi tiết từng bài:** Tiêu đề (`title`), tóm tắt (`abstract`/`sapo`), thời gian đăng, nội dung chi tiết.
5. **Yêu cầu 5:** Tổ chức dữ liệu vào Pandas DataFrame và xuất ra file CSV chuẩn `data_vnexpress_bongda.csv` (hỗ trợ `utf-8-sig` hiển thị tốt trên Excel tiếng Việt).
6. **Yêu cầu 6 (Mở rộng):** Thu thập dữ liệu từ trang báo khác (Báo Dân Trí `dantri.com.vn`), so sánh cấu trúc cây DOM và xuất `data_dantri_thethao.csv`.

---

## 🚀 Hướng dẫn đẩy lên GitHub (Git Commands)

Mở terminal (PowerShell hoặc Git Bash) tại thư mục gốc của đồ án và chạy các lệnh sau:

```bash
# 1. Khởi tạo Git repository (nếu chưa khởi tạo)
git init

# 2. Thêm tất cả các file vào staging
git add .

# 3. Tạo commit đầu tiên
git commit -m "feat: hoan thanh Lab 1 Thu thap du lieu Web Scraping chay tren Google Colab"

# 4. Đổi tên nhánh chính sang main
git branch -M main

# 5. Liên kết với kho lưu trữ GitHub của bạn
git remote add origin https://github.com/barackvn/MayHocNangCao.git

# 6. Đẩy mã nguồn lên GitHub
git push -u origin main
```
