# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN - ĐHQG-HCM
### KHOA KHOA HỌC DỮ LIỆU & TRÍ TUỆ NHÂN TẠO
---
## HỌC PHẦN: DS200 - PHÂN TÍCH DỮ LIỆU LỚN (BIG DATA ANALYTICS)
### BÁO CÁO CÁC BÀI THỰC HÀNH BUỔI 3: PHÂN TÍCH DỮ LIỆU VÀ CÁC PHƯƠNG PHÁP HỌC CÓ GIÁM SÁT

* **Lớp:** DS200.G11.CN2.TTNT
* **Giảng viên hướng dẫn:** ThS. Hà Minh Tân
* **Học viên / Sinh viên thực hiện:** Dương Quốc Thương
* **STT:** 66
* **Email:** hotro.76@gmail.com
* **GitHub Repository:** [https://github.com/barackvn/MayHocNangCao](https://github.com/barackvn/MayHocNangCao)

---

## 📚 DANH SÁCH BÀI THỰC HÀNH

### 1. Lab 3.1: Hồi Quy Tuyến Tính Đơn Giản (Simple Linear Regression)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/barackvn/MayHocNangCao/blob/main/Buoi3-Phan%20Tich%20Du%20lieu%20v%C3%A0%20Cac%20Phuong%20Phap%20hoc%20co%20giam%20s%C3%A1t/Lab3_1_HoiQuyTuyenTinhDonGian.ipynb)

* **Tập tin notebook:** [Lab3_1_HoiQuyTuyenTinhDonGian.ipynb](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi3-Phan%20Tich%20Du%20lieu%20v%C3%A0%20Cac%20Phuong%20Phap%20hoc%20co%20giam%20s%C3%A1t/Lab3_1_HoiQuyTuyenTinhDonGian.ipynb) *(hoặc alias [LAB-3.1.ipynb](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi3-Phan%20Tich%20Du%20lieu%20v%C3%A0%20Cac%20Phuong%20Phap%20hoc%20co%20giam%20s%C3%A1t/LAB-3.1.ipynb))*
* **Tài liệu đề bài:** `LAB-3.1.pdf`
* **Tập dữ liệu thực tế:** [Salary_Data.csv](https://github.com/barackvn/MayHocNangCao/blob/main/Buoi3-Phan%20Tich%20Du%20lieu%20v%C3%A0%20Cac%20Phuong%20Phap%20hoc%20co%20giam%20s%C3%A1t/Salary_Data.csv) (Nguồn Kaggle: [Salary_data.csv - Kaggle Dataset](https://www.kaggle.com/datasets/ravitejakotharu/salary-datacsv) - 30 bản ghi gồm `YearsExperience` và `Salary`)
* **Nội dung thực hiện chi tiết:**
  - **Lý thuyết:**
    - Định nghĩa phương pháp Hồi quy tuyến tính đơn giản (*Simple Linear Regression*).
    - Công thức mô hình: $y = b_0 + b_1 x$ với biến độc lập $x$, biến phụ thuộc $y$, hệ số góc $b_1$ và hệ số chặn $b_0$.
    - Ước tính hệ số bằng tiêu chuẩn bình phương nhỏ nhất (Ordinary Least Squares - OLS) nhằm tối thiểu hóa tổng bình phương phần dư ($RSS \to \min$).
  - **Bước 1 (Load Dataset):**
    - Đọc dữ liệu từ file `Salary_Data.csv` (hỗ trợ tự động tải về từ GitHub khi chạy trên Google Colab).
    - Khám phá cấu trúc dữ liệu (`dataset.head()`, `dataset.shape`).
    - Phân tách biến độc lập $X$ và biến phụ thuộc $y$.
    - Chia tập dữ liệu thành Train set (80%) và Test set (20%) với `random_state=42`.
  - **Bước 2 (Visualize Data):**
    - Vẽ biểu đồ ma trận phân tán `sns.pairplot(dataset)` cho toàn bộ tập dữ liệu.
    - Vẽ biểu đồ phân tán điểm dữ liệu riêng cho tập huấn luyện (`X_train`, `y_train`).
    - Vẽ biểu đồ phân tán điểm dữ liệu riêng cho tập kiểm thử (`X_test`, `y_test`).
    - Khẳng định tính tương quan tuyến tính mạnh mẽ của dữ liệu.
  - **Bước 3 (Training Simple Linear Regression Model):**
    - Khởi tạo và huấn luyện mô hình `LinearRegression()` từ thư viện `scikit-learn`.
    - Trích xuất hệ số góc $b_1 \approx 9423.82$ và hệ số chặn $b_0 \approx 25321.58$.
    - Phương trình hồi quy cụ thể: $\text{Salary} = 25321.58 + 9423.82 \times \text{YearsExperience}$.
  - **Bước 4 (Predicting Test Results & Evaluation):**
    - Dự đoán mức lương `y_pred` trên tập kiểm thử và lập bảng so sánh `Original Salary` vs `Predict Salary`.
    - Đánh giá hệ số xác định $R^2$:
      - **Training Accuracy ($R^2$):** $\approx 0.9645$ (96.45%)
      - **Testing Accuracy ($R^2$):** $\approx 0.9024$ (90.24%)
  - **Bước 5 (Visualising Regression Line):**
    - Trực quan hóa đường hồi quy dự đoán cùng các điểm dữ liệu thực tế trên tập Train (`Salary vs Experience - Train set`).
    - Trực quan hóa đường hồi quy dự đoán cùng các điểm dữ liệu thực tế trên tập Test (`Salary vs Experience - Test set`).
  - **Bước 6 (Phần Mở Rộng - Advanced Evaluation & Practical Prediction):**
    - Tính toán các chỉ số đo lường sai số: MAE, MSE, RMSE, $R^2$.
    - Thử nghiệm dự đoán mức lương cụ thể cho nhân viên có số năm kinh nghiệm mới (5.0 năm, 10.0 năm, 12.0 năm).

