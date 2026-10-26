"""
Script tự động khởi tạo Bộ 28 Slides Thuyết trình PowerPoint (.pptx) chuẩn học thuật
Tỷ lệ 16:9, màu sắc hiện đại, nhúng biểu đồ kết quả 300 DPI và đầy đủ Speaker Notes cho từng slide.
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Đảm bảo UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(BASE_DIR, "results", "figures")
DELIVERABLES_DIR = os.path.join(BASE_DIR, "deliverables")
os.makedirs(DELIVERABLES_DIR, exist_ok=True)

# Bảng màu chủ đạo (Executive Deep Navy & Tech Teal)
C_DARK_NAVY  = RGBColor(15, 23, 42)      # #0F172A
C_LIGHT_BG   = RGBColor(248, 250, 252)   # #F8FAFC
C_PRIMARY    = RGBColor(14, 116, 144)    # #0E7490 (Deep Cyan/Teal)
C_ACCENT     = RGBColor(249, 115, 22)    # #F97316 (Vibrant Orange)
C_TEXT_DARK  = RGBColor(30, 41, 59)      # #1E293B
C_TEXT_MUTED = RGBColor(100, 116, 139)   # #64748B
C_WHITE      = RGBColor(255, 255, 255)
C_CARD_BG    = RGBColor(255, 255, 255)
C_CARD_BORDER= RGBColor(226, 232, 240)

def set_slide_background(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, title_text, category_text="ĐỒ ÁN PHÂN TÍCH DỮ LIỆU LỚN - NHẬN DIỆN KHUÔN MẶT ĐA CAMERA"):
    # Header container
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = C_PRIMARY

    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = C_DARK_NAVY

def add_card(slide, left, top, width, height, title, content_bullets, border_color=C_CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = C_CARD_BG
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)

    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.25)
    tf.margin_right = Inches(0.25)
    tf.margin_top = Inches(0.2)
    tf.margin_bottom = Inches(0.2)

    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = C_PRIMARY
    p0.space_after = Pt(8)

    for item in content_bullets:
        p = tf.add_paragraph()
        p.text = f"•  {item}"
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(5)

def add_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = notes_text

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    print("[*] Bắt đầu khởi tạo 28 Slides thuyết trình bảo vệ đồ án...")

    # ==============================================================================
    # SLIDE 1: BÌA ĐỒ ÁN
    # ==============================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, C_DARK_NAVY)

    tb = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN - ĐHQG-HCM\nKHOA CÔNG NGHỆ THÔNG TIN / KHOA HỌC DỮ LIỆU"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = C_ACCENT
    p0.space_after = Pt(20)

    p1 = tf.add_paragraph()
    p1.text = "BÁO CÁO ĐỒ ÁN MÔN HỌC: PHÂN TÍCH DỮ LIỆU LỚN"
    p1.font.size = Pt(16)
    p1.font.color.rgb = C_WHITE
    p1.space_after = Pt(15)

    p2 = tf.add_paragraph()
    p2.text = "KIẾN TRÚC LAI KẾT HỢP MÔ HÌNH ĐẶC TRƯNG SÂU ARCFACE VÀ CHỈ MỤC LƯỢNG TỬ HÓA VECTOR PHÂN TÁN (IVF-PQ/HNSW) CHO BÀI TOÁN NHẬN DIỆN KHUÔN MẶT ĐA CAMERA THỜI GIAN THỰC"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.space_after = Pt(30)

    p3 = tf.add_paragraph()
    p3.text = "Giảng viên hướng dẫn: ThS. Hà Minh Tân\nNhóm sinh viên thực hiện: Nhóm G11 (Khoa CNTT - ĐHQG-HCM)"
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(203, 213, 225)

    add_speaker_notes(s1, "Kính chào Thầy Hà Minh Tân cùng toàn thể hội đồng. Nhóm G11 xin trình bày đồ án phân tích dữ liệu lớn về kiến trúc nhận diện khuôn mặt đa camera quy mô lớn kết hợp ArcFace và chỉ mục FAISS.")

    # ==============================================================================
    # SLIDE 2: ĐỘNG LỰC THỰC TIỄN - TẬN DỤNG HẠ TẦNG CAMERA RTSP
    # ==============================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, C_LIGHT_BG)
    add_header(s2, "Động lực Thực tiễn: Tận dụng Hạ tầng Camera IP Sẵn có")
    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Thực trạng Đầu tư Hạ tầng Camera",
             ["Hàng nghìn camera IP thông thường (chuẩn RTSP H.264) đã lắp đặt tại các tòa nhà, trường học, nhà máy.",
              "Chi phí thay mới bằng AI Camera chuyên dụng cực kỳ tốn kém ($500 – $2.000 / camera).",
              "Băng thông mạng và lưu trữ bị chiếm dụng lớn nếu truyền toàn bộ video thô về server xử lý.",
              "Nhu cầu cấp bách: Tận dụng luồng RTSP hiện hữu với thuật toán AI & Big Data tập trung."])
    add_card(s2, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Mục tiêu Giá trị Thực tiễn Mang lại",
             ["Biến mọi Camera IP chuẩn RTSP thành mắt thần an ninh thông minh mà không cần đổi phần cứng.",
              "Cơ chế lọc khung hình mờ (Laplacian variance) loại bỏ 60% dữ liệu suy biến ngay tại biên.",
              "Đảm bảo khả năng phục vụ liên tục 24/7 với chi phí vận hành hạ tầng tối thiểu.",
              "Khả năng mở rộng linh hoạt: Thêm camera mới chỉ cần khai báo URL luồng RTSP."])
    add_speaker_notes(s2, "Phân tích giá trị thực tiễn: Tận dụng hạ tầng camera IP thông thường thay vì mua AI camera đắt đỏ. Hệ thống chỉ xử lý các khung hình đạt chuẩn nhờ bộ lọc mờ.")

    # ==============================================================================
    # SLIDE 3: ĐIỂM NGHẼN CỔ CHAI KHI MỞ RỘNG QUY MÔ (BIG DATA BOTTLENECK)
    # ==============================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, C_LIGHT_BG)
    add_header(s3, "Điểm nghẽn Cổ chai khi Mở rộng Quy mô (Scalability Bottleneck)")
    add_card(s3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Khi Dữ liệu Tăng trưởng lên Triệu Thực thể",
             ["Mỗi khuôn mặt tương ứng 1 vector đặc trưng 512 chiều float32 (2.048 bytes).",
              "Quy mô cơ sở dữ liệu: 1.000.000 người tiêu tốn hơn 2 GB RAM chỉ để chứa dữ liệu vector thô.",
              "Độ phức tạp quét cạn (Brute-Force Flat Search): O(N * D) cho mỗi khuôn mặt xuất hiện.",
              "Tại N = 1.000.000, độ trễ tìm kiếm vọt lên 40 - 100 ms/khuôn mặt, hệ thống sụp đổ."])
    add_card(s3, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Yêu cầu Đặt ra cho Hệ thống Lớn",
             ["Giảm dung lượng RAM ít nhất 10 - 30 lần để máy chủ phổ thông có thể chịu tải hàng triệu người.",
              "Duy trì độ trễ đối sánh dưới 1 ms/khuôn mặt để phục vụ luồng RTSP 30 FPS thời gian thực.",
              "Đảm bảo độ chính xác Recall@1 không bị suy giảm đáng kể so với phương pháp vét cạn.",
              "Không cần huấn luyện lại mạng nơ-ron (Zero-Retraining) khi thêm danh tính mới vào kho dữ liệu."])
    add_speaker_notes(s3, "Phân tích điểm nghẽn cổ chai tính toán: Quét cạn O(N*D) khiến độ trễ tăng vọt khi đạt triệu người. Cần kỹ thuật nén lượng tử hóa và tìm kiếm xấp xỉ.")

    # ==============================================================================
    # SLIDE 4: MỤC TIÊU VÀ PHẠM VI NGHIÊN CỨU
    # ==============================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, C_LIGHT_BG)
    add_header(s4, "Mục tiêu Nghiên cứu và Phạm vi Đề tài")
    add_card(s4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Mục tiêu Cụ thể của Đề tài",
             ["Xây dựng Kiến trúc Lai 4 tầng kết hợp AI và Big Data Pipeline hoàn chỉnh.",
              "Nghiên cứu cơ sở toán học trên mặt siêu cầu đơn vị và chứng minh tương đương Cosine - Euclid.",
              "Ứng dụng Inverted File (IVF) và Product Quantization (PQ) trên FAISS nén RAM 32 lần.",
              "Thiết lập pipeline Apache Kafka + Spark Structured Streaming chịu tải 10 - 500 camera."])
    add_card(s4, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Phạm vi Thực nghiệm và Đóng gói",
             ["Thực nghiệm định lượng trên 3 tập dữ liệu: Khuôn mặt đa góc, 1M Vector 512D, 5M log sự kiện.",
              "Đo đạc 5 kịch bản thực nghiệm chuyên sâu: TAR/FAR, Scalability, Pareto, Spark, Parquet.",
              "Bàn giao trọn gói: Quyển Báo cáo Word > 40 trang, Slide 28 trang, Code sạch và Demo RTSP."])
    add_speaker_notes(s4, "Mục tiêu và phạm vi đề tài: Hoàn thành trọn vẹn cả 4 tầng kiến trúc và kiểm chứng qua 5 kịch bản thực nghiệm định lượng.")

    # ==============================================================================
    # SLIDE 5: ĐẶC TRƯNG 5Vs CỦA BIG DATA TRONG BÀI TOÁN
    # ==============================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, C_LIGHT_BG)
    add_header(s5, "Bài toán dưới Lăng kính Dữ liệu lớn (Mô hình 5Vs)")
    add_card(s5, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8),
             "Volume & Velocity",
             ["Volume: Hàng triệu vector 512-D, hàng chục GB sự kiện giám sát mỗi ngày.",
              "Velocity: Hàng trăm luồng video RTSP 25-30 FPS; hàng nghìn sự kiện/giây đổ về Kafka.",
              "Đòi hỏi kiến trúc xử lý phân tán và nén dữ liệu cột tối ưu."])
    add_card(s5, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8),
             "Variety & Veracity",
             ["Variety: Đa dạng định dạng từ luồng video H.264/RTSP, JSON event log, đến Apache Parquet.",
              "Veracity: Độ tin cậy ảnh bị ảnh hưởng bởi mờ chuyển động, góc nghiêng, ánh sáng ngược.",
              "Giải quyết bằng bộ lọc Laplacian và căn chỉnh Affine 5 điểm mốc."])
    add_card(s5, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8),
             "Value (Giá trị mang lại)",
             ["Cảnh báo tức thời đối tượng nằm trong danh sách đen (Blacklist) với độ trễ dưới 1 giây.",
              "Tự động điểm danh hàng vạn cán bộ công nhân viên không cần chạm.",
              "Truy vết lộ trình di chuyển liên camera (Cross-Camera Tracking) trên Data Lake."])
    add_speaker_notes(s5, "Phân tích 5Vs của Dữ liệu lớn: Bài toán thỏa mãn đầy đủ Volume, Velocity, Variety, Veracity và mang lại Value thực tế cao.")

    # ==============================================================================
    # SLIDE 6: TIẾN HÓA MÔ HÌNH TRÍCH XUẤT ĐẶC TRƯNG KHUÔN MẶT
    # ==============================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, C_LIGHT_BG)
    add_header(s6, "Tiến hóa Công nghệ Trích xuất Đặc trưng Sâu (Deep Representation)")
    add_card(s6, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Từ Softmax đến Triplet Loss",
             ["DeepFace (2014): Dùng hàm Softmax truyền thống, số lượng tham số bùng nổ theo số lớp danh tính.",
              "FaceNet (2015): Sử dụng Triplet Loss tối ưu khoảng cách Euclid cục bộ giữa Anchor, Positive, Negative.",
              "Hạn chế FaceNet: Khó khăn trong việc khai phá mẫu khó (Semi-hard mining), hội tụ chậm trên tập dữ liệu lớn."])
    add_card(s6, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Bước đột phá: ArcFace trên Mặt Siêu Cầu",
             ["SphereFace & CosFace: Đưa biên góc vào hàm mất mát để tối ưu độ tương đồng Cosine.",
              "ArcFace (2019): Bổ sung biên góc cộng tính trực tiếp vào góc đích: cos(θ + m).",
              "Phân tách rõ ràng giữa các lớp trên mặt siêu cầu, đạt độ chính xác 99.83% trên tập chuẩn LFW.",
              "Vector đặc trưng chuẩn hóa L2 có tính khái quát cao, không cần huấn luyện lại mạng."])
    add_speaker_notes(s6, "Lịch sử tiến hóa từ DeepFace, FaceNet đến ArcFace: ArcFace vượt trội nhờ cơ chế biên góc cộng tính trên mặt siêu cầu đơn vị.")

    # ==============================================================================
    # SLIDE 7: TỔNG QUAN TÌM KIẾM LÁNG GIỀNG GẦN NHẤT XẤP XỈ (ANN)
    # ==============================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, C_LIGHT_BG)
    add_header(s7, "Tổng quan Chỉ mục Tìm kiếm Vector Chiều cao (ANN Indexing)")
    add_card(s7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Hạn chế của Cấu trúc Cổ điển",
             ["KD-Tree, Ball-Tree: Hoàn toàn mất tác dụng trong không gian 512 chiều do 'Lời nguyền số chiều'.",
              "LSH (Locality Sensitive Hashing): Tốn nhiều hàm băm và dung lượng bộ nhớ lớn để đạt Recall cao.",
              "Quét cạn (IndexFlatIP): Cho độ chính xác 100% nhưng không thể mở rộng quá 100.000 vectors."])
    add_card(s7, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Các Trụ cột Hiện đại trong Thư viện FAISS",
             ["Inverted File (IVF): Phân vùng không gian thành nlist cụm Voronoi; chỉ tìm kiếm trong nprobe cụm lân cận.",
              "Product Quantization (PQ): Phân rã vector thành m không gian con và nén thành mã byte 8-bit.",
              "HNSW: Xây dựng đồ thị phân cấp thế giới nhỏ, cho tốc độ tìm kiếm cận logarit O(log N)."])
    add_speaker_notes(s7, "Tổng quan các thuật toán ANN: KD-tree bất lực ở số chiều cao. IVF, PQ và HNSW là giải pháp hàng đầu trong xử lý Big Data vector.")

    # ==============================================================================
    # SLIDE 8: TỔNG QUAN XỬ LÝ LUỒNG VÀ DATA LAKE
    # ==============================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, C_LIGHT_BG)
    add_header(s8, "Tổng quan Công nghệ Xử lý Luồng Phân tán & Data Lake")
    add_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Apache Kafka & Spark Streaming",
             ["Apache Kafka: Bộ đệm thông điệp phân tán với cơ chế log phân vùng, chịu lỗi cao, thông lượng > 100k msg/s.",
              "PySpark Structured Streaming: Xử lý theo vi lô (Micro-batch), hỗ trợ mô hình thời gian sự kiện (Event-Time).",
              "Stateful Deduplication: Lưu trữ trạng thái tạm thời để khử trùng lặp sự kiện cùng đối tượng."])
    add_card(s8, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Định dạng Lưu trữ Cột Apache Parquet",
             ["Cấu trúc lưu trữ hướng cột tối ưu hóa các phép tính tổng hợp (OLAP Aggregation).",
              "Thuật toán nén Snappy / ZSTD giúp giảm 75 - 85% dung lượng đĩa so với JSON/CSV thô.",
              "Dictionary Encoding và Bit-Packing cho phép lọc dữ liệu mà không cần giải nén toàn bộ file."])
    add_speaker_notes(s8, "Tổng quan công nghệ luồng và Data Lake: Kafka đệm dữ liệu, Spark xử lý trạng thái và Parquet lưu trữ cột phục vụ phân tích.")

    # ==============================================================================
    # SLIDE 9: BẢNG ĐỐI SÁNH CÁC CÔNG TRÌNH VÀ RESEARCH GAP
    # ==============================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, C_LIGHT_BG)
    add_header(s9, "Đối sánh Nghiên cứu Liên quan & Khoảng trống Nghiên cứu")
    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Hạn chế của các Công trình Trước đây",
             ["Nhiều công trình chỉ tập trung cải tiến mô hình AI trên ảnh tĩnh, bỏ qua bài toán mở rộng triệu vector.",
              "Một số nghiên cứu dùng Milvus/FAISS độc lập nhưng thiếu tầng xử lý luồng sự kiện phân tán.",
              "Thiếu cơ chế lọc chất lượng khung hình RTSP dẫn tới lãng phí năng nguyên tính toán."])
    add_card(s9, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Khoảng trống Nghiên cứu Đề tài Giải quyết",
             ["Thiết lập Kiến trúc Lai 4 tầng hoàn chỉnh từ thu nhận video RTSP đến lưu trữ Data Lake.",
              "Kết hợp đồng thời nén RAM 32x (IVF-PQ) và duy trì độ trễ < 1ms trên hàng triệu thực thể.",
              "Tích hợp thuật toán khử trùng lặp có trạng thái và truy vết lộ trình liên camera thời gian thực."])
    add_speaker_notes(s9, "Khoảng trống nghiên cứu: Kết hợp toàn diện giữa mô hình ArcFace với kỹ thuật lượng tử hóa tích và pipeline phân tán Spark.")

    # ==============================================================================
    # SLIDE 10: KIẾN TRÚC LAI 4 TẦNG TỔNG THỂ (NHÚNG HÌNH 1)
    # ==============================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, C_LIGHT_BG)
    add_header(s10, "Kiến trúc Lai 4 tầng Tổng thể (4-Tier Architecture)")
    fig1_path = os.path.join(FIGURES_DIR, "fig1_system_architecture.png")
    if os.path.exists(fig1_path):
        s10.shapes.add_picture(fig1_path, Inches(0.8), Inches(1.7), width=Inches(11.7))
    add_speaker_notes(s10, "Trình bày sơ đồ kiến trúc 4 tầng: Tầng 1 thu nhận RTSP; Tầng 2 trích xuất ArcFace; Tầng 3 chỉ mục FAISS; Tầng 4 xử lý luồng Kafka, Spark và Parquet.")

    # ==============================================================================
    # SLIDE 11: TẦNG 1 - THU NHẬN RTSP VÀ LỌC MỜ LAPLACIAN
    # ==============================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, C_LIGHT_BG)
    add_header(s11, "Tầng 1: Thu nhận Luồng RTSP và Lọc Mờ Khung hình")
    add_card(s11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Toán tử Laplace và Đo độ Sắc nét",
             ["Toán tử Laplace: Δf = ∂²f/∂x² + ∂²f/∂y²; ma trận nhân tích chập [[0,1,0],[1,-4,1],[0,1,0]].",
              "Đo độ sắc nét bằng phương sai: σ²_Laplacian = Var(Δf).",
              "Khung hình mờ do chuyển động làm triệt tiêu các cạnh tần số cao => σ² giảm mạnh.",
              "Hệ thống thiết lập ngưỡng lọc σ² >= 120; loại bỏ ngay 50 - 70% khung hình suy biến."])
    add_card(s11, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Cơ chế Dynamic Frame Dropping",
             ["Camera IP truyền 25 - 30 FPS, khuôn mặt di chuyển chỉ cần phân tích 3 - 5 FPS.",
              "Bộ đệm vòng (Ring Buffer) tự động hủy các khung hình cũ khi hàng đợi xử lý quá tải.",
              "Đảm bảo hệ thống không bao giờ bị tích tụ độ trễ mạng (Network Latency Accumulation)."])
    add_speaker_notes(s11, "Tầng 1 giải thích chi tiết phương sai toán tử Laplacian và cơ chế bỏ khung hình chủ động giúp hệ thống luôn mượt mà ở 30 FPS.")

    # ==============================================================================
    # SLIDE 12: TẦNG 2 - RETINAFACE VÀ CĂN CHỈNH AFFINE 5 ĐIỂM
    # ==============================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, C_LIGHT_BG)
    add_header(s12, "Tầng 2: Phát hiện RetinaFace và Căn chỉnh Affine 5 Điểm")
    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "RetinaFace & Loss Đa nhiệm",
             ["Kiến trúc Feature Pyramid Network (FPN) kết hợp mô-đun bối cảnh SSH.",
              "Hàm mất mát đa nhiệm: L = L_cls + λ1 * L_box + λ2 * L_pts + λ3 * L_pixel.",
              "Xác định đồng thời Bounding Box và 5 điểm mốc: 2 mắt, đỉnh mũi, 2 khóe miệng."])
    add_card(s12, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Chuẩn hóa Hình học bằng Biến đổi Affine",
             ["Tìm ma trận Affine M ∈ ℝ²ˣ³ qua bài toán bình phương tối thiểu giữa 5 điểm mốc và tọa độ mẫu.",
              "Phép xoay và co giãn đưa khuôn mặt về tư thế chuẩn chính diện kích thước 112 x 112 pixels.",
              "Loại bỏ triệt để sai số do góc nghiêng đầu của người đi lại trước camera."])
    add_speaker_notes(s12, "Tầng 2 giải thích RetinaFace và thuật toán căn chỉnh Affine 5 điểm mốc, đảm bảo vector khuôn mặt bất biến trước các góc nghiêng đầu.")

    # ==============================================================================
    # SLIDE 13: TOÁN HỌC ARCFACE TRÊN MẶT SIÊU CẦU ĐƠN VỊ
    # ==============================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13, C_LIGHT_BG)
    add_header(s13, "Toán học ArcFace trên Mặt Siêu Cầu Đơn vị")
    add_card(s13, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Công thức Hàm Mất mát Biên Góc",
             ["Chuẩn hóa L2 trọng số ||W_j|| = 1 và đặc trưng ||x_i|| = 1 => W_j^T * x_i = cos(θ_j).",
              "Hàm mất mát ArcFace: L = - (1/B) * Σ log [ e^(s * cos(θ + m)) / (e^(s * cos(θ + m)) + Σ e^(s * cos θ_j)) ].",
              "Hệ số tỷ lệ s = 64 và biên góc cộng tính m = 0.5 rad (~ 28.6°).",
              "Tối đa hóa khoảng cách giữa các lớp (Inter-class) và co cụm nội bộ lớp (Intra-class)."])
    add_card(s13, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Tách biệt Training và Identification 1:N",
             ["Mô hình được huấn luyện trước (Pretrained) trên hàng triệu ảnh chuẩn (MS1MV2).",
              "Khi triển khai thực tế: Thêm người mới chỉ cần trích xuất vector 512D nạp vào FAISS.",
              "Không cần huấn luyện lại mạng nơ-ron (Zero-Retraining Cost), sẵn sàng mở rộng vô hạn."])
    add_speaker_notes(s13, "Phân tích công thức ArcFace: Chuẩn hóa L2 đưa đặc trưng lên siêu cầu, biên góc m=0.5 giúp phân biệt danh tính cực kỳ chính xác.")

    # ==============================================================================
    # SLIDE 14: CHỨNG MINH TƯƠNG ĐƯƠNG COSINE VÀ KHOẢNG CÁCH EUCLID
    # ==============================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14, C_LIGHT_BG)
    add_header(s14, "Chứng minh Tương đương Toán học: Cosine và Khoảng cách Euclid")
    add_card(s14, Inches(0.8), Inches(1.8), Inches(11.6), Inches(4.8),
             "Các Bước Chứng minh Toán học Chặt chẽ",
             ["Giả thiết: Cho hai vector u, v ∈ ℝ⁵¹² đã được chuẩn hóa L2 đơn vị: ||u||₂ = 1 và ||v||₂ = 1.",
              "Khai triển khoảng cách Euclid bình phương: ||u - v||₂² = (u - v)ᵀ (u - v) = ||u||₂² + ||v||₂² - 2 uᵀ v.",
              "Thay độ dài đơn vị vào: ||u - v||₂² = 1 + 1 - 2 (uᵀ v) = 2 - 2 * S_cos(u, v).",
              "Suy ra: S_cos(u, v) = 1 - (1/2) * ||u - v||₂².",
              "Hệ quả thực tiễn: Cặp vector có độ tương đồng Cosine lớn nhất CHÍNH LÀ cặp có khoảng cách Euclid nhỏ nhất!",
              "Ý nghĩa kỹ thuật: Cho phép sử dụng toàn bộ các cấu trúc chỉ mục L2 (như IndexIVFPQ) trên FAISS mà vẫn bảo toàn 100% bản chất so khớp góc của ArcFace."])
    add_speaker_notes(s14, "Điểm cốt lõi toán học: Chứng minh khoảng cách Euclid bình phương tỷ lệ nghịch tuyến tính với Cosine Similarity, cho phép tận dụng trọn vẹn chỉ mục L2.")

    # ==============================================================================
    # SLIDE 15: CHỈ MỤC PHÂN CỤM ĐẢO NGƯỢC (IVF) VÀ LƯỢNG TỬ HÓA TÍCH (PQ)
    # ==============================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15, C_LIGHT_BG)
    add_header(s15, "Tầng 3: Phân cụm Đảo ngược (IVF) và Lượng tử hóa Tích (PQ)")
    add_card(s15, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Inverted File (IVF) - Phân cụm Voronoi",
             ["Sử dụng K-Means chia không gian thành nlist = 1024 cụm Voronoi.",
              "Khi truy vấn: Chỉ quét nprobe cụm lân cận thay vì toàn bộ cơ sở dữ liệu.",
              "Giảm không gian tìm kiếm xuống (nprobe / nlist) = (16 / 1024) = 1.56% số lượng vector."])
    add_card(s15, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Product Quantization (PQ) - Nén RAM 32 Lần",
             ["Chia không gian ℝ⁵¹² thành m = 64 không gian con 8 chiều.",
              "Mỗi không gian con học 256 centroids (mã hóa bằng 8-bit = 1 byte).",
              "Mỗi vector 2.048 bytes được nén thành chuỗi 64 bytes => Tỷ lệ nén đúng 32 lần!",
              "Tra cứu Asymmetric Distance Computation (ADC) qua bảng tính sẵn, tốc độ cực nhanh."])
    add_speaker_notes(s15, "Giải thích IVF-PQ: IVF lọc cụm Voronoi, PQ nén 512 số thực thành 64 bytes, tiết kiệm 96% RAM và tìm kiếm siêu nhanh.")

    # ==============================================================================
    # SLIDE 16: CHỈ MỤC ĐỒ THỊ THẾ GIỚI NHỎ PHÂN CẤP (HNSW)
    # ==============================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16, C_LIGHT_BG)
    add_header(s16, "Tầng 3: Cấu trúc Đồ thị Phân cấp Thế giới nhỏ (HNSW)")
    add_card(s16, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Nguyên lý Hoạt động của HNSW",
             ["Xây dựng đồ thị phân tầng tương tự Skip-List: Tầng cao liên kết xa, tầng thấp liên kết gần.",
              "Tìm kiếm tham lam (Greedy Search): Nhảy nhanh ở tầng trên để tiếp cận vùng lân cận, sau đó đi xuống tầng đáy.",
              "Độ phức tạp tìm kiếm đạt mức cận logarit O(log N)."])
    add_card(s16, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Đặc tính và So sánh với IVF-PQ",
             ["Tham số cấu hình: M = 32 (số cạnh liên kết mỗi đỉnh), efSearch = 64.",
              "Ưu điểm: Đạt độ chính xác Recall@1 cao nhất trong các thuật toán ANN.",
              "Nhược điểm: Tốn thêm bộ nhớ RAM để lưu trữ danh sách cạnh đồ thị (tăng ~28% so với Flat)."])
    add_speaker_notes(s16, "Cấu trúc đồ thị HNSW: Tìm kiếm tham lam đa tầng cho Recall@1 cao nhất nhưng tiêu tốn RAM nhiều hơn IVF-PQ.")

    # ==============================================================================
    # SLIDE 17: TẦNG 4 - XỬ LÝ LUỒNG SPARK STREAMING VÀ DATA LAKE
    # ==============================================================================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17, C_LIGHT_BG)
    add_header(s17, "Tầng 4: Xử lý Luồng Spark Streaming & Khử Trùng Lặp Trạng thái")
    add_card(s17, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Kafka Ingestion & Watermarking",
             ["Khóa phân vùng MurmurHash2(CameraID) đảm bảo thứ tự thời gian cho từng camera.",
              "Spark Micro-batching với chu kỳ 1 giây.",
              "Cơ chế Watermarking 10 phút: wm = max(event_time) - 10m, tự động giải phóng trạng thái cũ."])
    add_card(s17, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Stateful Deduplication & Parquet Lake",
             ["Thuật toán khử trùng lặp có trạng thái: Gom các sự kiện của cùng 1 người trên 1 camera trong 5 giây.",
              "Giảm hơn 80% tải ghi dữ liệu không cần thiết xuống đĩa.",
              "Ghi xuống Data Lake Parquet nén Snappy phân vùng theo Zone/Date, sẵn sàng cho truy vấn SQL."])
    add_speaker_notes(s17, "Tầng 4 xử lý luồng: Spark micro-batch 1s, watermark 10m và khử trùng lặp khuôn mặt trong 5 giây trước khi ghi vào Data Lake.")

    # ==============================================================================
    # SLIDE 18: MÔI TRƯỜNG CÀI ĐẶT & 3 BỘ DỮ LIỆU THỰC NGHIỆM
    # ==============================================================================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18, C_LIGHT_BG)
    add_header(s18, "Môi trường Phần cứng & 3 Bộ Dữ liệu Thực nghiệm")
    add_card(s18, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8),
             "Môi trường Kiểm thử",
             ["CPU: Intel Core i7 16-Threads / RAM 32 GB / GPU NVIDIA RTX.",
              "Hệ sinh thái: Python 3.14, FAISS 1.15, PySpark 3.5, PyArrow 25.",
              "Hỗ trợ tập lệnh SIMD AVX2 tối ưu hóa tính toán ma trận."])
    add_card(s18, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8),
             "Dataset A & Dataset B",
             ["Dataset A: Tập kiểm thử nhận diện khuôn mặt đa camera (góc sáng, mờ chuyển động).",
              "Dataset B: Bộ vector 512-D L2-Normalized ở 4 mốc: 10K, 100K, 500K, 1M vectors.",
              "Kích thước mốc 1M vector thô: 2.048 MB."])
    add_card(s18, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8),
             "Dataset C (Event Logs)",
             ["500.000 đến 5.000.000 bản ghi sự kiện nhận diện đa camera.",
              "Schema 9 trường thuộc tính: event_id, timestamp, zone_id, camera_id, person_id, similarity...",
              "Phục vụ benchmark Kafka, Spark và Data Lake Parquet."])
    add_speaker_notes(s18, "Trình bày môi trường thực nghiệm và 3 bộ dữ liệu: Dataset A đo TAR/FAR; Dataset B triệu vector đo FAISS; Dataset C đo Spark & Parquet.")

    # ==============================================================================
    # SLIDE 19: PIPELINE TIỀN XỬ LÝ DỮ LIỆU 4 BƯỚC
    # ==============================================================================
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_background(s19, C_LIGHT_BG)
    add_header(s19, "Quy trình Tiền xử lý Dữ liệu 4 bước (Data Preprocessing Pipeline)")
    add_card(s19, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.8),
             "Bước 1: Lọc Laplacian",
             ["Chuyển ảnh xám.",
              "Tính phương sai Laplacian.",
              "Loại bỏ nếu σ² < 120.",
              "Tiết kiệm 60% tải trích xuất AI."])
    add_card(s19, Inches(3.7), Inches(1.8), Inches(2.7), Inches(4.8),
             "Bước 2: Căn chỉnh Affine",
             ["Định vị 5 điểm mốc.",
              "Giải Least Squares tìm ma trận M.",
              "Warp affine về 112x112.",
              "Bất biến góc nghiêng đầu."])
    add_card(s19, Inches(6.6), Inches(1.8), Inches(2.7), Inches(4.8),
             "Bước 3: Chuẩn hóa L2",
             ["Mô hình ArcFace xuất vector 512D.",
              "Chuẩn hóa: v = v / ||v||₂.",
              "Đưa vector về siêu cầu S⁵¹¹.",
              "Sẵn sàng cho Inner Product."])
    add_card(s19, Inches(9.5), Inches(1.8), Inches(2.7), Inches(4.8),
             "Bước 4: Ép kiểu Schema",
             ["Tạo StructType trên Spark.",
              "Ép kiểu Timestamp, String, Float.",
              "Loại bỏ bản ghi lỗi / null.",
              "Tối ưu lưu trữ cột Parquet."])
    add_speaker_notes(s19, "4 bước tiền xử lý chuẩn mực: Lọc mờ, căn chỉnh Affine, chuẩn hóa vector L2 và định kiểu dữ liệu Spark Schema.")

    # ==============================================================================
    # SLIDE 20: KỊCH BẢN 1 - ĐÁNH GIÁ TAR/FAR VÀ CHỌN NGƯỠNG (NHÚNG HÌNH 2)
    # ==============================================================================
    s20 = prs.slides.add_slide(blank_layout)
    set_slide_background(s20, C_LIGHT_BG)
    add_header(s20, "Kịch bản 1: Đánh giá TAR, FAR và Lựa chọn Ngưỡng Cosine")
    fig2_path = os.path.join(FIGURES_DIR, "fig2_roc_tar_far_curve.png")
    if os.path.exists(fig2_path):
        s20.shapes.add_picture(fig2_path, Inches(0.8), Inches(1.7), width=Inches(7.2))
    add_card(s20, Inches(8.3), Inches(1.7), Inches(4.2), Inches(5.2),
             "Phân tích Kết quả Ngưỡng τ",
             ["Tại τ = 0.40: TAR rất cao (98.6%) nhưng FAR lên tới 0.48% (quá nhiều kẻ giả mạo).",
              "Tại τ = 0.60: FAR cực thấp (0.0008%) nhưng TAR tụt xuống 78.4% (bỏ sót nhiều người hợp lệ).",
              "Điểm tối ưu đề xuất: τ = 0.50.",
              "TAR đạt 92.54% trong điều kiện khác camera thực tế.",
              "FAR chỉ là 0.021% (chỉ 2 trên 10.000 lần thử).",
              "Đây là ngưỡng vàng triển khai cho toàn bộ hệ thống."])
    add_speaker_notes(s20, "Phân tích Kịch bản 1: Lựa chọn ngưỡng Cosine 0.50 đạt cân bằng tối ưu giữa TAR 92.5% và FAR cực thấp 0.02%.")

    # ==============================================================================
    # SLIDE 21: KỊCH BẢN 2 - KHẢ NĂNG MỞ RỘNG FAISS (NHÚNG HÌNH 3)
    # ==============================================================================
    s21 = prs.slides.add_slide(blank_layout)
    set_slide_background(s21, C_LIGHT_BG)
    add_header(s21, "Kịch bản 2: Khả năng Mở rộng Chỉ mục FAISS từ 10K đến 1 Triệu Vector")
    fig3_path = os.path.join(FIGURES_DIR, "fig3_latency_qps_scaling.png")
    if os.path.exists(fig3_path):
        s21.shapes.add_picture(fig3_path, Inches(0.8), Inches(1.7), width=Inches(7.2))
    add_card(s21, Inches(8.3), Inches(1.7), Inches(4.2), Inches(5.2),
             "Hiệu năng tại Mốc 1.000.000 Vectors",
             ["IndexFlatIP (Vét cạn): Latency vọt lên 42.5 ms, QPS tụt còn 23 queries/s.",
              "IndexIVFFlat: Latency 1.85 ms, QPS đạt 540 queries/s (nhanh gấp 23 lần).",
              "IndexIVFPQ: Latency chỉ 0.42 ms, QPS đạt 2.380 queries/s (nhanh gấp 100 lần!).",
              "IndexHNSW32: Latency 0.38 ms, QPS đạt 2.630 queries/s.",
              "IVFPQ và HNSW hoàn toàn đáp ứng thời gian thực dưới 1 ms trên hàng triệu khuôn mặt."])
    add_speaker_notes(s21, "Phân tích Kịch bản 2: Khi cơ sở dữ liệu đạt 1 triệu người, IVFPQ và HNSW giữ độ trễ dưới 0.5ms, nhanh hơn 100 lần so với quét cạn.")

    # ==============================================================================
    # SLIDE 22: HIỆU QUẢ TIẾT KIỆM 96% BỘ NHỚ RAM CỦA IVF-PQ (NHÚNG HÌNH 4)
    # ==============================================================================
    s22 = prs.slides.add_slide(blank_layout)
    set_slide_background(s22, C_LIGHT_BG)
    add_header(s22, "Hiệu quả Tiết kiệm 96% Bộ nhớ RAM của Lượng tử hóa Tích (IVF-PQ)")
    fig4_path = os.path.join(FIGURES_DIR, "fig4_ram_consumption_comparison.png")
    if os.path.exists(fig4_path):
        s22.shapes.add_picture(fig4_path, Inches(0.8), Inches(1.7), width=Inches(7.2))
    add_card(s22, Inches(8.3), Inches(1.7), Inches(4.2), Inches(5.2),
             "Điểm Nhấn Tiết kiệm Tài nguyên",
             ["Tại quy mô 1.000.000 vector 512 chiều:",
              "• FlatIP tiêu tốn: 2.048 MB RAM.",
              "• HNSW tiêu tốn: 2.621 MB RAM (do lưu đồ thị).",
              "• IVFPQ tiêu tốn chỉ: 76.2 MB RAM!",
              "Tiết kiệm chính xác 96.3% bộ nhớ RAM.",
              "Một máy chủ phổ thông 32GB RAM có thể lưu trữ hơn 300 triệu khuôn mặt trên chỉ mục IVFPQ!"])
    add_speaker_notes(s22, "Điểm nhấn Kịch bản 2: IVFPQ nén 96.3% RAM, chỉ tốn 76MB cho 1 triệu người so với hơn 2GB của phương pháp thường.")

    # ==============================================================================
    # SLIDE 23: KỊCH BẢN 3 - ĐÁNH ĐỔI PARETO RECALL VÀ LATENCY (NHÚNG HÌNH 5)
    # ==============================================================================
    s23 = prs.slides.add_slide(blank_layout)
    set_slide_background(s23, C_LIGHT_BG)
    add_header(s23, "Kịch bản 3: Đánh đổi Pareto giữa Recall và Latency theo nprobe")
    fig5_path = os.path.join(FIGURES_DIR, "fig5_recall_vs_latency_pareto.png")
    if os.path.exists(fig5_path):
        s23.shapes.add_picture(fig5_path, Inches(0.8), Inches(1.7), width=Inches(7.2))
    add_card(s23, Inches(8.3), Inches(1.7), Inches(4.2), Inches(5.2),
             "Khảo sát Siêu tham số nprobe",
             ["nprobe = 1: Latency cực nhanh (0.08 ms) nhưng Recall@1 chỉ 68.2% (bỏ sót nhiều).",
              "nprobe = 128: Recall@1 đạt 96.1% nhưng Latency tăng lên 1.25 ms.",
              "Vùng Sweet-spot tối ưu: nprobe = 16 – 32.",
              "• Recall@1 đạt 92.8% – 94.5%.",
              "• Recall@10 đạt 98.4% – 99.1%.",
              "• Latency chỉ từ 0.32 – 0.45 ms/truy vấn."])
    add_speaker_notes(s23, "Phân tích Kịch bản 3: Đường cong Pareto xác định nprobe từ 16 đến 32 là điểm tối ưu tuyệt đối, đạt Recall@10 > 98.5% và Latency < 0.45ms.")

    # ==============================================================================
    # SLIDE 24: KỊCH BẢN 4 - HIỆU NĂNG LUỒNG SPARK STREAMING (NHÚNG HÌNH 6)
    # ==============================================================================
    s24 = prs.slides.add_slide(blank_layout)
    set_slide_background(s24, C_LIGHT_BG)
    add_header(s24, "Kịch bản 4: Hiệu năng Xử lý Luồng Spark khi Tải từ 10 đến 500 Camera")
    fig6_path = os.path.join(FIGURES_DIR, "fig6_spark_streaming_throughput.png")
    if os.path.exists(fig6_path):
        s24.shapes.add_picture(fig6_path, Inches(0.8), Inches(1.7), width=Inches(7.2))
    add_card(s24, Inches(8.3), Inches(1.7), Inches(4.2), Inches(5.2),
             "Thông lượng và Độ trễ Đầu-Cuối",
             ["Tại 100 Camera (1.000 sự kiện/s): Vi lô xử lý chỉ mất 0.54s, độ trễ P95 là 1.15s, Lag = 0.",
              "Tại 250 Camera (2.500 sự kiện/s): Vi lô 1.12s, độ trễ P95 là 2.10s, Lag = 0.",
              "Tại 500 Camera (5.000 sự kiện/s): Spark xử lý 4.985 sự kiện/s, độ trễ P95 là 3.45s.",
              "Hệ thống vận hành ổn định, không bị nghẽn hàng đợi Kafka."])
    add_speaker_notes(s24, "Phân tích Kịch bản 4: Spark Structured Streaming xử lý mượt mà tới 500 camera đồng thời với độ trễ P95 dưới 3.5 giây.")

    # ==============================================================================
    # SLIDE 25: KỊCH BẢN 5 - DATA LAKE PARQUET VÀ TRUY VẾT LIÊN CAMERA
    # ==============================================================================
    s25 = prs.slides.add_slide(blank_layout)
    set_slide_background(s25, C_LIGHT_BG)
    add_header(s25, "Kịch bản 5: Đánh giá Data Lake Parquet & Truy vết Hành trình")
    add_card(s25, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "So sánh Apache Parquet vs JSON Lines",
             ["Dung lượng đĩa (500.000 sự kiện):",
              "• JSON Lines thô: 68.4 MB.",
              "• Apache Parquet (Snappy): 13.3 MB (giảm 80.5% đĩa!).",
              "Thời gian truy vấn phân tích tổng hợp (OLAP):",
              "• JSON Lines: 0.62 giây.",
              "• Parquet (Columnar Pushdown): 0.08 giây (nhanh gấp 7.8 lần!)."])
    add_card(s25, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Truy vết Hành trình & Báo động Bất thường",
             ["Cross-Camera Trajectory Tracking: Tự động gom chuỗi sự kiện theo person_id và sắp xếp thời gian.",
              "Thuật toán Spatiotemporal Anomaly Detection:",
              "Phát hiện trường hợp 1 đối tượng xuất hiện ở 2 khu vực cách xa nhau trong dưới 2 giây (Spatiotemporal Impossible Jump).",
              "Cảnh báo tức thời nguy cơ gian lận thẻ hoặc giả mạo nhận diện."])
    add_speaker_notes(s25, "Phân tích Kịch bản 5: Parquet nén hơn 80% đĩa, truy vấn nhanh gấp gần 8 lần. Ứng dụng truy vết hành trình và phát hiện nhảy cóc bất thường.")

    # ==============================================================================
    # SLIDE 26: TỔNG KẾT ĐÓNG GÓP KHOA HỌC & THỰC TIỄN
    # ==============================================================================
    s26 = prs.slides.add_slide(blank_layout)
    set_slide_background(s26, C_LIGHT_BG)
    add_header(s26, "Tổng kết các Đóng góp Khoa học và Thực tiễn của Đồ án")
    add_card(s26, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Đóng góp về Khoa học & Phương pháp",
             ["Chứng minh chặt chẽ sự tương đương giữa khoảng cách Euclid và Cosine Similarity trên siêu cầu.",
              "Làm chủ cơ chế kết hợp giữa mô hình đặc trưng sâu ArcFace và chỉ mục lượng tử hóa tích IVF-PQ.",
              "Xác lập đường cong Pareto tối ưu siêu tham số nprobe cân bằng hoàn hảo giữa Recall và Latency."])
    add_card(s26, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Đóng góp về Thực tiễn & Kỹ thuật",
             ["Xây dựng hệ thống giải quyết bài toán tận dụng camera IP RTSP sẵn có, tiết kiệm hàng tỷ đồng phần cứng.",
              "Nén 96% dung lượng RAM, cho phép máy chủ thông thường phục vụ cơ sở dữ liệu hàng triệu người.",
              "Hiện thực hóa pipeline xử lý luồng Spark chịu tải 500 camera với Data Lake Parquet tối ưu."])
    add_speaker_notes(s26, "Tổng kết 4 đóng góp chính: Phương pháp toán học trên siêu cầu, kỹ thuật nén RAM 96%, kiến trúc tận dụng RTSP và pipeline luồng Spark.")

    # ==============================================================================
    # SLIDE 27: HẠN CHẾ & HƯỚNG PHÁT TRIỂN TƯƠNG LAI
    # ==============================================================================
    s27 = prs.slides.add_slide(blank_layout)
    set_slide_background(s27, C_LIGHT_BG)
    add_header(s27, "Hạn chế của Hệ thống và Hướng Nghiên cứu Mở rộng")
    add_card(s27, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Hạn chế Cần Hoàn thiện",
             ["Chưa tích hợp mô hình chống giả mạo khuôn mặt chuyên sâu (Face Anti-Spoofing / Liveness Detection).",
              "Chỉ mục FAISS hiện vận hành trên môi trường đơn node, chưa phân mảnh Sharding qua nhiều máy chủ vật lý.",
              "Chất lượng nhận diện ban đêm còn phụ thuộc vào đèn hồng ngoại của camera IP."])
    add_card(s27, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8),
             "Định hướng Phát triển Tiếp theo",
             ["Tích hợp Silent Liveness Detection phát hiện giả mạo bằng màn hình điện thoại hoặc ảnh in.",
              "Chuyển đổi chỉ mục vector sang cơ sở dữ liệu vector phân tán mã nguồn mở (Milvus hoặc Qdrant) trên Kubernetes.",
              "Tích hợp thuật toán Re-Identification toàn thân (Person Re-ID) khi khuôn mặt bị che khuất."])
    add_speaker_notes(s27, "Thẳng thắn nhìn nhận hạn chế về liveness và mở rộng phân tán. Hướng phát triển: Tích hợp Anti-spoofing và chuyển đổi sang cụm Milvus/Qdrant trên K8s.")

    # ==============================================================================
    # SLIDE 28: LỜI CẢM ƠN VÀ PHIÊN HỎI ĐÁP (Q&A)
    # ==============================================================================
    s28 = prs.slides.add_slide(blank_layout)
    set_slide_background(s28, C_DARK_NAVY)

    tb28 = s28.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(4.0))
    tf28 = tb28.text_frame
    tf28.word_wrap = True

    p0 = tf28.paragraphs[0]
    p0.text = "XIN CHÂN THÀNH CẢM ƠN THẦY HÀ MINH TÂN\nCÙNG QUÝ THẦY CÔ VÀ CÁC BẠN ĐÃ LẮNG NGHE!"
    p0.font.size = Pt(24)
    p0.font.bold = True
    p0.font.color.rgb = C_WHITE
    p0.space_after = Pt(25)

    p1 = tf28.add_paragraph()
    p1.text = "Nhóm G11 rất mong nhận được những góp ý, nhận xét quý báu từ Thầy và Hội đồng.\n\nSẴN SÀNG CHO PHIÊN HỎI ĐÁP (Q&A)"
    p1.font.size = Pt(16)
    p1.font.color.rgb = C_ACCENT

    add_speaker_notes(s28, "Nhóm xin chân thành cảm ơn Thầy Hà Minh Tân đã tận tình hướng dẫn. Nhóm xin trân trọng cảm ơn Hội đồng và sẵn sàng bước vào phần trả lời câu hỏi.")

    out_pptx = os.path.join(DELIVERABLES_DIR, "Slide_Bao_Ve_Do_An.pptx")
    prs.save(out_pptx)
    print(f"\n[THÀNH CÔNG] Đã tạo bộ 28 slides PowerPoint tại: {out_pptx}")

if __name__ == "__main__":
    build_presentation()
