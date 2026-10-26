"""
Hệ thống Cấu hình Tham số Toàn cục cho Dự án Big Data Face Recognition
"""

import os
from pathlib import Path

# Thư mục gốc dự án
BASE_DIR = Path(__file__).resolve().parent.parent

# Các thư mục con
DATA_DIR = BASE_DIR / "data"
SAMPLE_FACES_DIR = DATA_DIR / "sample_faces"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"
EVENTS_PARQUET_DIR = DATA_DIR / "events_parquet"

RESULTS_DIR = BASE_DIR / "results"
TABLES_DIR = RESULTS_DIR / "tables"
FIGURES_DIR = RESULTS_DIR / "figures"

DELIVERABLES_DIR = BASE_DIR / "deliverables"
DOCS_DIR = BASE_DIR / "docs"

# Tạo tất cả các thư mục cần thiết
for directory in [
    DATA_DIR, SAMPLE_FACES_DIR, EMBEDDINGS_DIR, EVENTS_PARQUET_DIR,
    RESULTS_DIR, TABLES_DIR, FIGURES_DIR, DELIVERABLES_DIR, DOCS_DIR
]:
    directory.mkdir(parents=True, exist_ok=True)

# Tham số mô hình AI & Vector Đặc trưng
EMBEDDING_DIM = 512
SIMILARITY_METRIC = "INNER_PRODUCT"  # Tương đương Cosine khi vector chuẩn hóa L2
DEFAULT_COSINE_THRESHOLD = 0.50     # Ngưỡng tối ưu cân bằng TAR và FAR

# Tham số chỉ mục FAISS
DEFAULT_NLIST = 1024
DEFAULT_NPROBE = 16
PQ_M = 64                          # 64 sub-vectors x 8-bit = 64 bytes/vector
PQ_NBITS = 8
HNSW_M = 32
HNSW_EF_CONSTRUCTION = 64
HNSW_EF_SEARCH = 64

# Tham số Streaming & Data Lake
DEFAULT_KAFKA_TOPIC = "camera_face_events"
MICROBATCH_DURATION = "1 second"
WATERMARK_DURATION = "10 minutes"
PARQUET_COMPRESSION = "snappy"
