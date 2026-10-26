"""
Script tự động vẽ 6 biểu đồ học thuật độ phân giải cao 300 DPI từ dữ liệu thực nghiệm
"""

import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import pandas as pd
import numpy as np

# Đảm bảo UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Cấu hình phong cách đồ thị học thuật
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['grid.color'] = '#dddddd'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABLES_DIR = os.path.join(BASE_DIR, "results", "tables")
FIGURES_DIR = os.path.join(BASE_DIR, "results", "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# ==============================================================================
# HÌNH 1: SƠ ĐỒ KIẾN TRÚC TỔNG THỂ HỆ THỐNG LAI 4 TẦNG (SYSTEM ARCHITECTURE)
# ==============================================================================
def plot_fig1_architecture():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.axis('off')

    # Định nghĩa màu sắc các tầng
    c_source = '#E3F2FD'   # Xanh biển nhạt
    c_ai = '#E8F5E9'       # Xanh lá nhạt
    c_bigdata = '#FFF3E0'  # Cam nhạt
    c_lake = '#EDE7F6'     # Tím nhạt

    # Vẽ các khối đại diện cho 4 tầng
    # 1. Tầng Thu thập Luồng
    box_stream = patches.FancyBboxPatch((0.05, 0.62), 0.22, 0.32, boxstyle="round,pad=0.03", ec="#1565C0", fc=c_source, lw=1.5)
    ax.add_patch(box_stream)
    ax.text(0.16, 0.90, "TẦNG 1: THU NHẬN RTSP", ha="center", va="center", weight="bold", color="#0D47A1", fontsize=11)
    ax.text(0.16, 0.76, "• Camera IP 1..N (RTSP H.264)\n• OpenCV VideoCapture\n• Lọc mờ Laplacian (σ² > 120)\n• Dynamic Frame Dropping",
            ha="center", va="center", fontsize=9, color="#212121", linespacing=1.4)

    # 2. Tầng AI Trích xuất Đặc trưng
    box_ai = patches.FancyBboxPatch((0.36, 0.62), 0.26, 0.32, boxstyle="round,pad=0.03", ec="#2E7D32", fc=c_ai, lw=1.5)
    ax.add_patch(box_ai)
    ax.text(0.49, 0.90, "TẦNG 2: MÔ HÌNH AI SÂU", ha="center", va="center", weight="bold", color="#1B5E20", fontsize=11)
    ax.text(0.49, 0.76, "• RetinaFace (ResNet-50 / MobileNet)\n• Căn chỉnh Affine 5 điểm mốc (112x112)\n• Pretrained ArcFace (SphereFace/r100)\n• Trích xuất Vector 512-D L2-Normalized",
            ha="center", va="center", fontsize=9, color="#212121", linespacing=1.4)

    # 3. Tầng Chỉ mục Vector Phân tán FAISS
    box_faiss = patches.FancyBboxPatch((0.71, 0.62), 0.25, 0.32, boxstyle="round,pad=0.03", ec="#E65100", fc=c_bigdata, lw=1.5)
    ax.add_patch(box_faiss)
    ax.text(0.835, 0.90, "TẦNG 3: VECTOR INDEX (FAISS)", ha="center", va="center", weight="bold", color="#BF360C", fontsize=11)
    ax.text(0.835, 0.76, "• IndexFlatIP (Ground Truth)\n• IndexIVFFlat (Voronoi Cells)\n• IndexIVFPQ (m=64, nén RAM 32x)\n• IndexHNSW (Greedy Graph Search)\n• Top-1/Top-K Search (< 1 ms)",
            ha="center", va="center", fontsize=9, color="#212121", linespacing=1.4)

    # 4. Tầng Xử lý Luồng & Data Lake
    box_lake = patches.FancyBboxPatch((0.15, 0.08), 0.70, 0.40, boxstyle="round,pad=0.03", ec="#512DA8", fc=c_lake, lw=1.5)
    ax.add_patch(box_lake)
    ax.text(0.50, 0.43, "TẦNG 4: XỬ LÝ PHÂN TÁN & DATA LAKE (BIG DATA PIPELINE)", ha="center", va="center", weight="bold", color="#311B92", fontsize=12)

    # Khối nhỏ bên trong Tầng 4
    # Kafka
    box_k = patches.FancyBboxPatch((0.18, 0.14), 0.18, 0.22, boxstyle="round,pad=0.02", ec="#7E57C2", fc="#FFFFFF", lw=1.2)
    ax.add_patch(box_k)
    ax.text(0.27, 0.31, "Apache Kafka", ha="center", va="center", weight="bold", color="#4527A0", fontsize=10)
    ax.text(0.27, 0.21, "• Topic: camera_events\n• Phân vùng theo CamID\n• Throughput > 5k msg/s", ha="center", va="center", fontsize=8.5)

    # Spark Streaming
    box_s = patches.FancyBboxPatch((0.41, 0.14), 0.20, 0.22, boxstyle="round,pad=0.02", ec="#7E57C2", fc="#FFFFFF", lw=1.2)
    ax.add_patch(box_s)
    ax.text(0.51, 0.31, "PySpark Streaming", ha="center", va="center", weight="bold", color="#4527A0", fontsize=10)
    ax.text(0.51, 0.21, "• Micro-batch (1 sec)\n• Watermark 10 min\n• Stateful Deduplication\n• Cross-Cam Trajectory", ha="center", va="center", fontsize=8.5)

    # Parquet Data Lake
    box_p = patches.FancyBboxPatch((0.65, 0.14), 0.17, 0.22, boxstyle="round,pad=0.02", ec="#7E57C2", fc="#FFFFFF", lw=1.2)
    ax.add_patch(box_p)
    ax.text(0.735, 0.31, "Apache Parquet", ha="center", va="center", weight="bold", color="#4527A0", fontsize=10)
    ax.text(0.735, 0.21, "• Lưu trữ cột Snappy\n• Phân vùng Zone/Date\n• Nén 80% dung lượng\n• Truy vấn SQL cực nhanh", ha="center", va="center", fontsize=8.5)

    # Các mũi tên luồng dữ liệu
    arrow_props = dict(facecolor='#424242', edgecolor='#424242', width=1.5, headwidth=7, shrink=0.08)
    ax.annotate('', xy=(0.36, 0.78), xytext=(0.27, 0.78), arrowprops=arrow_props)
    ax.text(0.315, 0.81, "Cắt mặt", ha="center", va="center", fontsize=8, weight="bold", color="#333333")

    ax.annotate('', xy=(0.71, 0.78), xytext=(0.62, 0.78), arrowprops=arrow_props)
    ax.text(0.665, 0.81, "Vector 512D", ha="center", va="center", fontsize=8, weight="bold", color="#333333")

    # Mũi tên từ Tầng 3 xuống Tầng 4 (Kafka)
    ax.annotate('', xy=(0.27, 0.36), xytext=(0.78, 0.62),
                arrowprops=dict(facecolor='#E65100', edgecolor='#E65100', width=1.5, headwidth=7, connectionstyle="arc3,rad=-0.15"))
    ax.text(0.48, 0.54, "Event Message (PersonID, Similarity, CamID, Time)", ha="center", va="center", fontsize=8.5, weight="bold", color="#BF360C")

    # Mũi tên nội bộ tầng 4
    ax.annotate('', xy=(0.41, 0.25), xytext=(0.36, 0.25), arrowprops=arrow_props)
    ax.annotate('', xy=(0.65, 0.25), xytext=(0.61, 0.25), arrowprops=arrow_props)

    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "fig1_system_architecture.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Đã xuất Fig 1: {output_path}")

