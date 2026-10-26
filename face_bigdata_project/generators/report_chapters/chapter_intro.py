"""
Chương Mở Đầu: Tính cấp thiết, Mục tiêu, Đối tượng, Phạm vi, Phương pháp, Ý nghĩa, Bố cục (Ngân sách 4 trang)
"""

from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from .style_utils import add_p, add_h1, add_h2, add_h3, add_callout_box

def generate_introduction(doc):
    add_h1(doc, "MỞ ĐẦU")

    # --------------------------------------------------------------------------
    # 1. TÍNH CẤP THIẾT VÀ GIÁ TRỊ THỰC TIỄN
    # --------------------------------------------------------------------------
    add_h2(doc, "1. Tính cấp thiết và Giá trị thực tiễn của đề tài")
    add_p(doc, "Trong kỷ nguyên chuyển đổi số và phát triển đô thị thông minh (Smart City), các hệ thống giám sát an ninh thông minh, tự động hóa kiểm soát ra vào tại các tòa nhà cao ốc, khu công nghiệp công nghệ cao, sân bay và trường học đang trở thành một thành phần cốt lõi không thể thiếu. Sự bùng nổ của các thiết bị ghi hình độ nét cao đã dẫn tới việc hàng trăm nghìn camera giám sát được triển khai trên diện rộng. Tuy nhiên, khi vận hành ở quy mô thực tế, các doanh nghiệp và cơ quan quản lý đang phải đối mặt với một nghịch lý lớn giữa bài toán chi phí đầu tư phần cứng và bài toán năng lực xử lý dữ liệu lớn:")

    add_p(doc, "Thứ nhất, rào cản chi phí thay thế phần cứng chuyên dụng: Đa phần các giải pháp nhận diện khuôn mặt thương mại hiện nay đều yêu cầu trang bị các dòng 'AI Camera' chuyên dụng đắt đỏ (có tích hợp sẵn chip vi xử lý nơ-ron NPU tại biên). Mức chi phí cho mỗi mắt camera chuyên dụng này dao động từ 15 đến 50 triệu đồng. Trong khi đó, tại hầu hết các cơ quan, nhà máy, xí nghiệp, hạ tầng camera IP thông thường (sử dụng giao thức truyền luồng RTSP chuẩn H.264/H.265) đã được lắp đặt hoàn chỉnh từ trước với số lượng lên tới hàng trăm mắt camera. Việc xóa bỏ hạ tầng cũ để thay mới đồng loạt đòi hỏi nguồn vốn đầu tư khổng lồ lên tới hàng tỷ đồng, gây lãng phí nghiêm trọng nguồn lực xã hội. Do đó, nhu cầu cấp bách là phải tìm ra một giải pháp kỹ thuật có khả năng 'thông minh hóa' trực tiếp hạ tầng camera IP RTSP sẵn có, tận dụng luồng video thô truyền về trung tâm dữ liệu mà không cần phải can thiệp hay thay thế phần cứng tại hiện trường.")

    add_p(doc, "Thứ hai, hiện tượng 'Nghẽn cổ chai tính toán' (The Computational Scalability Bottleneck): Khi hệ thống mở rộng quy mô giám sát lên hàng chục, hàng trăm camera đồng thời phục vụ quản lý nhân sự cho một tập đoàn lớn, khu đô thị hoặc cơ sở dữ liệu quốc gia (từ 100.000 đến hàng triệu người), bài toán lập tức đối mặt với điểm nghẽn cổ chai điển hình của Dữ liệu lớn (Big Data). Mỗi khuôn mặt khi được trích xuất bằng các mạng nơ-ron học sâu (Deep Neural Networks) sẽ tạo thành một vector đặc trưng toán học 512 chiều (dưới dạng số thực dấu phẩy động float32, tương ứng 2.048 bytes).")

    add_callout_box(doc, "Bản chất của Điểm nghẽn Cổ chai Tìm kiếm Vector:",
                    "Nếu áp dụng phương pháp so khớp vét cạn truyền thống (Brute-force Flat Search) hoặc lưu trữ trong các hệ quản trị cơ sở dữ liệu quan hệ SQL (MySQL, PostgreSQL), độ phức tạp tính toán cho mỗi lần khuôn mặt xuất hiện là O(N * D), trong đó N là số lượng người trong cơ sở dữ liệu và D = 512 là số chiều. Tại quy mô N = 1.000.000 người, một truy vấn đòi hỏi thực hiện hơn 500 triệu phép nhân cộng dấu phẩy động, khiến thời gian phản hồi tăng vọt từ dưới 1 ms lên 40 - 150 ms cho mỗi khuôn mặt, đồng thời chiếm dụng 2 - 8 GB bộ nhớ RAM chỉ để chứa dữ liệu vector thô. Khi có hàng trăm camera đồng thời gửi khung hình về, hệ thống lập tức sụp đổ do tràn bộ nhớ và tắc nghẽn hàng đợi (Message Queue Lag).")

    add_p(doc, "Nhận thức rõ thách thức thực tiễn to lớn này, đề tài được khởi xướng với mục tiêu xây dựng một Kiến trúc Lai (Hybrid Architecture) kết hợp hài hòa giữa mô hình biểu diễn đặc trưng sâu tiên tiến nhất hiện nay (RetinaFace và ArcFace) với các kỹ thuật chỉ mục nén vector phân tán (FAISS IVF-PQ/HNSW) và hệ sinh thái xử lý luồng sự kiện phân tán (Apache Kafka, PySpark Structured Streaming và Data Lake Parquet). Đề tài hướng tới việc giải quyết triệt để bài toán mở rộng quy mô, đảm bảo khả năng nhận diện thời gian thực với độ trễ dưới 1 mili-giây trên hàng triệu khuôn mặt, đồng thời tiết kiệm hơn 90% chi phí phần cứng máy chủ.")

    # --------------------------------------------------------------------------
    # 2. MỤC TIÊU NGHIÊN CỨU
    # --------------------------------------------------------------------------
    add_h2(doc, "2. Mục tiêu nghiên cứu (Tổng quát và Cụ thể)")
    add_p(doc, "Mục tiêu tổng quát của đề tài là: Nghiên cứu, thiết kế, hiện thực hóa và đánh giá thực nghiệm toàn diện một hệ thống lai tích hợp giữa Trí tuệ nhân tạo thị giác máy tính và Nền tảng Dữ liệu lớn phân tán, cho phép thu nhận trực tiếp luồng video từ các Camera IP RTSP thông thường, thực hiện nhận diện khuôn mặt cực nhanh trên cơ sở dữ liệu quy mô triệu vector và phân tích sự kiện di chuyển thời gian thực.")

    add_p(doc, "Để hiện thực hóa mục tiêu tổng quát trên, nhóm nghiên cứu đã xác định và hoàn thành 4 mục tiêu kỹ thuật cụ thể sau:")
    add_p(doc, "1. Xây dựng Kiến trúc Lai 4 tầng hoàn chỉnh: Tách biệt rõ ràng giữa tầng thu nhận video RTSP và lọc chất lượng khung hình (Tầng 1); tầng biểu diễn đặc trưng AI sâu trên mặt siêu cầu (Tầng 2); tầng chỉ mục tìm kiếm vector dữ liệu lớn siêu tốc (Tầng 3); và tầng xử lý luồng phân tán kết hợp Data Lake (Tầng 4).", space_before=2, space_after=2)
    add_p(doc, "2. Tối ưu hóa mô hình AI theo cơ chế Zero-Retraining: Ứng dụng mô hình ArcFace với hàm mất mát biên góc cộng tính (Additive Angular Margin Loss) để ánh xạ khuôn mặt thành vector chuẩn hóa 512 chiều trên mặt siêu cầu đơn vị. Thiết lập cơ chế đăng ký danh tính mới tức thời mà không cần phải huấn luyện lại (retrain) toàn bộ mạng nơ-ron.", space_before=2, space_after=2)
    add_p(doc, "3. Đột phá về Nén RAM và Tốc độ Tìm kiếm Vector: Nghiên cứu cơ sở toán học chứng minh tương đương giữa độ đo Cosine và khoảng cách Euclid bình phương. Ứng dụng thuật toán Phân cụm Đảo ngược (IVF) và Lượng tử hóa Tích (Product Quantization - PQ) trên thư viện FAISS, đạt mục tiêu nén dung lượng bộ nhớ RAM ít nhất 30 lần và duy trì độ trễ đối sánh dưới 0.5 ms trên 1.000.000 vector.", space_before=2, space_after=2)
    add_p(doc, "4. Xây dựng Pipeline Xử lý Luồng và Data Lake hiệu năng cao: Thiết lập cụm Apache Kafka và PySpark Structured Streaming với cơ chế Watermarking và lọc trùng lặp có trạng thái (Stateful Deduplication), đảm bảo xử lý ổn định luồng sự kiện từ 10 đến 500 camera đồng thời; lưu trữ sự kiện lịch sử dưới định dạng Apache Parquet nén Snappy phục vụ truy vết hành trình liên camera (Cross-Camera Tracking).", space_before=2, space_after=4)

    # --------------------------------------------------------------------------
    # 3. ĐỐI TƯỢNG VÀ PHẠM VI NGHIÊN CỨU
    # --------------------------------------------------------------------------
    add_h2(doc, "3. Đối tượng và Phạm vi nghiên cứu")
    add_p(doc, "Đối tượng nghiên cứu của đồ án bao gồm:")
    add_p(doc, "• Dữ liệu hình ảnh khuôn mặt thu nhận trực tiếp từ luồng video mạng Camera IP thông qua giao thức RTSP thời gian thực trong điều kiện môi trường thực tế (chuyển động, góc nghiêng, ánh sáng biến thiên).")
    add_p(doc, "• Bộ dữ liệu vector đặc trưng chiều cao (High-dimensional Vector Embeddings, R^512) ở các mốc quy mô từ 10.000 đến 1.000.000 vector chuẩn hóa L2.")
    add_p(doc, "• Dữ liệu nhật ký sự kiện giám sát đa camera (Multi-Camera Event Stream Logs) quy mô từ 500.000 đến 5.000.000 bản ghi.")
    add_p(doc, "• Các thuật toán thị giác máy tính sâu (RetinaFace, ArcFace) và các cấu trúc chỉ mục tìm kiếm láng giềng gần nhất xấp xỉ (Inverted File, Product Quantization, HNSW trên thư viện FAISS).")
    add_p(doc, "• Các framework tính toán luồng phân tán và lưu trữ dữ liệu lớn: Apache Kafka, Apache Spark Structured Streaming, Apache Parquet.")

    add_p(doc, "Phạm vi thực hiện của đồ án:")
    add_p(doc, "• Về mặt thuật toán: Tập trung vào bài toán nhận diện 1:N (Face Identification) trên cơ sở dữ liệu lớn đã đăng ký, đối sánh vector đặc trưng trên mặt siêu cầu đơn vị và phân tích chuỗi thời gian sự kiện liên camera.")
    add_p(doc, "• Về mặt công nghệ: Xây dựng hệ thống hoàn chỉnh trên môi trường Python 3, FAISS, PySpark, PyArrow; đo đạc và kiểm chứng định lượng trên 5 kịch bản thực nghiệm khắt khe.")
    add_p(doc, "• Giới hạn đề tài: Đề tài chưa đi sâu vào việc huấn luyện mô hình chống giả mạo khuôn mặt 3D chuyên biệt (Face Anti-Spoofing) và giới hạn triển khai chỉ mục FAISS trên môi trường máy chủ đơn node có hỗ trợ tập lệnh SIMD AVX2.")

    # --------------------------------------------------------------------------
    # 4. PHƯƠNG PHÁP LUẬN NGHIÊN CỨU
    # --------------------------------------------------------------------------
    add_h2(doc, "4. Phương pháp luận nghiên cứu")
    add_p(doc, "Đồ án áp dụng phương pháp luận nghiên cứu kết hợp chặt chẽ giữa lý thuyết toán học mô hình hóa và thực nghiệm đo đạc định lượng (Empirical Benchmark Methodology):")
    add_p(doc, "1. Phương pháp Nghiên cứu Lý thuyết và Mô hình hóa Toán học: Khảo cứu sâu các nguyên lý hình học vi phân trên mặt siêu cầu đơn vị S^(D-1). Thiết lập chứng minh giải tích chứng minh sự tương đương tuyến tính giữa hàm mất mát khoảng cách Euclid bình phương và độ tương đồng Cosine. Phân tích độ phức tạp thời gian và không gian của các thuật toán phân vùng Voronoi K-Means, lượng tử hóa tích phân rã không gian con và đồ thị thế giới nhỏ phân cấp.")
    add_p(doc, "2. Phương pháp Thực nghiệm Đo đạc Định lượng (Empirical Benchmarking): Xây dựng bộ mã nguồn kiểm thử tự động, thu thập các chỉ số hiệu năng khách quan: Tỷ lệ chấp nhận đúng (TAR), Tỷ lệ chấp nhận sai (FAR), Tỷ lệ từ chối sai (FRR), Điểm F1-Score, Thời gian xây dựng chỉ mục (Build Time), Dung lượng RAM tiêu thụ thực tế (Resident Set Size - RSS), Độ trễ truy vấn trung bình (Latency tính bằng mili-giây), Thông lượng truy vấn (QPS), Tỷ lệ nén dữ liệu đĩa (Compression Ratio) và Độ trễ đầu-cuối P95 (End-to-End Latency).")
    add_p(doc, "3. Phương pháp Thiết kế Hệ thống Hướng Dữ liệu lớn (Big Data Architecture Design): Tiếp cận thiết kế hệ thống theo mô hình Lambda/Kappa thu nhỏ, áp dụng kỹ thuật giải phóng trạng thái bộ đệm với Event-Time Watermarking và lưu trữ hướng cột Parquet để tối ưu hóa khả năng đọc quét theo cột (Columnar Projection Pushdown).")

    # --------------------------------------------------------------------------
    # 5. Ý NGHĨA KHOA HỌC VÀ THỰC TIỄN
    # --------------------------------------------------------------------------
    add_h2(doc, "5. Ý nghĩa khoa học và thực tiễn của đề tài")
    add_p(doc, "Về mặt ý nghĩa khoa học: Đề tài đóng góp một giải pháp kiến trúc lai mẫu mực giải quyết mối tương quan phức tạp giữa độ chính xác nhận diện của mô hình học sâu và khả năng mở rộng dữ liệu lớn. Công trình làm sáng tỏ cơ chế hoạt động của thuật toán Asymmetric Distance Computation (ADC) trong lượng tử hóa tích khi kết hợp với các vector đặc trưng siêu cầu, đồng thời cung cấp các dẫn chứng thực nghiệm xác thực đường cong đánh đổi Pareto giữa Recall và Latency khi biến thiên các siêu tham số chỉ mục.")
    add_p(doc, "Về mặt ý nghĩa thực tiễn: Đề tài cung cấp một giải pháp khả thi, sẵn sàng ứng dụng thực tế với chi phí triển khai cực thấp. Các tổ chức, nhà máy, trường học hoàn toàn có thể tận dụng hàng trăm camera quan sát sẵn có để nâng cấp thành hệ thống giám sát an ninh và điểm danh tự động thông minh. Mức tiết kiệm 96.3% bộ nhớ RAM của chỉ mục IVF-PQ cho phép một máy chủ thông thường cấu hình 32 GB RAM có thể phục vụ cơ sở dữ liệu hàng trăm triệu người mà không cần đầu tư các cụm siêu máy tính đắt đỏ.")

    # --------------------------------------------------------------------------
    # 6. BỐ CỤC CỦA ĐỒ ÁN
    # --------------------------------------------------------------------------
    add_h2(doc, "6. Bố cục của quyển báo cáo")
    add_p(doc, "Quyển báo cáo đồ án được cấu trúc thành 3 chương nội dung chính, phần kết luận và phụ lục như sau:")
    add_p(doc, "• CHƯƠNG 1: TỔNG QUAN BÀI TOÁN VÀ CƠ SỞ LÝ THUYẾT: Trình bày chi tiết đặc trưng 5Vs của bài toán dưới góc độ Big Data; lịch sử tiến hóa của các mô hình trích xuất đặc trưng sâu từ DeepFace đến ArcFace; khảo cứu các cấu trúc chỉ mục tìm kiếm vector chiều cao (ANN); tổng quan công nghệ xử lý luồng Kafka, Spark và Data Lake Parquet; đối sánh các công trình quốc tế và xác định khoảng trống nghiên cứu.")
    add_p(doc, "• CHƯƠNG 2: PHƯƠNG PHÁP NGHIÊN CỨU VÀ KIẾN TRÚC HỆ THỐNG LAI (Trọng tâm 1): Phân tích chi tiết kiến trúc lai 4 tầng; phương pháp thu nhận RTSP và lọc mờ Laplacian; phương pháp phát hiện RetinaFace và căn chỉnh Affine 5 điểm mốc; cơ sở toán học ArcFace trên siêu cầu đơn vị; chứng minh tương đương Cosine và Euclid bình phương; phân tích chuyên sâu các thuật toán IndexIVFFlat, IndexIVFPQ nén 32x và IndexHNSW; quy trình xử lý luồng Kafka và Spark Streaming với cơ chế Stateful Deduplication.")
    add_p(doc, "• CHƯƠNG 3: THỰC HIỆN VÀ THỰC NGHIỆM ĐỊNH LƯỢNG (Trọng tâm 2): Mô tả môi trường phần cứng, 3 bộ dữ liệu thực nghiệm; quy trình tiền xử lý 4 bước; trình bày chi tiết kết quả, bảng số liệu và biểu đồ phân tích cho 5 kịch bản thực nghiệm định lượng; thảo luận và bài học kinh nghiệm triển khai.")
    add_p(doc, "• KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN: Tổng kết các đóng góp, nhìn nhận thẳng thắn các hạn chế hiện tại và đề xuất hướng mở rộng (Face Anti-Spoofing, Milvus/Qdrant phân tán trên Kubernetes).")
    add_p(doc, "• TÀI LIỆU THAM KHẢO & PHỤ LỤC: Danh mục 25 tài liệu tham khảo chuẩn IEEE và phụ lục mã nguồn cốt lõi của hệ thống.")
