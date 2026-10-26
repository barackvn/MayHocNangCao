"""
Thực nghiệm 3: Khảo sát Siêu tham số nprobe & Phân tích Đánh đổi Pareto giữa Recall và Latency
"""

import os
import sys
import time
import numpy as np
import pandas as pd
import faiss

# Đảm bảo UTF-8 cho console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import BASE_DIR, TABLES_DIR

def run_experiment_3():
    print("="*80)
    print("THỰC NGHIỆM 3: KHẢO SÁT SIÊU THAM SỐ NPROBE TRÊN CHỈ MỤC IVFPQ")
    print("="*80)

    N = 200_000
    dim = 512
    n_queries = 500
    rng = np.random.default_rng(42)

    print(f"[*] Đang sinh {N:,} vector cơ sở và {n_queries} vector query chuẩn hóa...")
    xb = rng.standard_normal((N, dim), dtype=np.float32)
    faiss.normalize_L2(xb)

    rng_q = np.random.default_rng(777)
    xq = rng_q.standard_normal((n_queries, dim), dtype=np.float32)
    faiss.normalize_L2(xq)

    print("[*] Đang xây dựng Ground Truth (IndexFlatIP)...")
    idx_flat = faiss.IndexFlatIP(dim)
    idx_flat.add(xb)
    _, I_gt = idx_flat.search(xq, 10)

    print("[*] Đang huấn luyện IndexIVFPQ (m=64, nbits=8, nlist=512)...")
    quantizer = faiss.IndexFlatL2(dim)
    idx_pq = faiss.IndexIVFPQ(quantizer, dim, 512, 64, 8)
    idx_pq.train(xb[:50_000])
    idx_pq.add(xb)

    rows = []
    print("\n[*] Đang khảo sát nprobe từ 1 đến 128:")
    for nprobe in [1, 2, 4, 8, 16, 32, 64, 128]:
        idx_pq.nprobe = nprobe
        t0 = time.perf_counter()
        _, I_pq = idx_pq.search(xq, 10)
        elapsed = time.perf_counter() - t0

        r1 = (I_pq[:, 0] == I_gt[:, 0]).mean() * 100
        r10 = np.mean([I_gt[i, 0] in I_pq[i, :10] for i in range(n_queries)]) * 100
        latency_ms = (elapsed / n_queries) * 1000.0
        qps = int(n_queries / elapsed)

        print(f"  -> nprobe = {nprobe:3d} | Latency = {latency_ms:.3f} ms | QPS = {qps:5d} | Recall@1 = {r1:5.2f}% | Recall@10 = {r10:5.2f}%")

        rows.append({
            "nprobe": nprobe,
            "Latency_ms": round(latency_ms, 3),
            "QPS": qps,
            "Recall_at_1_Pct": round(r1, 2),
            "Recall_at_10_Pct": round(r10, 2)
        })

    df3 = pd.DataFrame(rows)
    csv_out = os.path.join(TABLES_DIR, "exp3_recall_latency_tradeoff.csv")
    df3.to_csv(csv_out, index=False)
    print(f"\n[THÀNH CÔNG] Đã lưu kết quả Kịch bản 3 vào: {csv_out}")
    print(df3.to_string(index=False))

if __name__ == "__main__":
    run_experiment_3()