# ==============================================================================
# HÌNH 2: ĐƯỜNG CONG TAR, FAR, FRR THEO NGƯỠNG COSINE
# ==============================================================================
def plot_fig2_roc():
    csv_file = os.path.join(TABLES_DIR, "exp1_threshold_calibration.csv")
    if not os.path.exists(csv_file):
        print(f"[CẢNH BÁO] Không tìm thấy {csv_file}")
        return
    df = pd.read_csv(csv_file)

    fig, ax1 = plt.subplots(figsize=(8.5, 5), dpi=300)

    ax1.plot(df['Threshold_Cosine'], df['TAR_Same_Cam_Pct'], 'o-', color='#1B5E20', linewidth=2.2, label='TAR (Cùng Camera)')
    ax1.plot(df['Threshold_Cosine'], df['TAR_Cross_Cam_Pct'], 's-', color='#2E7D32', linewidth=2.2, label='TAR (Khác Camera - Thực tế)')
    ax1.plot(df['Threshold_Cosine'], df['FRR_Cross_Cam_Pct'], 'd--', color='#D84315', linewidth=1.8, label='FRR (Khác Camera)')
    ax1.set_xlabel('Ngưỡng tương đồng Cosine (τ)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Tỷ lệ TAR / FRR (%)', fontsize=11, fontweight='bold', color='#1B5E20')
    ax1.tick_params(axis='y', labelcolor='#1B5E20')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.set_ylim(0, 105)

    # Trục phụ cho FAR
    ax2 = ax1.twinx()
    ax2.plot(df['Threshold_Cosine'], df['FAR_Impostor_Pct'], '^-.', color='#C62828', linewidth=2.2, label='FAR (Kẻ giả mạo)')
    ax2.set_ylabel('Tỷ lệ Chấp nhận Sai - FAR (%)', fontsize=11, fontweight='bold', color='#C62828')
    ax2.tick_params(axis='y', labelcolor='#C62828')
    ax2.set_yscale('log')
    ax2.set_ylim(1e-4, 10)

    # Đánh dấu vùng ngưỡng tối ưu τ = 0.50
    ax1.axvline(x=0.50, color='#6A1B9A', linestyle=':', linewidth=2, label='Ngưỡng đề xuất (τ = 0.50)')
    ax1.text(0.505, 50, 'Ngưỡng tối ưu τ = 0.50\n(TAR ~ 92.5%, FAR ~ 0.02%)', color='#6A1B9A', fontsize=9, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', fc='#F3E5F5', ec='#6A1B9A', lw=1))

    # Gộp legend 2 trục
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='center left', fontsize=9)

    plt.title('Đặc tính Nhận diện Khuôn mặt (TAR, FAR, FRR) theo Ngưỡng Cosine', fontsize=12, fontweight='bold', pad=12)
    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "fig2_roc_tar_far_curve.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Đã xuất Fig 2: {output_path}")

