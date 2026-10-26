"""
Chương Phần Đầu: Trang bìa, Lời cam đoan, Lời cảm ơn, Tóm tắt (Vi & En), Mục lục, Danh mục
"""

from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from .style_utils import add_p, add_h1, add_h2, set_cell_background, set_cell_margins

def generate_front_matter(doc):
    # ==============================================================================
    # 1. TRANG BÌA CHÍNH (MAIN COVER PAGE)
    # ==============================================================================
    # Tạo bảng viền khung đôi nghệ thuật bao quanh trang bìa
    table_cover = doc.add_table(rows=1, cols=1)
    table_cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell_cover = table_cover.cell(0, 0)
    tcPr = cell_cover._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="double" w:sz="18" w:space="0" w:color="0E7490"/>'
        f'<w:left w:val="double" w:sz="18" w:space="0" w:color="0E7490"/>'
        f'<w:bottom w:val="double" w:sz="18" w:space="0" w:color="0E7490"/>'
        f'<w:right w:val="double" w:sz="18" w:space="0" w:color="0E7490"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    set_cell_margins(cell_cover, top=300, bottom=300, left=300, right=300)

    p = cell_cover.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH\nTRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(14, 116, 144)

    p_sub = cell_cover.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(2)
    p_sub.paragraph_format.space_after = Pt(30)
    r_sub = p_sub.add_run("KHOA CÔNG NGHỆ THÔNG TIN / KHOA HỌC DỮ LIỆU")
    r_sub.bold = True
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(12)

    p_type = cell_cover.add_paragraph()
    p_type.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_type.paragraph_format.space_before = Pt(20)
    p_type.paragraph_format.space_after = Pt(15)
    r_type = p_type.add_run("BÁO CÁO ĐỒ ÁN MÔN HỌC\nPHÂN TÍCH DỮ LIỆU LỚN (BIG DATA ANALYTICS)")
    r_type.bold = True
    r_type.font.name = 'Times New Roman'
    r_type.font.size = Pt(14)
    r_type.font.color.rgb = RGBColor(15, 23, 42)

    p_title = cell_cover.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(25)
    p_title.paragraph_format.space_after = Pt(25)
    p_title.paragraph_format.line_spacing = 1.3
    r_title = p_title.add_run(
        "XÂY DỰNG KIẾN TRÚC LAI KẾT HỢP MÔ HÌNH ĐẶC TRƯNG SÂU ARCFACE "
        "VÀ CHỈ MỤC LƯỢNG TỬ HÓA VECTOR PHÂN TÁN (IVF-PQ/HNSW) "
        "CHO BÀI TOÁN NHẬN DIỆN KHUÔN MẶT VÀ PHÂN TÍCH SỰ KIỆN ĐA CAMERA THỜI GIAN THỰC"
    )
    r_title.bold = True
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(16)
    r_title.font.color.rgb = RGBColor(14, 116, 144)

    p_eng = cell_cover.add_paragraph()
    p_eng.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_eng.paragraph_format.space_before = Pt(5)
    p_eng.paragraph_format.space_after = Pt(45)
    r_eng = p_eng.add_run(
        "(Building a Hybrid Architecture Combining Deep ArcFace Representation and Distributed "
        "Vector Quantization Indexing (IVF-PQ/HNSW) for Real-Time Multi-Camera Face Recognition "
        "and Event Stream Analytics)"
    )
    r_eng.italic = True
    r_eng.font.name = 'Times New Roman'
    r_eng.font.size = Pt(11)
    r_eng.font.color.rgb = RGBColor(100, 116, 139)

    p_info = cell_cover.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_info.paragraph_format.left_indent = Inches(0.8)
    p_info.paragraph_format.space_before = Pt(20)
    p_info.paragraph_format.space_after = Pt(6)
    p_info.paragraph_format.line_spacing = 1.3
    r_info = p_info.add_run(
        "Giảng viên hướng dẫn:\tThS. Hà Minh Tân\n"
        "Mã lớp học phần:\t\t09-DS200.G11.CN2.TTNT\n"
        "Nhóm sinh viên thực hiện:\tNhóm G11\n"
        "Sinh viên đại diện:\t\tTrần Đình Tiễn\t\tMSSV: 25210216\n"
        "Thành viên nhóm:\t\tPhan Minh Nhân\tMSSV: 25210153\n"
        "\t\t\t\tNgô Gia Bảo\t\tMSSV: 25210061"
    )
    r_info.font.name = 'Times New Roman'
    r_info.font.size = Pt(12)

    p_bottom = cell_cover.add_paragraph()
    p_bottom.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_bottom.paragraph_format.space_before = Pt(40)
    p_bottom.paragraph_format.space_after = Pt(10)
    r_bottom = p_bottom.add_run("TP. HỒ CHÍ MINH, THÁNG 10 NĂM 2026")
    r_bottom.bold = True
    r_bottom.font.name = 'Times New Roman'
    r_bottom.font.size = Pt(12)

    # ==============================================================================
    # 2. LỜI CAM ĐOAN (PLEDGE)
    # ==============================================================================
    doc.add_page_break()
    p_pledge_h = doc.add_paragraph()
    p_pledge_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_pledge_h.paragraph_format.space_before = Pt(20)
    p_pledge_h.paragraph_format.space_after = Pt(15)
    r = p_pledge_h.add_run("LỜI CAM ĐOAN")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(14, 116, 144)

    add_p(doc, "Chúng tôi xin cam đoan rằng toàn bộ nội dung được trình bày trong quyển Báo cáo Đồ án môn học Phân tích Dữ liệu lớn này là kết quả nghiên cứu, thử nghiệm và hiện thực hóa thực chất của tập thể Nhóm G11 dưới sự định hướng khoa học tận tình của ThS. Hà Minh Tân.")
    add_p(doc, "Tất cả các số liệu thực nghiệm, bảng đối sánh, đường cong đặc tính TAR/FAR, độ trễ tìm kiếm mili-giây, thông lượng xử lý sự kiện Spark Streaming và biểu đồ lưu trữ Data Lake Parquet đều được thu thập một cách trung thực từ các kịch bản chạy thực tế trên hệ thống máy tính của nhóm.")
    add_p(doc, "Các đoạn trích dẫn lý thuyết, công thức toán học và tài liệu tham khảo đều được ghi chú nguồn gốc rõ ràng, minh bạch theo đúng quy chuẩn trích dẫn khoa học IEEE. Nhóm chúng tôi hoàn toàn chịu trách nhiệm trước Nhà trường và Giảng viên về tính nguyên bản và liêm chính học thuật của đồ án này.")

    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig.paragraph_format.space_before = Pt(30)
    p_sig.paragraph_format.space_after = Pt(4)
    r_sig = p_sig.add_run("TP. Hồ Chí Minh, ngày 20 tháng 10 năm 2026\nĐại diện nhóm tác giả\n\n\n\n")
    r_sig.italic = True
    r_sig.font.name = 'Times New Roman'
    r_sig.font.size = Pt(12)
    r_name = p_sig.add_run("Tập thể Nhóm G11")
    r_name.bold = True
    r_name.font.name = 'Times New Roman'
    r_name.font.size = Pt(12)

    # ==============================================================================
    # 3. LỜI CẢM ƠN (ACKNOWLEDGMENT)
    # ==============================================================================
    doc.add_page_break()
    p_ack_h = doc.add_paragraph()
    p_ack_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ack_h.paragraph_format.space_before = Pt(20)
    p_ack_h.paragraph_format.space_after = Pt(15)
    r = p_ack_h.add_run("LỜI CẢM ƠN")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(14, 116, 144)

    add_p(doc, "Lời đầu tiên, tập thể Nhóm G11 xin được bày tỏ lòng biết ơn sâu sắc và chân thành nhất tới Thầy Hà Minh Tân - Giảng viên phụ trách môn học Phân tích Dữ liệu lớn (Big Data Analytics). Trong suốt quá trình học tập và nghiên cứu thực hiện đồ án, Thầy đã không ngừng truyền cảm hứng học thuật, tận tình định hướng đề tài, gợi mở các phương pháp giải quyết bài toán nghẽn cổ chai dữ liệu lớn và đưa ra những lời nhận xét chuyên môn vô cùng quý giá.")
    add_p(doc, "Chúng em cũng xin gửi lời cảm ơn trân trọng tới Ban Giám hiệu, Khoa Công nghệ Thông tin và Bộ môn Khoa học Dữ liệu - Trường Đại học Công nghệ Thông tin (ĐHQG-HCM) đã tạo môi trường học tập tiên tiến, trang bị hệ thống máy móc, tài nguyên học liệu số phong phú để chúng em có điều kiện thực hành và nghiên cứu những công nghệ Dữ liệu lớn hiện đại nhất.")
    add_p(doc, "Dù nhóm đã nỗ lực hết mình với tinh thần nghiêm túc và cầu thị cao nhất, đồ án khó tránh khỏi những thiếu sót nhất định do giới hạn về thời gian và tài nguyên hạ tầng. Chúng em rất mong nhận được những ý kiến đóng góp, chỉ bảo quý báu của Thầy và Hội đồng thẩm định để đề tài tiếp tục được hoàn thiện và nâng cao trong các giai đoạn phát triển tiếp theo.")

    # ==============================================================================
    # 4. TÓM TẮT ĐỒ ÁN (ABSTRACT TIẾNG VIỆT & TIẾNG ANH)
    # ==============================================================================
    doc.add_page_break()
    p_ab_vi = doc.add_paragraph()
    p_ab_vi.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ab_vi.paragraph_format.space_before = Pt(15)
    p_ab_vi.paragraph_format.space_after = Pt(10)
    r = p_ab_vi.add_run("TÓM TẮT ĐỒ ÁN")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(14, 116, 144)

    add_p(doc, "Đồ án nghiên cứu và hiện thực hóa một Kiến trúc Lai 4 tầng (4-Tier Hybrid Architecture) kết hợp hài hòa giữa mô hình Trí tuệ nhân tạo thị giác máy tính và hệ sinh thái Xử lý Dữ liệu lớn phân tán nhằm giải quyết triệt để hai bài toán thực tế: (1) Tận dụng hạ tầng Camera IP chuẩn RTSP sẵn có tại các cơ quan, nhà máy mà không cần đầu tư AI Camera đắt tiền; và (2) Khắc phục điểm nghẽn cổ chai tính toán (Scalability Bottleneck) khi mở rộng quy mô lên hàng triệu vector đặc trưng và hàng trăm luồng video đồng thời.")
    add_p(doc, "Ở tầng biểu diễn đặc trưng, hệ thống tích hợp RetinaFace căn chỉnh Affine 5 điểm mốc và mô hình ArcFace ánh xạ khuôn mặt vào vector chuẩn hóa 512 chiều trên mặt siêu cầu đơn vị. Nhóm đã chứng minh toán học sự tương đương giữa khoảng cách Euclid bình phương và độ đo Cosine Similarity, làm cơ sở ứng dụng các chỉ mục tìm kiếm xấp xỉ (ANN) tối ưu phần cứng trên thư viện FAISS. Bằng cách áp dụng kỹ thuật Phân cụm Đảo ngược (IVF) và Lượng tử hóa Tích (Product Quantization - PQ), hệ thống nén dung lượng bộ nhớ RAM tới 96.3% (từ 2.048 MB xuống chỉ còn 76.2 MB cho 1 triệu khuôn mặt) và duy trì độ trễ đối sánh dưới 0.45 ms/khuôn mặt. Ở tầng dữ liệu lớn, cụm Apache Kafka và PySpark Structured Streaming với cơ chế khử trùng lặp trạng thái (Stateful Deduplication) cho phép hấp thụ ổn định luồng sự kiện từ 10 đến 500 camera đồng thời với độ trễ P95 đầu-cuối dưới 3.5 giây. Dữ liệu sau đó được lưu trữ trên Data Lake định dạng Apache Parquet nén Snappy, giúp tiết kiệm 80.5% dung lượng đĩa và tăng tốc truy vấn phân tích tổng hợp gấp 7.8 lần so với định dạng JSON, mở ra khả năng truy vết hành trình liên camera (Cross-Camera Tracking) và phát hiện bất thường thời gian thực.")
    add_p(doc, "Từ khóa: Nhận diện khuôn mặt đa camera, ArcFace, Lượng tử hóa tích (Product Quantization), FAISS, Apache Spark Streaming, Apache Parquet, Data Lake, Big Data Analytics.", italic=True, font_size=11.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    p_ab_en = doc.add_paragraph()
    p_ab_en.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ab_en.paragraph_format.space_before = Pt(15)
    p_ab_en.paragraph_format.space_after = Pt(10)
    r = p_ab_en.add_run("ABSTRACT")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(14, 116, 144)

    add_p(doc, "This project proposes and implements a comprehensive 4-Tier Hybrid Architecture integrating deep computer vision representations with distributed Big Data stream processing to address two practical challenges: (1) Leveraging pre-installed commodity RTSP IP cameras without investing in expensive dedicated AI cameras; and (2) Eliminating the computational scalability bottleneck when querying across millions of 512-dimensional facial feature vectors under high-velocity camera streams.")
    add_p(doc, "At the feature representation tier, RetinaFace with 5-point affine alignment is combined with pretrained ArcFace to map facial images onto the unit hypersphere in R^512. We provide a rigorous mathematical proof demonstrating the exact linear equivalence between squared Euclidean distance and Cosine Similarity, unlocking the full potential of hardware-accelerated Approximate Nearest Neighbor (ANN) index structures in FAISS. By employing Inverted File indexing (IVF) and Product Quantization (PQ), the system achieves a 96.3% reduction in RAM footprint (compressing 1,000,000 vectors from 2,048 MB down to 76.2 MB) while maintaining sub-millisecond query latency (< 0.45 ms per face). At the distributed stream analytics tier, an Apache Kafka and PySpark Structured Streaming pipeline incorporates event-time watermarking and stateful deduplication to reliably ingest events from 10 up to 500 concurrent camera feeds with end-to-end P95 latency below 3.5 seconds. Historical events persisted in an Apache Parquet Data Lake achieve an 80.5% disk compression ratio and a 7.8x query speedup over raw JSON Lines, enabling real-time cross-camera trajectory tracking and spatiotemporal anomaly detection.")
    add_p(doc, "Keywords: Multi-Camera Face Recognition, ArcFace, Product Quantization, FAISS, Apache Spark Streaming, Apache Parquet, Data Lake, Big Data Analytics.", italic=True, font_size=11.5)

    # ==============================================================================
    # 5. MỤC LỤC TỰ ĐỘNG & DANH MỤC
    # ==============================================================================
    doc.add_page_break()
    p_toc_h = doc.add_paragraph()
    p_toc_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_h.paragraph_format.space_before = Pt(20)
    p_toc_h.paragraph_format.space_after = Pt(15)
    r = p_toc_h.add_run("MỤC LỤC CHI TIẾT")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.color.rgb = RGBColor(14, 116, 144)

    toc_items = [
        ("LỜI CAM ĐOAN", "ii"),
        ("LỜI CẢM ƠN", "iii"),
        ("TÓM TẮT ĐỒ ÁN (TIẾNG VIỆT & TIẾNG ANH)", "iv"),
        ("DANH MỤC TỪ VIẾT TẮT", "vi"),
        ("DANH MỤC BẢNG BIỂU", "vii"),
        ("DANH MỤC HÌNH VẼ VÀ ĐỒ THỊ", "viii"),
        ("MỞ ĐẦU", "1"),
        ("   1. Tính cấp thiết và giá trị thực tiễn của đề tài", "1"),
        ("   2. Mục tiêu nghiên cứu (Tổng quát và Cụ thể)", "2"),
        ("   3. Đối tượng và phạm vi nghiên cứu", "3"),
        ("   4. Phương pháp luận nghiên cứu", "3"),
        ("   5. Ý nghĩa khoa học và thực tiễn của đề tài", "4"),
        ("   6. Bố cục của quyển báo cáo", "4"),
        ("CHƯƠNG 1: TỔNG QUAN BÀI TOÁN VÀ CƠ SỞ LÝ THUYẾT", "5"),
        ("   1.1. Tổng quan bài toán nhận diện khuôn mặt đa camera dưới góc độ Big Data (5Vs)", "5"),
        ("   1.2. Tổng quan các công nghệ trích xuất đặc trưng sâu (Deep Representation)", "7"),
        ("   1.3. Tổng quan các cấu trúc chỉ mục tìm kiếm Vector chiều cao (ANN Indexing)", "9"),
        ("   1.4. Tổng quan kiến trúc xử lý luồng phân tán và Data Lake", "11"),
        ("   1.5. Bảng đối sánh các công trình liên quan và Khoảng trống nghiên cứu (Research Gap)", "12"),
        ("CHƯƠNG 2: PHƯƠNG PHÁP NGHIÊN CỨU VÀ KIẾN TRÚC HỆ THỐNG LAI (TRỌNG TÂM 1)", "13"),
        ("   2.1. Kiến trúc Lai 4 tầng tổng thể (4-Tier Hybrid Architecture)", "13"),
        ("   2.2. Phương pháp thu nhận luồng RTSP và lọc chất lượng khung hình", "15"),
        ("   2.3. Phương pháp phát hiện và căn chỉnh khuôn mặt (RetinaFace & Affine 5-Point)", "17"),
        ("   2.4. Phương pháp trích xuất đặc trưng trên mặt siêu cầu với ArcFace", "19"),
        ("   2.5. Cơ sở toán học của Tìm kiếm Láng giềng Gần nhất Xấp xỉ (ANN) trên tập dữ liệu lớn", "21"),
        ("        2.5.1. Chứng minh toán học tương đương Cosine và Euclid bình phương", "21"),
        ("        2.5.2. Phân tích chỉ mục phân cụm đảo ngược Inverted File (IndexIVFFlat)", "23"),
        ("        2.5.3. Phân tích sâu thuật toán Lượng tử hóa Tích (IndexIVFPQ nén RAM 32 lần)", "24"),
        ("        2.5.4. Phân tích cấu trúc đồ thị Thế giới nhỏ Phân cấp (IndexHNSW)", "26"),
        ("   2.6. Phương pháp xử lý luồng sự kiện thời gian thực với Kafka và Spark Streaming", "27"),
        ("CHƯƠNG 3: THỰC HIỆN VÀ THỰC NGHIỆM ĐỊNH LƯỢNG (TRỌNG TÂM 2)", "29"),
        ("   3.1. Môi trường phần cứng và hệ sinh thái phần mềm cài đặt", "29"),
        ("   3.2. Mô tả chi tiết 3 bộ dữ liệu thực nghiệm (Dataset A, Dataset B, Dataset C)", "30"),
        ("   3.3. Quy trình tiền xử lý dữ liệu 4 bước chuẩn hóa", "32"),
        ("   3.4. Thiết kế và Phân tích 5 Kịch bản Thực nghiệm Định lượng", "33"),
        ("        3.4.1. Kịch bản 1: Đánh giá độ chính xác (TAR/FAR) và hiệu chỉnh ngưỡng Cosine", "33"),
        ("        3.4.2. Kịch bản 2: Đánh giá khả năng mở rộng quy mô vector FAISS từ 10K đến 1M", "35"),
        ("        3.4.3. Kịch bản 3: Phân tích đường cong đánh đổi Pareto giữa Recall và Latency", "38"),
        ("        3.4.4. Kịch bản 4: Đánh giá thông lượng và độ trễ Spark Streaming tải 500 camera", "40"),
        ("        3.4.5. Kịch bản 5: Đánh giá Data Lake Parquet và truy vết hành trình liên camera", "42"),
        ("   3.5. Thảo luận tổng hợp và bài học kinh nghiệm triển khai thực tế", "44"),
        ("KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", "45"),
        ("TÀI LIỆU THAM KHẢO CHUẨN IEEE", "47"),
        ("PHỤ LỤC: MÃ NGUỒN CỐT LÕI CỦA HỆ THỐNG", "49")
    ]

    for item, page in toc_items:
        p_toc = doc.add_paragraph()
        p_toc.paragraph_format.space_before = Pt(1)
        p_toc.paragraph_format.space_after = Pt(2)
        p_toc.paragraph_format.line_spacing = 1.15
        r_item = p_toc.add_run(item)
        r_item.font.name = 'Times New Roman'
        r_item.font.size = Pt(11.5)
        if "CHƯƠNG" in item or "MỞ ĐẦU" in item or "KẾT LUẬN" in item:
            r_item.bold = True
            r_item.font.color.rgb = RGBColor(14, 116, 144)

        # Tab fill dots
        dots = " " + "." * max(2, (68 - len(item))) + " "
        r_dots = p_toc.add_run(dots)
        r_dots.font.name = 'Times New Roman'
        r_dots.font.size = Pt(10)
        r_dots.font.color.rgb = RGBColor(148, 163, 184)

        r_page = p_toc.add_run(page)
        r_page.font.name = 'Times New Roman'
        r_page.font.size = Pt(11)
        r_page.bold = True

    # ==============================================================================
    # 6. DANH MỤC TỪ VIẾT TẮT, BẢNG BIỂU, HÌNH VẼ
    # ==============================================================================
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(15)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("DANH MỤC CÁC TỪ VIẾT TẮT")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(14, 116, 144)

    abbrevs = [
        ("AI", "Artificial Intelligence (Trí tuệ nhân tạo)"),
        ("ANN", "Approximate Nearest Neighbor (Tìm kiếm láng giềng gần nhất xấp xỉ)"),
        ("ADC", "Asymmetric Distance Computation (Tính toán khoảng cách bất đối xứng)"),
        ("API", "Application Programming Interface (Giao diện lập trình ứng dụng)"),
        ("FAR", "False Acceptance Rate (Tỷ lệ chấp nhận sai / Kẻ mạo danh lọt qua)"),
        ("FRR", "False Rejection Rate (Tỷ lệ từ chối sai người hợp lệ)"),
        ("FAISS", "Facebook AI Similarity Search (Thư viện tìm kiếm tương đồng vector của Meta)"),
        ("FPN", "Feature Pyramid Network (Mạng kim tự tháp đặc trưng trong RetinaFace)"),
        ("HNSW", "Hierarchical Navigable Small World (Đồ thị thế giới nhỏ phân cấp)"),
        ("IVF", "Inverted File (Cấu trúc tệp nghịch đảo / phân cụm không gian)"),
        ("LSH", "Locality-Sensitive Hashing (Băm nhạy cảm cục bộ)"),
        ("OLAP", "Online Analytical Processing (Xử lý phân tích trực tuyến trên Data Lake)"),
        ("PQ", "Product Quantization (Kỹ thuật lượng tử hóa tích phân rã không gian)"),
        ("QPS", "Queries Per Second (Số lượng truy vấn xử lý trên mỗi giây)"),
        ("RTSP", "Real-Time Streaming Protocol (Giao thức truyền luồng video thời gian thực)"),
        ("SSH", "Single Stage Headless (Mô-đun bối cảnh ngữ cảnh trong phát hiện mặt)"),
        ("TAR", "True Acceptance Rate (Tỷ lệ chấp nhận đúng người hợp lệ)"),
        ("SIMD", "Single Instruction, Multiple Data (Tập lệnh xử lý vector phần cứng AVX2/AVX512)")
    ]

    table_abb = doc.add_table(rows=len(abbrevs) + 1, cols=2)
    table_abb.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_abb.rows[0].cells[0].text = "Ký hiệu viết tắt"
    table_abb.rows[0].cells[1].text = "Thuật ngữ đầy đủ và Ý nghĩa"
    set_cell_background(table_abb.rows[0].cells[0], "0E7490")
    set_cell_background(table_abb.rows[0].cells[1], "0E7490")
    for c in table_abb.rows[0].cells:
        for r in c.paragraphs[0].runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (abbr, mean) in enumerate(abbrevs):
        r_cells = table_abb.rows[idx + 1].cells
        r_cells[0].text = abbr
        r_cells[1].text = mean
        bg = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        set_cell_background(r_cells[0], bg)
        set_cell_background(r_cells[1], bg)
        set_cell_margins(r_cells[0], top=80, bottom=80, left=100, right=100)
        set_cell_margins(r_cells[1], top=80, bottom=80, left=100, right=100)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Danh mục bảng biểu và hình vẽ
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(15)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("DANH MỤC CÁC BẢNG BIỂU VÀ HÌNH VẼ")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(14, 116, 144)

    list_tables = [
        "Bảng 1.1: Bảng đối sánh các công trình nghiên cứu nhận diện khuôn mặt và tìm kiếm vector",
        "Bảng 3.1: Môi trường phần cứng và các thư viện phần mềm trong hệ sinh thái thực nghiệm",
        "Bảng 3.2: Bảng cấu trúc dữ liệu lược đồ sự kiện giám sát đa camera (Event Stream Schema)",
        "Bảng 3.3: Kết quả hiệu chỉnh ngưỡng tương đồng Cosine (TAR, FAR, FRR) (Kịch bản 1)",
        "Bảng 3.4: Hiệu năng mở rộng quy mô chỉ mục vector từ 10.000 đến 1.000.000 vectors (Kịch bản 2)",
        "Bảng 3.5: Đánh đổi giữa Recall@K và Latency theo siêu tham số nprobe trên IVFPQ (Kịch bản 3)",
        "Bảng 3.6: Khả năng chịu tải và độ trễ xử lý luồng Spark từ 10 đến 500 Camera (Kịch bản 4)",
        "Bảng 3.7: So sánh dung lượng lưu trữ và thời gian truy vấn giữa Parquet và JSON Lines (Kịch bản 5)"
    ]
    for t in list_tables:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_before = Pt(1)
        p_t.paragraph_format.space_after = Pt(2)
        r = p_t.add_run(f"•  {t}")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    list_figs = [
        "Hình 1.1: Kiến trúc Lai 4 tầng tổng thể tích hợp luồng RTSP, mô hình AI ArcFace, chỉ mục FAISS và Spark Data Lake",
        "Hình 3.1: Đường cong đặc tính nhận diện khuôn mặt (TAR, FAR, FRR) theo biến thiên ngưỡng Cosine",
        "Hình 3.2: Đồ thị so sánh độ trễ truy vấn (ms) và thông lượng QPS theo quy mô vector từ 10K đến 1M",
        "Hình 3.3: Biểu đồ tiêu thụ bộ nhớ RAM minh họa mức tiết kiệm 96.3% RAM vượt trội của cấu trúc IVF-PQ",
        "Hình 3.4: Đường cong đánh đổi Pareto giữa Recall@1 / Recall@10 và Latency theo siêu tham số nprobe",
        "Hình 3.5: Thông lượng sự kiện và độ trễ đầu-cuối P95 của cụm Spark Structured Streaming theo tải camera"
    ]
    for f in list_figs:
        p_f = doc.add_paragraph()
        p_f.paragraph_format.space_before = Pt(1)
        p_f.paragraph_format.space_after = Pt(2)
        r = p_f.add_run(f"•  {f}")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
