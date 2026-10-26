# BẢN THUYẾT MINH ĐỀ TÀI ĐỒ ÁN MÔN HỌC: PHÂN TÍCH DỮ LIỆU LỚN (BIG DATA)
## VÒNG THẨM ĐỊNH VÀ CHỌN LỌC ĐỀ TÀI (TOP 30%)

---

### THÔNG TIN CHUNG
* **Tên đề tài tiếng Việt:** **Xây dựng Kiến trúc Lai Kết hợp Mô hình Đặc trưng Sâu ArcFace và Chỉ mục Lượng tử hóa Vector Phân tán (IVF-PQ/HNSW) cho Bài toán Nhận diện Khuôn mặt và Phân tích Sự kiện Đa Camera Thời gian thực**
* **Tên đề tài tiếng Anh:** *Building a Hybrid Architecture Combining Deep ArcFace Representation and Distributed Vector Quantization Indexing (IVF-PQ/HNSW) for Real-Time Multi-Camera Face Recognition and Event Stream Analytics*
* **Môn học:** Phân tích Dữ liệu lớn (Big Data Analytics)
* **Giảng viên hướng dẫn:** ThS. Hà Minh Tân
* **Nhóm sinh viên thực hiện:** Nhóm G11 - Khoa Công nghệ Thông tin / Khoa học Dữ liệu

---

### 1. TÍNH CẤP THIẾT VÀ GIÁ TRỊ THỰC TIỄN CỦA ĐỀ TÀI (PRACTICAL MOTIVATION)

Trong bối cảnh đô thị thông minh, quản lý an ninh tòa nhà và khu công nghiệp hiện đại, số lượng camera giám sát tăng trưởng với tốc độ chóng mặt. Tuy nhiên, hai rào cản kỹ thuật và kinh tế lớn nhất hiện nay là:

1. **Rào cản chi phí phần cứng chuyên dụng:**
   Hầu hết các giải pháp thương mại đòi hỏi thay thế toàn bộ hệ thống bằng "AI Camera" chuyên dụng có gắn chip NPU đắt đỏ (từ 500$ – 2.000$/camera). Trong khi đó, các doanh nghiệp và cơ quan nhà nước đã đầu tư hàng nghìn camera IP chuẩn RTSP thông thường truyền luồng H.264/H.265 về trung tâm điều khiển. Việc tận dụng trực tiếp luồng RTSP của hạ tầng camera sẵn có là bài toán thực tiễn có ý nghĩa kinh tế cực kỳ to lớn.

2. **Hiện tượng "Nghẽn cổ chai tính toán" (The Scalability Bottleneck):**
   Khi một khuôn mặt được cắt từ camera và trích xuất thành vector đặc trưng 512 chiều (float32), nếu so khớp tuần tự theo phương pháp quét cạn truyền thống (Brute-Force Flat Search) hoặc lưu trong hệ quản trị cơ sở dữ liệu quan hệ (SQL RDBMS):
   * Với quy mô nhỏ ($10^3$ người), thời gian tìm kiếm dưới 1 ms.
   * Nhưng khi cơ sở dữ liệu mở rộng lên hàng triệu người ($10^6 - 5 \times 10^6$ vectors) từ hàng trăm camera cùng lúc, độ phức tạp $O(N \cdot D)$ khiến độ trễ vọt lên 50 – 150 ms cho mỗi khuôn mặt, đồng thời chiếm dụng 2 – 10 GB bộ nhớ RAM cho mỗi tiến trình.
   * Kết quả: Hệ thống sụp đổ, trễ hàng ngàn khung hình, không thể phản hồi thời gian thực.

**Động lực đề tài:** Đề tài ra đời nhằm giải quyết triệt để bài toán này bằng cách kết hợp sức mạnh biểu diễn của Deep Learning với các kỹ thuật Tối ưu Dữ liệu lớn phân tán tiên tiến nhất hiện nay.

