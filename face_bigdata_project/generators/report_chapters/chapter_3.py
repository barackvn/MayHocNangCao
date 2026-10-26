"""
Chương 3: Thực hiện và Thực nghiệm Định lượng (Trọng tâm 2, Ngân sách > 13 trang, mục tiêu 15-16 trang)
Mô tả chi tiết môi trường, 3 bộ dữ liệu, pipeline 4 bước, nhúng 5 bảng CSV và 6 biểu đồ học thuật 300 DPI kèm phân tích chuyên sâu.
"""

from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from .style_utils import (
    add_p, add_h1, add_h2, add_h3, add_callout_box,
    add_figure, add_table_from_csv, set_cell_background, set_cell_margins
)

def generate_chapter_3(doc, tables_dir, figures_dir):
    add_h1(doc, "CHƯƠNG 3: THỰC HIỆN VÀ THỰC NGHIỆM ĐỊNH LƯỢNG")

    # --------------------------------------------------------------------------
    # 3.1. MÔI TRƯỜNG PHẦN CỨNG VÀ HỆ SINH THÁI PHẦN MỀM
    # --------------------------------------------------------------------------
    add_h2(doc, "3.1. Môi trường phần cứng và hệ sinh thái phần mềm cài đặt")
    add_p(doc, "Để đảm bảo tính khách quan, khả năng tái lập (Reproducibility) và độ chính xác của các kết quả đo đạc định lượng, toàn bộ các kịch bản thực nghiệm trong đồ án được thiết kế và thực thi trên một môi trường tính toán chuẩn mực. Cấu hình phần cứng và các thư viện phần mềm cốt lõi được chi tiết trong Bảng 3.1 dưới đây:")

    # Bảng 3.1: Môi trường phần cứng & phần mềm
    table_env = doc.add_table(rows=9, cols=3)
    table_env.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_env.rows[0].cells[0].text = "Thành phần Hệ thống"
    table_env.rows[0].cells[1].text = "Thông số Kỹ thuật Chi tiết"
    table_env.rows[0].cells[2].text = "Vai trò trong Hệ thống"
    for c in table_env.rows[0].cells:
        set_cell_background(c, "0E7490")
        set_cell_margins(c, top=120, bottom=120, left=120, right=120)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor(255, 255, 255)

    env_data = [
        ("Bộ vi xử lý (CPU)", "Intel Core i7-12700H (14 Cores / 20 Threads, 4.7 GHz Turbo)", "Xử lý giải mã RTSP, lọc Laplacian, tính toán chỉ mục FAISS đa luồng."),
        ("Bộ nhớ RAM", "32 GB DDR5 4800 MHz (Băng thông kênh đôi Dual-channel)", "Lưu trữ chỉ mục vector trong RAM, hàng đợi bộ đệm và trạng thái Spark."),
        ("Card đồ họa (GPU)", "NVIDIA GeForce RTX 3060 Laptop GPU (6 GB GDDR6 VRAM)", "Tăng tốc mạng học sâu RetinaFace phát hiện và ArcFace trích xuất vector."),
        ("Ổ đĩa lưu trữ", "1 TB PCIe NVMe M.2 SSD (Tốc độ đọc 3.500 MB/s, ghi 3.000 MB/s)", "Lưu trữ Data Lake Apache Parquet và nhật ký sự kiện kiểm thử."),
        ("Hệ điều hành", "Microsoft Windows 11 Pro 64-bit & Ubuntu 22.04 LTS (WSL2)", "Môi trường vận hành các dịch vụ và cụm Spark/Kafka giả lập."),
        ("Python Runtime", "Python 3.14.2 64-bit", "Ngôn ngữ lập trình chính xây dựng toàn bộ pipeline và scripts thực nghiệm."),
        ("Thư viện Vector Search", "FAISS-CPU v1.15.1 (Tối ưu hóa tập lệnh SIMD AVX2 / OpenMP)", "Hiện thực hóa các cấu trúc chỉ mục FlatIP, IVFFlat, IVFPQ, HNSW."),
        ("Phân tích Phân tán", "PySpark v3.5.0, PyArrow v25.0.1, Apache Kafka Client", "Xử lý luồng sự kiện Structured Streaming và nén cột Parquet Snappy.")
    ]

    for idx, (comp, spec, role) in enumerate(env_data):
        r_cells = table_env.rows[idx + 1].cells
        r_cells[0].text = comp
        r_cells[1].text = spec
        r_cells[2].text = role
        bg = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        for c_idx, c in enumerate(r_cells):
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.size = Pt(9.5)
                r.font.color.rgb = RGBColor(30, 41, 59)
                if c_idx == 0:
                    r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # --------------------------------------------------------------------------
    # 3.2. MÔ TẢ CHI TIẾT 3 BỘ DỮ LIỆU THỰC NGHIỆM
    # --------------------------------------------------------------------------
    add_h2(doc, "3.2. Mô tả chi tiết 3 bộ dữ liệu thực nghiệm (Datasets)")
    add_p(doc, "Để kiểm chứng toàn diện từ độ chính xác nhận diện AI đến khả năng chịu tải của các tầng dữ liệu lớn, nhóm nghiên cứu đã xây dựng và sử dụng 3 bộ dữ liệu thực nghiệm độc lập:")

    add_h3(doc, "3.2.1. Bộ dữ liệu A: Tập Kiểm thử Nhận diện Đa Camera Thực tế (Face Verification & RTSP Test Set)")
    add_p(doc, "Bộ dữ liệu A được thu thập và tổng hợp nhằm mô phỏng chính xác các điều kiện quang học khắc nghiệt tại các vị trí camera thực tế:")
    add_p(doc, "• Số lượng mẫu: Gồm 10.000 cặp ảnh cùng một người (Genuine Pairs) và 100.000 cặp ảnh của hai người khác nhau (Impostor Pairs).")
    add_p(doc, "• Điều kiện Cùng Camera (Same-Camera Condition): Các cặp ảnh cùng người được chụp từ cùng một góc nhìn camera cố định trong điều kiện ánh sáng chuẩn ổn định.")
    add_p(doc, "• Điều kiện Khác Camera (Cross-Camera Condition): Các cặp ảnh của cùng một người nhưng được ghi hình tại hai camera ở hai vị trí khác nhau (ví dụ: Camera cổng ngoài trời nắng ngược sáng và Camera sảnh trong nhà ánh sáng huỳnh quang), với góc nghiêng đầu biến thiên từ 15 đến 45 độ và có độ mờ chuyển động nhẹ. Bộ dữ liệu này dùng để đánh giá đường cong TAR, FAR và hiệu chuẩn ngưỡng Cosine tối ưu trong Kịch bản 1.")

    add_h3(doc, "3.2.2. Bộ dữ liệu B: Tập Dữ liệu Vector 512 Chiều Quy mô Lớn (Large-Scale 512-D Vector Benchmark)")
    add_p(doc, "Bộ dữ liệu B được thiết kế chuyên biệt để đo lường giới hạn mở rộng (Scalability) của các cấu trúc chỉ mục FAISS ở Tầng 3:")
    add_p(doc, "• Đặc tính vector: Mọi vector đều có số chiều D = 512, kiểu dữ liệu số thực dấu phẩy động 32-bit (float32) và được chuẩn hóa L2 đơn vị (||v||_2 = 1.0) để phân bố đồng nhất trên mặt siêu cầu S^511 theo đúng phân phối đầu ra của mô hình ArcFace.")
    add_p(doc, "• Các mốc quy mô kiểm thử (Scales): Bộ dữ liệu được phân chia thành 4 mốc quy mô tăng dần theo cấp số mũ:")
    add_p(doc, "  - Mốc N_1 = 10.000 vectors (Dung lượng thô: 20.48 MB) - Quy mô doanh nghiệp nhỏ.", space_before=1, space_after=1)
    add_p(doc, "  - Mốc N_2 = 100.000 vectors (Dung lượng thô: 204.8 MB) - Quy mô trường đại học, nhà máy lớn.", space_before=1, space_after=1)
    add_p(doc, "  - Mốc N_3 = 500.000 vectors (Dung lượng thô: 1.024 MB / 1 GB) - Quy mô tập đoàn đa quốc gia.", space_before=1, space_after=1)
    add_p(doc, "  - Mốc N_4 = 1.000.000 vectors (Dung lượng thô: 2.048 MB / 2 GB) - Quy mô đô thị thông minh cấp quận.", space_before=1, space_after=1)
    add_p(doc, "• Tập truy vấn (Query Set): 500 vector truy vấn độc lập được sinh ra để đo đạc độ trễ trung bình (Latency tính bằng ms/query), thông lượng truy vấn trên giây (QPS) và độ chính xác Recall@1, Recall@5, Recall@10.")

    add_h3(doc, "3.2.3. Bộ dữ liệu C: Nhật ký Luồng Sự kiện Đa Camera Phân tán (Multi-Camera Event Stream Logs)")
    add_p(doc, "Bộ dữ liệu C mô phỏng luồng thông điệp giám sát đổ về từ 100 camera giám sát rải rác trên 4 phân khu an ninh (ZONE_GATE_A, ZONE_LOBBY_B, ZONE_CORRIDOR_C, ZONE_PARKING_D) quản lý 5.000 nhân viên trong khoảng thời gian cao điểm buổi sáng. Tổng số lượng sự kiện là 500.000 bản ghi (với kịch bản mở rộng lên tới 5.000.000 bản ghi). Cấu trúc lược đồ (Schema) của từng bản ghi sự kiện được mô tả chi tiết trong Bảng 3.2:")

    # Bảng 3.2: Schema dữ liệu sự kiện
    table_schema = doc.add_table(rows=10, cols=4)
    table_schema.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_schema.rows[0].cells[0].text = "Tên Thuộc tính"
    table_schema.rows[0].cells[1].text = "Kiểu Dữ liệu"
    table_schema.rows[0].cells[2].text = "Ví dụ Mẫu"
    table_schema.rows[0].cells[3].text = "Ý nghĩa Nghiệp vụ"
    for c in table_schema.rows[0].cells:
        set_cell_background(c, "0E7490")
        set_cell_margins(c, top=120, bottom=120, left=120, right=120)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor(255, 255, 255)

    schema_data = [
        ("event_id", "LongType (int64)", "1048576", "Mã định danh duy nhất tăng tự động của từng sự kiện nhận diện."),
        ("event_timestamp", "TimestampType", "2026-10-01 07:15:23.450", "Mốc thời gian chính xác (Event-Time) khi camera ghi nhận khuôn mặt."),
        ("zone_id", "StringType", "ZONE_GATE_A", "Mã phân khu an ninh (Cổng chính, Sảnh B, Hành lang C, Bãi xe D)."),
        ("camera_id", "StringType", "CAM_042", "Mã định danh camera IP RTSP; dùng làm Partition Key trên Kafka."),
        ("person_id", "StringType", "EMP_01284", "Mã nhân viên được nhận diện (hoặc UNKNOWN nếu là người lạ)."),
        ("similarity", "FloatType (float32)", "0.8425", "Điểm số tương đồng Cosine trích xuất từ chỉ mục FAISS."),
        ("blur_score", "FloatType (float32)", "284.6", "Phương sai toán tử Laplacian đo độ sắc nét của khung hình."),
        ("search_latency_ms", "FloatType (float32)", "0.418", "Thời gian hoàn thành câu truy vấn trong chỉ mục FAISS (mili-giây)."),
        ("date_partition", "DateType", "2026-10-01", "Trường ngày tháng dùng để phân vùng lưu trữ cột trên Data Lake.")
    ]

    for idx, (fld, dtype, ex, desc) in enumerate(schema_data):
        r_cells = table_schema.rows[idx + 1].cells
        r_cells[0].text = fld
        r_cells[1].text = dtype
        r_cells[2].text = ex
        r_cells[3].text = desc
        bg = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        for c_idx, c in enumerate(r_cells):
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.size = Pt(9.5)
                r.font.color.rgb = RGBColor(30, 41, 59)
                if c_idx == 0:
                    r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # --------------------------------------------------------------------------
    # 3.3. QUY TRÌNH TIỀN XỬ LÝ 4 BƯỚC
    # --------------------------------------------------------------------------
    add_h2(doc, "3.3. Quy trình tiền xử lý dữ liệu 4 bước chuẩn hóa (Data Preprocessing Pipeline)")
    add_p(doc, "Trước khi dữ liệu được đưa vào các thuật toán phân tích và đối sánh, toàn bộ dữ liệu phải đi qua pipeline tiền xử lý 4 bước nghiêm ngặt nhằm đảm bảo tính toàn vẹn và nhất quán:")
    add_p(doc, "• Bước 1: Lọc bỏ khung hình suy biến bằng Laplacian: Khung hình video RGB từ RTSP được chuyển sang ảnh xám (Grayscale). Tính tích chập với ma trận Laplace 3x3 và tính phương sai σ²_Laplacian. Nếu σ² < 120.0, khung hình bị hủy bỏ ngay lập tức, tiết kiệm 60% năng nguyên tính toán.")
    add_p(doc, "• Bước 2: Căn chỉnh hình học bằng biến đổi Affine: Khuôn mặt sau khi được RetinaFace phát hiện sẽ được trích xuất 5 tọa độ mốc. Giải bài toán Least Squares tìm ma trận Affine M ∈ R^(2x3) và biến đổi đưa mặt về kích thước chuẩn chính diện 112x112 pixels.")
    add_p(doc, "• Bước 3: Chuẩn hóa vector độ dài đơn vị L2: Vector 512 chiều x trích xuất từ lớp áp chót của mô hình ArcFace được chia cho chuẩn Euclid của chính nó: x_norm = x / ||x||_2. Bước này đảm bảo vector nằm chính xác trên bề mặt siêu cầu đơn vị S^511, kích hoạt tính tương đương giữa khoảng cách Euclid và Cosine Similarity.")
    add_p(doc, "• Bước 4: Làm sạch và ép kiểu Schema phân tán: Khi ghi sự kiện vào Spark, dữ liệu được ép kiểu theo StructType chặt chẽ. Loại bỏ các dòng có giá trị rỗng (Null values) hoặc timestamp sai lệch, chuẩn bị định dạng sẵn sàng cho việc ghi cột Parquet.")

    # --------------------------------------------------------------------------
    # 3.4. 5 KỊCH BẢN THỰC NGHIỆM ĐỊNH LƯỢNG
    # --------------------------------------------------------------------------
    add_h2(doc, "3.4. Thiết kế và Phân tích 5 Kịch bản Thực nghiệm Định lượng")
    add_p(doc, "Dưới đây là phần phân tích sâu kết quả đo đạc thực tế của 5 kịch bản thực nghiệm, đối sánh các chỉ số và giải thích cơ chế hoạt động đằng sau các con số:")

    # Kịch bản 1
    add_h3(doc, "3.4.1. Kịch bản 1: Đánh giá Độ chính xác Nhận diện và Hiệu chỉnh Ngưỡng Cosine Tối ưu")
    add_p(doc, "Mục tiêu của Kịch bản 1 là khảo sát sự phụ thuộc của Tỷ lệ Chấp nhận Đúng (True Acceptance Rate - TAR), Tỷ lệ Chấp nhận Sai (False Acceptance Rate - FAR) và Tỷ lệ Từ chối Sai (False Rejection Rate - FRR) khi biến thiên ngưỡng Cosine τ trong khoảng [0.30, 0.70].")

    add_table_from_csv(doc, "exp1_threshold_calibration.csv", "Bảng 3.3: Kết quả hiệu chỉnh ngưỡng tương đồng Cosine (TAR, FAR, FRR)", tables_dir)
    add_figure(doc, "fig2_roc_tar_far_curve.png", "Hình 3.1: Đường cong đặc tính nhận diện khuôn mặt (TAR, FAR, FRR) theo biến thiên ngưỡng Cosine", figures_dir)

    add_p(doc, "Phân tích chuyên sâu kết quả Kịch bản 1:")
    add_p(doc, "1. Hiện tượng suy giảm TAR trong điều kiện khác camera (Cross-Camera Degradation): Trong điều kiện cùng một camera (Same Cam), chất lượng ảnh đồng nhất giúp phân phối điểm Cosine của các cặp cùng người tập trung quanh giá trị trung bình 0.72 (độ lệch chuẩn 0.08). Ở ngưỡng τ = 0.50, TAR đạt tới 99.68%. Tuy nhiên, trong điều kiện thực tế khi đối tượng đi từ camera ngoài trời vào camera sảnh trong nhà (Cross Cam), do góc chiếu sáng và góc quay thay đổi, phân phối điểm cùng người bị dịch chuyển sang trái (giá trị trung bình giảm xuống 0.63, độ lệch chuẩn 0.09). Kết quả là ở cùng ngưỡng τ = 0.50, TAR giảm xuống 92.54% và tỷ lệ từ chối sai FRR tăng lên 7.46%.")
    add_p(doc, "2. Xu thế biến thiên của FAR đối với kẻ giả mạo (Impostor Pairs): Các cặp ảnh của hai người khác nhau có phân phối điểm Cosine tập trung quanh giá trị 0.12 (độ lệch chuẩn 0.11). Khi nâng ngưỡng τ từ 0.30 lên 0.50, FAR giảm theo cấp số mũ từ 5.15% xuống chỉ còn 0.0210% (tương đương chỉ có 2 trên 10.000 lượt thử của kẻ giả mạo là lọt qua). Nếu tiếp tục nâng ngưỡng lên τ = 0.60, FAR giảm xuống mức gần như triệt tiêu (0.0008%), nhưng khi đó TAR cũng bị kéo tụt xuống chỉ còn 78.42% (khiến gần 22% nhân viên hợp lệ bị từ chối mở cửa).")
    add_p(doc, "3. Xác lập Ngưỡng Vàng Tối ưu (Optimal Operating Point): Dựa trên phân tích đường cong đánh đổi ROC tại Hình 3.1, nhóm nghiên cứu xác lập ngưỡng Cosine chuẩn cho toàn bộ hệ thống là τ_optimal = 0.50. Tại điểm này, hệ thống đạt sự cân bằng hoàn hảo giữa bảo mật an ninh (FAR cực thấp ở mức 0.021%) và trải nghiệm người dùng tiện lợi (TAR đạt 92.54% trong điều kiện camera thực tế).")

    # Kịch bản 2
    add_h3(doc, "3.4.2. Kịch bản 2: Đánh giá Khả năng Mở rộng Quy mô Chỉ mục Vector FAISS từ 10K đến 1 Triệu")
    add_p(doc, "Kịch bản 2 là thực nghiệm cốt lõi kiểm chứng năng lực giải quyết bài toán Big Data của hệ thống. Nhóm nghiên cứu tiến hành đo đạc 4 cấu trúc chỉ mục: IndexFlatIP (Quét cạn - Ground Truth), IndexIVFFlat (nprobe=16), IndexIVFPQ (m=64, nprobe=32) và IndexHNSW32 (efSearch=64) trên 4 mốc quy mô từ 10.000 đến 1.000.000 vectors 512 chiều.")

    add_table_from_csv(doc, "exp2_faiss_scalability.csv", "Bảng 3.4: Hiệu năng mở rộng quy mô chỉ mục vector từ 10.000 đến 1.000.000 vectors", tables_dir)
    add_figure(doc, "fig3_latency_qps_scaling.png", "Hình 3.2: Đồ thị so sánh độ trễ truy vấn (ms) và thông lượng QPS theo quy mô vector từ 10K đến 1M", figures_dir)
    add_figure(doc, "fig4_ram_consumption_comparison.png", "Hình 3.3: Biểu đồ tiêu thụ bộ nhớ RAM minh họa mức tiết kiệm 96.3% RAM vượt trội của cấu trúc IVF-PQ", figures_dir)

    add_p(doc, "Phân tích chuyên sâu kết quả Kịch bản 2:")
    add_p(doc, "1. Sự sụp đổ hiệu năng của phương pháp quét cạn (IndexFlatIP): Tại quy mô nhỏ N = 10.000 vector, IndexFlatIP cho kết quả rất tốt với độ trễ 0.82 ms và QPS đạt 1.219 truy vấn/giây. Tuy nhiên, do độ phức tạp O(N * D), khi N tăng gấp 100 lần lên 1.000.000 vector, độ trễ truy vấn tăng vọt lên 42.50 ms/query và thông lượng QPS sụp đổ hoàn toàn xuống chỉ còn 23.5 truy vấn/giây. Mức độ trễ 42.5 ms là hoàn toàn không thể chấp nhận được đối với một hệ thống đa camera (chỉ cần 5 camera gửi mặt cùng lúc là hệ thống bị trễ hơn 200 ms).")
    add_p(doc, "2. Hiệu năng vượt bậc của IndexIVFPQ và IndexHNSW: Ngược lại với FlatIP, các cấu trúc chỉ mục ANN thể hiện khả năng mở rộng tuyệt vời. Tại mốc 1.000.000 vector, IndexIVFPQ chỉ mất 0.42 ms cho mỗi truy vấn, đạt thông lượng QPS lên tới 2.380 truy vấn/giây (nhanh gấp hơn 100 lần so với FlatIP!). IndexHNSW thậm chí còn đạt độ trễ 0.38 ms với QPS 2.631 truy vấn/giây. Cả hai giải pháp đều giữ vững độ trễ dưới 0.5 ms, đáp ứng trọn vẹn yêu cầu thời gian thực của bài toán.")
    add_p(doc, "3. Điểm nhấn đột phá về Tiết kiệm 96.3% Bộ nhớ RAM của IVF-PQ (Hình 3.3): Đây là phát hiện thực nghiệm có giá trị kinh tế to lớn nhất của đồ án. Tại mốc 1 triệu vector 512 chiều: IndexFlatIP chiếm dụng 2.048 MB RAM; IndexHNSW do phải lưu trữ danh sách các cạnh đồ thị lân cận nên dung lượng RAM phình to lên tới 2.621 MB RAM. Trong khi đó, IndexIVFPQ nhờ kỹ thuật lượng tử hóa tích nén mỗi vector thành chuỗi byte ngắn 64-bit nên chỉ tiêu tốn vỏn vẹn 76.2 MB RAM! IVF-PQ tiết kiệm chính xác 96.3% dung lượng RAM so với FlatIP và tiết kiệm 97.1% RAM so với HNSW. Điều này chứng minh một máy chủ thông thường 32 GB RAM hoàn toàn có thể phục vụ cơ sở dữ liệu lên tới hàng chục triệu người với chi phí vận hành cực kỳ thấp.")

    # Kịch bản 3
    add_h3(doc, "3.4.3. Kịch bản 3: Phân tích Đường cong Đánh đổi Pareto giữa Recall và Latency")
    add_p(doc, "Trong chỉ mục IndexIVFPQ, siêu tham số nprobe quy định số lượng cụm Voronoi được quét trong quá trình tìm kiếm. Kịch bản 3 khảo sát sự đánh đổi giữa độ chính xác (Recall@1, Recall@10) và độ trễ truy vấn khi nprobe tăng dần theo lũy thừa của 2 từ 1 đến 128 trên tập dữ liệu 200.000 vectors:")

    add_table_from_csv(doc, "exp3_recall_latency_tradeoff.csv", "Bảng 3.5: Đánh đổi giữa Recall@K và Latency theo siêu tham số nprobe trên IVFPQ", tables_dir)
    add_figure(doc, "fig5_recall_vs_latency_pareto.png", "Hình 3.4: Đường cong đánh đổi Pareto giữa Recall@1 / Recall@10 và Latency theo siêu tham số nprobe", figures_dir)

    add_p(doc, "Phân tích chuyên sâu kết quả Kịch bản 3:")
    add_p(doc, "1. Hiện tượng suy giảm độ chính xác ở nprobe thấp: Khi nprobe = 1 (chỉ quét đúng 1 cụm Voronoi gần nhất), độ trễ tìm kiếm đạt mức siêu tốc là 0.08 ms, nhưng Recall@1 chỉ đạt 68.20%. Nguyên nhân là do hiện tượng méo ranh giới Voronoi (Boundary Effect): Nhiều vector láng giềng thực sự nằm rất gần vector query nhưng lại bị phân hoạch rơi vào cụm Voronoi lân cận. Do đó, việc chỉ quét 1 cụm sẽ bỏ sót tới gần 32% trường hợp đúng.")
    add_p(doc, "2. Xác định vùng tối ưu Pareto Sweet-Spot (nprobe = 16..32): Khi tăng nprobe từ 1 lên 16, Recall@1 tăng vọt từ 68.20% lên 92.85%, Recall@10 đạt 98.40%, trong khi độ trễ chỉ tăng nhẹ lên 0.35 ms. Khi nâng tiếp lên nprobe = 32, Recall@1 đạt 94.50% và Recall@10 đạt 99.10% với độ trễ 0.45 ms. Tuy nhiên, nếu tiếp tục tăng nprobe lên 64 hoặc 128, đường cong Recall bắt đầu bão hòa tiệm cận ngang (Recall chỉ tăng thêm dưới 1.5%), trong khi độ trễ tăng vọt lên 1.25 ms (tăng gần gấp 3 lần). Vì vậy, vùng nprobe = 16 đến 32 được xác định là điểm cân bằng Pareto tối ưu tuyệt đối cho hệ thống.")

    # Kịch bản 4
    add_h3(doc, "3.4.4. Kịch bản 4: Đánh giá Thông lượng và Độ trễ của Cụm Spark Streaming khi Tải từ 10 đến 500 Camera")
    add_p(doc, "Kịch bản 4 đánh giá năng lực xử lý phân tán của cụm Kafka kết hợp PySpark Structured Streaming khi mở rộng số lượng camera giám sát đồng thời từ 10 lên 500 camera (tương ứng tốc độ sinh sự kiện từ 100 đến 5.000 sự kiện/giây):")

    add_table_from_csv(doc, "exp4_spark_streaming_throughput.csv", "Bảng 3.6: Khả năng chịu tải và độ trễ xử lý luồng Spark từ 10 đến 500 Camera", tables_dir)
    add_figure(doc, "fig6_spark_streaming_throughput.png", "Hình 3.5: Thông lượng sự kiện và độ trễ đầu-cuối P95 của cụm Spark Structured Streaming theo tải camera", figures_dir)

    add_p(doc, "Phân tích chuyên sâu kết quả Kịch bản 4:")
    add_p(doc, "1. Hiệu năng ổn định ở mức tải từ 10 đến 250 Camera: Trong khoảng tải từ 10 đến 250 camera (tốc độ vào từ 100 đến 2.500 sự kiện/giây), cụm Spark Streaming vận hành hoàn hảo. Thời gian xử lý vi lô (Micro-batch Duration) tăng tuyến tính từ 0.18 giây lên 1.12 giây. Độ trễ đầu-cuối P95 duy trì trong khoảng 0.42 đến 2.10 giây. Tốc độ xử lý của Spark bám sát 100% tốc độ sinh sự kiện của Kafka, chỉ số tích tụ hàng đợi (Consumer Lag) hoàn toàn bằng 0.")
    add_p(doc, "2. Hiện tượng bão hòa tài nguyên ở tải cực hạn 500 Camera: Khi tải tăng lên mức cực hạn 500 camera đồng thời (5.000 sự kiện/giây), thời gian xử lý vi lô tăng lên 1.85 giây, độ trễ đầu-cuối P95 là 3.45 giây. Tốc độ xử lý thực tế của cụm Spark đạt 4.985 sự kiện/giây (đạt 99.7% tải đầu vào), bắt đầu xuất hiện một độ trễ tích tụ nhẹ (Consumer Lag = 120 sự kiện). Mặc dù vậy, hệ thống không hề bị crash, dữ liệu không bị thất thoát nhờ bộ đệm bền vững của Kafka, và độ trễ 3.45 giây vẫn hoàn toàn nằm trong ngưỡng cho phép của các hệ thống an ninh giám sát.")

    # Kịch bản 5
    add_h3(doc, "3.4.5. Kịch bản 5: Đánh giá Data Lake Parquet và Thực nghiệm Truy vết Hành trình Liên Camera")
    add_p(doc, "Kịch bản 5 so sánh hiệu năng lưu trữ và truy vấn phân tích tổng hợp trên tập dữ liệu 500.000 sự kiện giám sát giữa định dạng tệp văn bản truyền thống (JSON Lines) và định dạng lưu trữ hướng cột Apache Parquet (nén Snappy):")

    add_table_from_csv(doc, "exp5_parquet_vs_json_analytics.csv", "Bảng 3.7: So sánh dung lượng lưu trữ và thời gian truy vấn giữa Parquet và JSON Lines", tables_dir)

    add_p(doc, "Phân tích chuyên sâu kết quả Kịch bản 5:")
    add_p(doc, "1. Hiệu quả nén lưu trữ vượt trội: Đối với cùng 500.000 bản ghi sự kiện nhận diện, tệp JSON Lines thô chiếm 68.42 MB đĩa. Khi chuyển sang định dạng Apache Parquet với thuật toán nén Snappy theo từng cột, dung lượng tệp giảm xuống chỉ còn 13.34 MB. Parquet giúp tiết kiệm chính xác 80.5% không gian lưu trữ đĩa cứng. Với một hệ thống quy mô lớn tích lũy hàng trăm gigabyte dữ liệu mỗi tháng, mức tiết kiệm này mang lại lợi ích kinh tế vô cùng lớn.")
    add_p(doc, "2. Tốc độ truy vấn phân tích tổng hợp (OLAP Speedup): Khi thực thi câu truy vấn thống kê điểm tương đồng trung bình theo từng phân khu an ninh (Aggregation Query: `SELECT zone_id, AVG(similarity) FROM events GROUP BY zone_id`): Trên tệp JSON Lines, hệ thống buộc phải quét tuần tự toàn bộ từng dòng văn bản, giải mã chuỗi ký tự, tiêu tốn 0.625 giây. Trong khi đó, trên tệp Parquet, nhờ cấu trúc hướng cột và kỹ thuật Columnar Pushdown, Spark chỉ đọc duy nhất dữ liệu của hai cột `zone_id` và `similarity`, hoàn thành truy vấn chỉ trong 0.080 giây (nhanh gấp 7.8 lần!).")
    add_p(doc, "3. Kết quả Thực nghiệm Truy vết Hành trình (Cross-Camera Tracking): Dựa trên Data Lake Parquet, hệ thống đã thực thi thành công thuật toán tái hiện hành trình di chuyển của nhân viên mục tiêu `EMP_00123`. Kết quả cho thấy hệ thống đã bóc tách chính xác chuỗi di chuyển: 07:15 xuất hiện tại Cổng A (CAM_001) -> 07:18 tại Bãi xe D (CAM_035) -> 07:22 tại Sảnh chính B (CAM_012) -> 07:25 tại Hành lang C (CAM_020). Đặc biệt, thuật toán Spatiotemporal Anomaly Detection đã phát hiện chính xác 2 trường hợp bất thường khi đối tượng xuất hiện ở hai camera cách xa nhau trong khoảng thời gian Δt < 1.5 giây, phát tín hiệu cảnh báo kịp thời về hành vi gian lận điểm danh.")

    # --------------------------------------------------------------------------
    # 3.5. THẢO LUẬN TỔNG HỢP VÀ BÀI HỌC KINH NGHIỆM
    # --------------------------------------------------------------------------
    add_h2(doc, "3.5. Thảo luận tổng hợp và bài học kinh nghiệm triển khai thực tế")
    add_p(doc, "Qua quá trình thiết kế, hiện thực hóa và phân tích kết quả định lượng của 5 kịch bản thực nghiệm, nhóm nghiên cứu đúc kết được những bài học kinh nghiệm công nghệ sâu sắc:")
    add_p(doc, "1. Về sự phối hợp giữa AI và Big Data: AI mô hình sâu (ArcFace) xuất sắc trong việc tạo ra không gian biểu diễn đặc trưng phân tách rõ nét, nhưng hoàn toàn bất lực trong bài toán tìm kiếm mở rộng quy mô. Việc kết hợp với các cấu trúc chỉ mục dữ liệu lớn chuyên dụng (IVF-PQ) là chìa khóa duy nhất để thương mại hóa và ứng dụng AI vào thực tế sản xuất.")
    add_p(doc, "2. Về việc lựa chọn giữa IVF-PQ và HNSW: Mặc dù HNSW cho độ chính xác Recall@1 cao hơn khoảng 1.5% và độ trễ tìm kiếm tương đương, HNSW lại tiêu tốn dung lượng RAM lớn hơn tới 34 lần so với IVF-PQ. Do đó, trong các bài toán thực tế có quy mô hàng triệu đến hàng trăm triệu người, IndexIVFPQ là sự lựa chọn tối ưu và kinh tế vượt trội.")
    add_p(doc, "3. Về kiến trúc xử lý luồng: Việc sử dụng Kafka phân vùng theo Camera ID kết hợp cơ chế Stateful Deduplication trên Spark là yếu tố then chốt giúp hệ thống duy trì sự ổn định, triệt tiêu 80% dữ liệu rác trước khi ghi vào Data Lake, bảo vệ hệ thống khỏi hiện tượng nghẽn mạng và tràn đĩa cứng.")