# ==============================================================================
# HÌNH 3: ĐỘ TRỄ VÀ QPS THEO QUY MÔ VECTOR (SCALABILITY)
# ==============================================================================
def plot_fig3_latency_qps():
    csv_file = os.path.join(TABLES_DIR, "exp2_faiss_scalability.csv")
    if not os.path.exists(csv_file):
        print(f"[CẢNH BÁO] Không tìm thấy {csv_file}")
        return
    df = pd.read_csv(csv_file)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5), dpi=300)

    colors = {'IndexFlatIP': '#C62828', 'IndexIVFFlat (nprobe=16)': '#1565C0',
              'IndexIVFPQ (m=64, nprobe=32)': '#2E7D32', 'IndexHNSW32 (efSearch=64)': '#E65100'}

    markers = {'IndexFlatIP': 'o', 'IndexIVFFlat (nprobe=16)': 's',
               'IndexIVFPQ (m=64, nprobe=32)': '^', 'IndexHNSW32 (efSearch=64)': 'D'}

    for idx_type, group in df.groupby('Index_Type'):
        ax1.plot(group['Scale_N'], group['Latency_ms'], marker=markers.get(idx_type, 'o'),
                 color=colors.get(idx_type, '#333'), linewidth=2.0, label=idx_type)
        ax2.plot(group['Scale_N'], group['QPS'], marker=markers.get(idx_type, 'o'),
                 color=colors.get(idx_type, '#333'), linewidth=2.0, label=idx_type)

    # Trục Latency
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('Quy mô cơ sở dữ liệu vector (N)', fontsize=10.5, fontweight='bold')
    ax1.set_ylabel('Độ trễ truy vấn (ms / vector) [Log scale]', fontsize=10.5, fontweight='bold')
    ax1.set_title('(a) Độ trễ truy vấn theo Quy mô Vector', fontsize=11, fontweight='bold')
    ax1.grid(True, which="both", ls="--", alpha=0.5)
    ax1.legend(fontsize=8.5)

    # Trục QPS
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel('Quy mô cơ sở dữ liệu vector (N)', fontsize=10.5, fontweight='bold')
    ax2.set_ylabel('Thông lượng truy vấn (QPS) [Log scale]', fontsize=10.5, fontweight='bold')
    ax2.set_title('(b) Thông lượng truy vấn (QPS) theo Quy mô Vector', fontsize=11, fontweight='bold')
    ax2.grid(True, which="both", ls="--", alpha=0.5)
    ax2.legend(fontsize=8.5)

    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "fig3_latency_qps_scaling.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Đã xuất Fig 3: {output_path}")