---

### 2. ĐIỂM MỚI VỀ PHƯƠNG PHÁP VÀ ĐÓNG GÓP KHOA HỌC (METHODOLOGY INNOVATION)

Đề tài không dừng lại ở việc áp dụng một mô hình thị giác máy tính đơn thuần, mà đề xuất **Mô hình Kiến trúc Lai 4 tầng (4-Tier Hybrid Architecture)** chuẩn mực cho hệ thống Dữ liệu lớn:

```
[Camera IP RTSP (1..N)] 
       │ (H.264 Streams)
       ▼
┌─────────────────────────────────────────────────────────────┐
│ TẦNG 1: THU NHẬN & LỌC CHẤT LƯỢNG (Quality-Aware Ingestion) │
│ • Lọc mờ bằng phương sai toán tử Laplacian (σ² > 120)       │
│ • Bỏ qua khung hình suy biến (Dynamic Frame Dropping)       │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Khuôn mặt đạt chuẩn)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TẦNG 2: MÔ HÌNH AI BIỂU DIỄN SÂU TRÊN MẶT SIÊU CẦU          │
│ • RetinaFace (FPN + SSH) căn chỉnh Affine 5 điểm mốc        │
│ • Pretrained ArcFace: Ánh xạ ảnh vào ℝ⁵¹² (||v||₂ = 1)      │
│ • Cơ chế "Zero-Retraining": Thêm mới không cần huấn luyện lại│
└──────────────────────────────┬──────────────────────────────┘
                               │ (Vector 512-D Chuẩn hóa L₂)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TẦNG 3: CHỈ MỤC TÌM KIẾM VECTOR DỮ LIỆU LỚN (FAISS ANN)    │
│ • IndexIVFFlat: Phân cụm Voronoi K-Means (nlist, nprobe)     │
│ • IndexIVFPQ: Lượng tử hóa tích (Product Quantization, m=64)│
│   ==> Nén dung lượng RAM 32 lần (từ 2.048 MB xuống 76 MB)   │
│ • IndexHNSW: Đồ thị phân cấp cho tìm kiếm cận logarit       │
│ • Độ trễ tìm kiếm < 0.5 ms trên 1.000.000 vector           │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Sự kiện nhận diện)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TẦNG 4: XỬ LÝ LUỒNG PHÂN TÁN & DATA LAKE (SPARK & PARQUET)  │
│ • Apache Kafka: Hấp thụ luồng sự kiện phân vùng theo CamID   │
│ • PySpark Structured Streaming: Sliding Window, Watermark   │
│ • Khử trùng lặp trạng thái (Stateful Deduplication)         │
│ • Apache Parquet: Lưu trữ cột nén Snappy, giảm 80% dung lượng│
│ • Phân tích hành trình liên camera (Cross-Camera Tracking)   │
└─────────────────────────────────────────────────────────────┘
```

#### Những điểm mới cốt lõi giúp đề tài vượt vòng chọn lọc 30%:
1. **Toán học tối ưu trên mặt siêu cầu đơn vị:** Chứng minh sự tương đương giữa khoảng cách Euclid $L_2^2$ và độ đo Cosine Similarity ($||u-v||_2^2 = 2 - 2 S_{cos}(u, v)$), cho phép sử dụng trọn vẹn các thuật toán định lượng không gian Metric của FAISS với tốc độ phần cứng SIMD tối đa.
2. **Kỹ thuật Lượng tử hóa Tích (Product Quantization - PQ):** Phân rã không gian $\mathbb{R}^{512}$ thành 64 không gian con 8 chiều, mã hóa mỗi vector thành chuỗi byte 64-bit, giúp tiết kiệm tới **96% bộ nhớ RAM** so với lưu vector thô.
3. **Pipeline Phân tích Sự kiện Đa Camera phân tán:** Xử lý luồng tới 500 camera đồng thời với độ trễ P95 dưới 3.5 giây, cho phép phát hiện tức thời hành vi di chuyển bất thường xuyên các khu vực an ninh (Spatiotemporal Anomaly Detection).

