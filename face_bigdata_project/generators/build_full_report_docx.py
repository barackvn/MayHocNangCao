"""
Bộ Sinh Quyển Báo cáo Đồ án Toàn diện (> 40 trang A4, mục tiêu 46-50 trang)
Tổng hợp toàn bộ 4 chương, bảng dữ liệu thực nghiệm, biểu đồ 300 DPI và chuyển đổi sang PDF.
"""

import os
import sys
from docx import Document
import win32com.client

# Đảm bảo UTF-8 cho console Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from report_chapters.style_utils import setup_document_styles
from report_chapters.chapter_front import generate_front_matter
from report_chapters.chapter_intro import generate_introduction
from report_chapters.chapter_1 import generate_chapter_1
from report_chapters.chapter_2 import generate_chapter_2
from report_chapters.chapter_3 import generate_chapter_3
from report_chapters.chapter_conclusion import generate_conclusion_and_references

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABLES_DIR = os.path.join(BASE_DIR, "results", "tables")
FIGURES_DIR = os.path.join(BASE_DIR, "results", "figures")
DELIVERABLES_DIR = os.path.join(BASE_DIR, "deliverables")
os.makedirs(DELIVERABLES_DIR, exist_ok=True)

def convert_docx_to_pdf(docx_path):
    """Chuyển đổi file .docx sang .pdf thông qua Microsoft Word COM Automation."""
    pdf_path = docx_path.replace(".docx", ".pdf")
    print(f"\n[*] Đang chuyển đổi {docx_path} sang định dạng PDF chuẩn bằng Microsoft Word...")

    word = None
    try:
        # Khởi động Microsoft Word ngầm
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        word.DisplayAlerts = False

        # Mở tài liệu Word
        doc = word.Documents.Open(os.path.abspath(docx_path))
        # Định dạng xuất PDF: wdFormatPDF = 17
        doc.SaveAs(os.path.abspath(pdf_path), FileFormat=17)
        doc.Close()
        print(f"[THÀNH CÔNG] Đã xuất file PDF chuẩn xác 100% tại: {pdf_path}")
    except Exception as e:
        print(f"[CẢNH BÁO] Không thể chuyển đổi tự động sang PDF bằng COM: {e}")
        print("Có thể chuyển đổi thủ công bằng cách mở file Word và chọn Save As PDF.")
    finally:
        if word:
            try:
                word.Quit()
            except Exception:
                pass

def build_full_report():
    print("="*80)
    print("BẮT ĐẦU TỰ ĐỘNG KHỞI TẠO QUYỂN BÁO CÁO ĐỒ ÁN WORD (> 40 TRANG)")
    print("="*80)

    doc = Document()
    setup_document_styles(doc)

    print("[1/5] Đang khởi tạo Phần Đầu (Bìa, Cam đoan, Cảm ơn, Tóm tắt, Mục lục, Danh mục)...")
    generate_front_matter(doc)

    print("[2/5] Đang khởi tạo Mở Đầu (Tính cấp thiết, Mục tiêu, Đối tượng, Phương pháp, Ý nghĩa)...")
    generate_introduction(doc)

    print("[3/5] Đang khởi tạo Chương 1: Tổng quan Bài toán và Cơ sở Lý thuyết (5Vs, DeepFace, ArcFace, ANN)...")
    generate_chapter_1(doc)

    print("[4/5] Đang khởi tạo Chương 2: Phương pháp Nghiên cứu & Kiến trúc Lai (Trọng tâm 1, >13 trang)...")
    generate_chapter_2(doc)

    print("[5/5] Đang khởi tạo Chương 3: Thực hiện & Thực nghiệm (Trọng tâm 2, >13 trang, 5 bảng, 6 biểu đồ)...")
    generate_chapter_3(doc, TABLES_DIR, FIGURES_DIR)

    print("[*] Đang khởi tạo Kết luận, Tài liệu Tham khảo chuẩn IEEE và Phụ lục Mã nguồn...")
    generate_conclusion_and_references(doc)

    docx_out = os.path.join(DELIVERABLES_DIR, "Bao_Cao_Do_An.docx")
    print(f"\n[*] Đang lưu tài liệu Word vào: {docx_out}...")
    doc.save(docx_out)
    print(f"[THÀNH CÔNG] Đã lưu thành công file Word: {docx_out}")

    # Chuyển đổi sang PDF
    convert_docx_to_pdf(docx_out)

if __name__ == "__main__":
    build_full_report()