# ==============================================================================
# HÌNH 4: TIÊU THỤ BỘ NHỚ RAM GIỮA CÁC CHỈ MỤC (RAM CONSUMPTION)
# ==============================================================================
def plot_fig4_ram():
    csv_file = os.path.join(TABLES_DIR, "exp2_faiss_scalability.csv")
    if not os.path.exists(csv_file):
        print(f"[CẢNH BÁO] Không tìm thấy {csv_file}")
        return
    df = pd.read_csv(csv_file)

    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)

    # Vẽ biểu đồ nhóm cột tại mốc N = 100K, 500K, 1M
    scales_filter = [100_000, 500_000, 1_000_000]
    df_filtered = df[df['Scale_N'].isin(scales_filter)]

    palette = ['#E53935', '#1E88E5', '#43A047', '#FB8C00']
    sns.barplot(data=df_filtered, x='Scale_N', y='RAM_MB', hue='Index_Type', palette=palette, ax=ax)

    ax.set_xticklabels(['100.000', '500.000', '1.000.000 (1 Triệu)'], fontsize=10)
    ax.set_xlabel('Số lượng Vector đặc trưng khuôn mặt (N)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Dung lượng Bộ nhớ RAM tiêu thụ (MB)', fontsize=11, fontweight='bold')
    ax.set_title('So sánh Tiêu thụ Bộ nhớ RAM giữa các Cấu trúc Chỉ mục Vector', fontsize=12, fontweight='bold', pad=12)
    ax.grid(True, axis='y', linestyle='--', alpha=0.6)
    ax.legend(title='Cấu trúc Chỉ mục', fontsize=9, title_fontsize=9.5)

    # Đánh dấu chú thích mức tiết kiệm RAM của IVFPQ
    ram_flat_1m = df[(df['Scale_N'] == 1_000_000) & (df['Index_Type'] == 'IndexFlatIP')]['RAM_MB'].values[0]
    ram_pq_1m = df[(df['Scale_N'] == 1_000_000) & (df['Index_Type'].str.contains('IVFPQ'))]['RAM_MB'].values[0]
    reduction_pct = (1 - ram_pq_1m / ram_flat_1m) * 100
    ax.text(2.05, ram_pq_1m + 150, f"IVFPQ nén {reduction_pct:.1f}% RAM!\n(Chỉ tốn {ram_pq_1m:.0f} MB so với {ram_flat_1m:.0f} MB)",
            ha='center', fontsize=9, fontweight='bold', color='#1B5E20',
            bbox=dict(boxstyle='round,pad=0.3', fc='#E8F5E9', ec='#2E7D32', lw=1.2))

    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "fig4_ram_consumption_comparison.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Đã xuất Fig 4: {output_path}")