---

### 3. ĐỐI TƯỢNG VÀ PHẠM VI NGHIÊN CỨU

* **Đối tượng nghiên cứu:**
  * Dữ liệu hình ảnh khuôn mặt từ camera IP (luồng video RTSP thời gian thực).
  * Bộ dữ liệu vector đặc trưng chiều cao ($\mathbb{R}^{512}$) quy mô từ $10^4$ đến $5 \times 10^6$ vectors.
  * Bộ dữ liệu nhật ký sự kiện giám sát (5 triệu bản ghi sự kiện đa camera).
* **Phạm vi thực hiện:**
  * Xây dựng và đánh giá thực nghiệm toàn bộ pipeline trên nền tảng Python, FAISS, Apache Kafka và Apache Spark.
  * Đánh giá định lượng trên 5 kịch bản thực nghiệm khắt khe: Độ chính xác TAR/FAR, Khả năng mở rộng Scalability, Đánh đổi Pareto Recall–Latency, Thông lượng xử lý luồng Spark, và Hiệu quả lưu trữ truy vấn Data Lake Parquet.

---

### 4. KẾ HOẠCH TRIỂN KHAI VÀ SẢN PHẨM BÀN GIAO (DELIVERABLES)

Nhóm cam kết thực hiện đầy đủ và vượt mức các tiêu chuẩn của đồ án:

| Hạng mục | Sản phẩm cụ thể | Chỉ tiêu chất lượng cam kết |
| :--- | :--- | :--- |
| **Quyển Báo cáo** | `Bao_Cao_Do_An.docx` & `Bao_Cao_Do_An.pdf` | **> 40 trang (Mục tiêu 46–50 trang)**, chuẩn cấu trúc IEEE, công thức toán học chi tiết, 5 bảng số liệu thực nghiệm, 6 biểu đồ 300 DPI. |
| **Trình bày Bảo vệ** | `Slide_Bao_Ve_Do_An.pptx` + Video 25 phút | **28 slides chuyên nghiệp**, tỷ lệ 16:9, đầy đủ Speaker Notes phân công cho từng thành viên. |
| **Sản phẩm Mã nguồn** | Thư mục `src/`, `data/`, `results/` | Code sạch, module hóa, có sẵn script chạy tự động toàn bộ thực nghiệm và ứng dụng Live Demo RTSP. |
| **Video Demo Kỹ thuật** | Video clip 10–15 phút | Quay màn hình giải thích luồng xử lý, chạy benchmark trên tập dữ liệu triệu vector và demo thời gian thực. |

---

### 5. KẾT LUẬN VÀ KIẾN NGHỊ

Đề tài **“Xây dựng Kiến trúc Lai Kết hợp Mô hình Đặc trưng Sâu ArcFace và Chỉ mục Lượng tử hóa Vector Phân tán (IVF-PQ/HNSW) cho Bài toán Nhận diện Khuôn mặt và Phân tích Sự kiện Đa Camera Thời gian thực”** đáp ứng hoàn hảo cả hai tiêu chí cốt lõi của Giảng viên:
1. **Tính ứng dụng thực tiễn cao:** Trực tiếp giải quyết bài toán nâng cấp an ninh camera quy mô lớn với chi phí thấp.
2. **Hàm lượng khoa học và công nghệ Dữ liệu lớn sâu sắc:** Kết hợp hài hòa giữa thị giác máy tính hiện đại và các cấu trúc dữ liệu phân tán phức tạp (ANN, IVF-PQ, HNSW, Streaming Windowing, Data Lake Parquet).

Kính mong Thầy Hà Minh Tân xem xét và phê duyệt đề tài vào **nhóm 30% đề tài tự chọn xuất sắc** để nhóm triển khai thực hiện!
