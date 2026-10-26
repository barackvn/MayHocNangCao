# ĐỒ ÁN MÔN HỌC: PHÂN TÍCH DỮ LIỆU LỚN (BIG DATA ANALYTICS)
## ĐỀ TÀI: XÂY DỰNG KIẾN TRÚC LAI KẾT HỢP MÔ HÌNH ĐẶC TRƯNG SÂU ARCFACE VÀ CHỈ MỤC LƯỢNG TỬ HÓA VECTOR PHÂN TÁN (IVF-PQ/HNSW) CHO BÀI TOÁN NHẬN DIỆN KHUÔN MẶT VÀ PHÂN TÍCH SỰ KIỆN ĐA CAMERA THỜI GIAN THỰC

* **Mã lớp:** 09-DS200.G11.CN2.TTNT - Phân tích Dữ liệu lớn
* **Giảng viên hướng dẫn:** ThS. Hà Minh Tân
* **Nhóm sinh viên thực hiện:** Nhóm G11

---

## 1. GIỚI THIỆU DỰ ÁN

Dự án nghiên cứu và phát triển kiến trúc lai 4 tầng tích hợp giữa **Thị giác máy tính (RetinaFace + ArcFace)** và **Hệ sinh thái Xử lý Dữ liệu lớn phân tán (FAISS, Apache Kafka, Apache Spark, Apache Parquet)** nhằm giải quyết bài toán:
1. **Tận dụng hạ tầng Camera IP RTSP sẵn có** mà không cần đầu tư AI Camera đắt đỏ.
2. **Khắc phục điểm nghẽn cổ chai tính toán (Scalability Bottleneck):** Cho phép tìm kiếm đối sánh khuôn mặt tức thời trên cơ sở dữ liệu hàng triệu người ($10^6 - 5 \times 10^6$ vectors 512 chiều) với độ trễ dưới 0.5 ms.
3. **Tiết kiệm 96% dung lượng bộ nhớ RAM** nhờ áp dụng kỹ thuật Lượng tử hóa tích (Product Quantization - PQ).
4. **Xử lý luồng sự kiện phân tán từ 10 đến 500 camera đồng thời** bằng Spark Structured Streaming và Data Lake Parquet phục vụ truy vết hành trình liên camera (Cross-Camera Tracking).

---

## 2. CẤU TRÚC THƯ MỤC DỰ ÁN

```text
face_bigdata_project/
├── README.md                                  # Hướng dẫn chi tiết cài đặt và thực thi
├── requirements.txt                           # Danh sách các gói phụ thuộc Python
├── docs/                                      # Tài liệu học thuật & kịch bản thuyết trình
│   ├── 00_De_Cuong_Chon_Loc_30_Phan_Tram.md   # Bản thuyết minh đề tài vòng chọn lọc 30%
│   ├── 01_Kich_Ban_Video_Trinh_Bay_25p.md     # Kịch bản lời thoại 28 slides (20-30 phút)
│   └── 02_Kich_Ban_Video_Demo_Code_15p.md     # Kịch bản quay video demo mã nguồn (10-15 phút)
├── data/
│   ├── sample_faces/                          # Dữ liệu ảnh khuôn mặt mẫu & luồng camera
│   ├── embeddings/                            # Vector đặc trưng 512-D (.npy) benchmark
│   └── events_parquet/                        # Dữ liệu sự kiện định dạng Apache Parquet
├── results/
│   ├── tables/                                # 5 Bảng số liệu thực nghiệm định lượng (.csv)
│   │   ├── exp1_threshold_calibration.csv
│   │   ├── exp2_faiss_scalability.csv
│   │   ├── exp3_recall_latency_tradeoff.csv
│   │   ├── exp4_spark_streaming_throughput.csv
│   │   └── exp5_parquet_vs_json_analytics.csv
│   └── figures/                               # 6 Biểu đồ học thuật chuẩn 300 DPI (.png)
│       ├── fig1_system_architecture.png
│       ├── fig2_roc_tar_far_curve.png
│       ├── fig3_latency_qps_scaling.png
│       ├── fig4_ram_consumption_comparison.png
│       ├── fig5_recall_vs_latency_pareto.png
│       └── fig6_spark_streaming_throughput.png
├── src/
│   ├── config.py                              # Cấu hình toàn cục tham số hệ thống
│   ├── run_all_experiments.py                 # Chạy toàn bộ thực nghiệm và sinh bảng CSV
│   ├── plot_all_figures.py                    # Vẽ 6 biểu đồ 300 DPI từ file CSV
│   ├── rtsp_live_demo.py                      # Ứng dụng demo nhận diện luồng trực tiếp & FAISS
│   ├── exp4_kafka_spark_streaming_sim.py      # Mô phỏng pipeline Spark Streaming tải 500 camera
│   └── exp5_datalake_trajectory_analytics.py  # Truy vết liên camera & phân tích Data Lake Parquet
├── generators/
│   ├── build_full_report_docx.py              # Script sinh Quyển báo cáo Word > 40 trang & PDF
│   └── build_presentation_pptx.py             # Script sinh Bộ 28 slides PowerPoint bảo vệ đồ án
└── deliverables/
    ├── Bao_Cao_Do_An.docx                     # Báo cáo Đồ án định dạng Word (> 40 trang chuẩn A4)
    ├── Bao_Cao_Do_An.pdf                      # Báo cáo Đồ án định dạng PDF (chuyển đổi từ Word)
    └── Slide_Bao_Ve_Do_An.pptx                # Bộ Slide trình bày bảo vệ đồ án (28 slides)
```

---

## 3. HƯỚNG DẪN CÀI ĐẶT & CHẠY HỆ THỐNG

### 3.1. Cài đặt môi trường
Khuyến nghị sử dụng Python 3.10 – 3.14 trên Windows hoặc Linux:
```bash
pip install -r requirements.txt
```

### 3.2. Chạy toàn bộ thực nghiệm định lượng & Sinh biểu đồ
Chạy script tự động thực thi 5 kịch bản thực nghiệm và xuất bảng CSV:
```bash
python src/run_all_experiments.py
```
Sau đó tự động tạo 6 biểu đồ học thuật độ phân giải cao:
```bash
python src/plot_all_figures.py
```

### 3.3. Chạy Demo ứng dụng nhận diện RTSP Live & FAISS
Khởi chạy giao diện mô phỏng camera với kho 50.000 khuôn mặt trên chỉ mục IVF-PQ:
```bash
python src/rtsp_live_demo.py
```

### 3.4. Chạy mô phỏng Spark Streaming & Truy vết Data Lake Parquet
```bash
python src/exp4_kafka_spark_streaming_sim.py
python src/exp5_datalake_trajectory_analytics.py
```

### 3.5. Tự động sinh Quyển Báo cáo Word (> 40 trang), PDF và Slide PowerPoint (28 slides)
```bash
# 1. Sinh Quyển báo cáo Word và tự động chuyển đổi sang PDF
python generators/build_full_report_docx.py

# 2. Sinh Bộ slide thuyết trình PowerPoint
python generators/build_presentation_pptx.py
```

Toàn bộ sản phẩm bàn giao cuối cùng sẽ nằm sẵn trong thư mục `deliverables/`.