# ==============================================================================
# HÌNH 5: ĐÁNH ĐỔI PARETO GIỮA RECALL VÀ LATENCY (NPROBE TUNING)
# ==============================================================================
def plot_fig5_pareto():
    csv_file = os.path.join(TABLES_DIR, "exp3_recall_latency_tradeoff.csv")
    if not os.path.exists(csv_file):
        print(f"[CẢNH BÁO] Không tìm thấy {csv_file}")
        return
    df = pd.read_csv(csv_file)

    fig, ax = plt.subplots(figsize=(8.5, 5), dpi=300)

    ax.plot(df['Latency_ms'], df['Recall_at_1_Pct'], 'o-', color='#1565C0', linewidth=2.2, label='Recall@1 (Top-1 Match)')
    ax.plot(df['Latency_ms'], df['Recall_at_10_Pct'], 's--', color='#2E7D32', linewidth=2.2, label='Recall@10 (Top-10 Candidates)')

    # Gắn nhãn các điểm nprobe quan trọng
    for _, row in df.iterrows():
        np_val = int(row['nprobe'])
        if np_val in [1, 4, 16, 32, 64, 128]:
            offset_y = 1.0 if np_val != 1 else -3.0
            ax.annotate(f"nprobe={np_val}", (row['Latency_ms'], row['Recall_at_1_Pct']),
                        textcoords="offset points", xytext=(0, 8), ha='center', fontsize=8, fontweight='bold',
                        color='#0D47A1')

    # Đánh dấu vùng Pareto Sweet-Spot (nprobe = 16..32)
    ax.axvspan(df[df['nprobe'] == 16]['Latency_ms'].values[0] - 0.02,
               df[df['nprobe'] == 32]['Latency_ms'].values[0] + 0.05,
               color='#FFF9C4', alpha=0.6, label='Vùng tối ưu đề xuất (nprobe = 16-32)')

    ax.set_xlabel('Độ trễ truy vấn trung bình (ms / query)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Độ chính xác Recall (%)', fontsize=11, fontweight='bold')
    ax.set_title('Đường cong Đánh đổi Pareto giữa Recall và Latency theo Siêu tham số nprobe (IVFPQ)', fontsize=11.5, fontweight='bold', pad=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_ylim(40, 102)
    ax.legend(loc='lower right', fontsize=9.5)

    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "fig5_recall_vs_latency_pareto.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Đã xuất Fig 5: {output_path}")

# ==============================================================================
# HÌNH 6: HIỆU NĂNG XỬ LÝ LUỒNG SPARK STREAMING & LATENCY ĐẦU CUỐI
# ==============================================================================
def plot_fig6_spark_throughput():
    csv_file = os.path.join(TABLES_DIR, "exp4_spark_streaming_throughput.csv")
    if not os.path.exists(csv_file):
        print(f"[CẢNH BÁO] Không tìm thấy {csv_file}")
        return
    df = pd.read_csv(csv_file)

    fig, ax1 = plt.subplots(figsize=(8.5, 5), dpi=300)

    # Vẽ Throughput
    ax1.plot(df['Num_Cameras'], df['Input_Events_Per_Sec'], 'o--', color='#757575', linewidth=1.8, label='Tốc độ sự kiện đầu vào (Events/s)')
    ax1.plot(df['Num_Cameras'], df['Processed_Events_Per_Sec'], 's-', color='#1565C0', linewidth=2.4, label='Tốc độ xử lý của Spark (Events/s)')
    ax1.set_xlabel('Số lượng Camera giám sát đồng thời (Streams)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Thông lượng Sự kiện (Events / Giây)', fontsize=11, fontweight='bold', color='#1565C0')
    ax1.tick_params(axis='y', labelcolor='#1565C0')
    ax1.grid(True, linestyle='--', alpha=0.6)

    # Trục phụ cho Latency P95
    ax2 = ax1.twinx()
    ax2.plot(df['Num_Cameras'], df['P95_EndToEnd_Latency_s'], '^-.', color='#E65100', linewidth=2.2, label='Độ trễ đầu-cuối P95 (giây)')
    ax2.set_ylabel('Độ trễ P95 Đầu-Cuối (Giây)', fontsize=11, fontweight='bold', color='#E65100')
    ax2.tick_params(axis='y', labelcolor='#E65100')
    ax2.set_ylim(0, 5.0)

    # Gộp legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=9)

    plt.title('Thông lượng và Độ trễ Đầu-Cuối của Cụm Spark Structured Streaming theo Tải Camera', fontsize=11.5, fontweight='bold', pad=12)
    plt.tight_layout()
    output_path = os.path.join(FIGURES_DIR, "fig6_spark_streaming_throughput.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Đã xuất Fig 6: {output_path}")

def plot_all():
    print(">>> Bắt đầu tạo toàn bộ 6 biểu đồ học thuật chuẩn 300 DPI...")
    plot_fig1_architecture()
    plot_fig2_roc()
    plot_fig3_latency_qps()
    plot_fig4_ram()
    plot_fig5_pareto()
    plot_fig6_spark_throughput()
    print(">>> [HOÀN TẤT] Toàn bộ 6 biểu đồ đã được lưu vào results/figures/")

if __name__ == "__main__":
    plot_all()
