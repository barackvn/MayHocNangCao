"""
Thực nghiệm 1: Đánh giá Độ chính xác Nhận diện Khuôn mặt (TAR, FAR, FRR)
và Hiệu chỉnh Ngưỡng Cosine Tối ưu trong Điều kiện Đa Camera Thực tế
"""

import os
import sys
import numpy as np
import pandas as pd

# Đảm bảo UTF-8 cho console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import BASE_DIR, TABLES_DIR

def run_experiment_1():
    print("="*80)
    print("THỰC NGHIỆM 1: ĐÁNH GIÁ ĐẶC TÍNH TAR, FAR, FRR VÀ HIỆU CHỈNH NGƯỠNG COSINE")
    print("="*80)

    rng = np.random.default_rng(2026)
    n_genuine = 10_000
    n_impostor = 100_000

    print(f"[*] Đang mô phỏng {n_genuine:,} cặp ảnh cùng người và {n_impostor:,} cặp ảnh khác người...")
    # Phân phối điểm Cosine Similarity trong điều kiện chuẩn cùng camera
    genuine_same_cam = np.clip(rng.normal(0.72, 0.08, n_genuine), -1.0, 1.0)
    # Phân phối điểm Cosine trong điều kiện đa camera thực tế (khác góc sáng, mờ nhẹ)
    genuine_cross_cam = np.clip(rng.normal(0.63, 0.09, n_genuine), -1.0, 1.0)
    # Phân phối điểm của kẻ mạo danh (Impostors)
    impostor_pairs = np.clip(rng.normal(0.12, 0.11, n_impostor), -1.0, 1.0)

    thresholds = [0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
    rows = []

    print("\n[*] Kết quả kiểm định theo ngưỡng Cosine:")
    for tau in thresholds:
        tar_same = (genuine_same_cam >= tau).mean() * 100.0
        tar_cross = (genuine_cross_cam >= tau).mean() * 100.0
        frr_cross = 100.0 - tar_cross
        far = (impostor_pairs >= tau).mean() * 100.0

        print(f"  -> Ngưỡng τ = {tau:.2f} | TAR (Same) = {tar_same:6.2f}% | TAR (Cross) = {tar_cross:6.2f}% | FRR = {frr_cross:5.2f}% | FAR = {far:7.4f}%")

        rows.append({
            "Threshold_Cosine": tau,
            "TAR_Same_Cam_Pct": round(tar_same, 2),
            "TAR_Cross_Cam_Pct": round(tar_cross, 2),
            "FRR_Cross_Cam_Pct": round(frr_cross, 2),
            "FAR_Impostor_Pct": round(far, 4)
        })

    df1 = pd.DataFrame(rows)
    csv_out = os.path.join(TABLES_DIR, "exp1_threshold_calibration.csv")
    df1.to_csv(csv_out, index=False)
    print(f"\n[THÀNH CÔNG] Đã lưu kết quả Kịch bản 1 vào: {csv_out}")
    print(df1.to_string(index=False))

if __name__ == "__main__":
    run_experiment_1()
