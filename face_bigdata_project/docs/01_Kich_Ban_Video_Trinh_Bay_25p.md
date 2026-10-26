# KỊCH BẢN THUYẾT TRÌNH BẢO VỆ ĐỒ ÁN (20 – 30 PHÚT)
## ĐỀ TÀI: KIẾN TRÚC LAI KẾT HỢP ARCFACE VÀ CHỈ MỤC VECTOR PHÂN TÁN (IVF-PQ/HNSW) CHO NHẬN DIỆN KHUÔN MẶT ĐA CAMERA VÀ PHÂN TÍCH SỰ KIỆN THỜI GIAN THỰC

* **Thời lượng dự kiến:** 24 – 26 phút (trung bình 50–60 giây/slide cho 28 slides)
* **Phân công thành viên:**
  * **Thành viên 1 (Trưởng nhóm):** Slide 1 đến Slide 9 (Mở đầu, Động lực thực tiễn, Tổng quan & Khoảng trống nghiên cứu)
  * **Thành viên 2:** Slide 10 đến Slide 17 (Phương pháp nghiên cứu, Kiến trúc 4 tầng, Toán học ArcFace & Chỉ mục ANN FAISS)
  * **Thành viên 3:** Slide 18 đến Slide 25 (Môi trường, 5 Kịch bản Thực nghiệm định lượng, Biểu đồ & Phân tích số liệu)
  * **Thành viên 4 (hoặc Thành viên 1):** Slide 26 đến Slide 28 (Kết luận, Hạn chế, Hướng phát triển & Hỏi đáp Q&A)

---

### PHẦN 1: MỞ ĐẦU & BÀI TOÁN THỰC TIỄN (THÀNH VIÊN 1 - 7 PHÚT)

#### Slide 1: Trang tiêu đề đồ án
* **Nội dung hiển thị:** Tên đề tài tiếng Việt & tiếng Anh, Giảng viên hướng dẫn ThS. Hà Minh Tân, Danh sách thành viên nhóm, Logo trường và khoa.
* **Lời thoại (Speaker Notes):**
  > *"Kính chào Thầy Hà Minh Tân cùng toàn thể hội đồng và các bạn sinh viên. Hôm nay, nhóm chúng em xin được đại diện trình bày báo cáo đồ án môn học Phân tích Dữ liệu lớn với đề tài: **'Xây dựng Kiến trúc Lai Kết hợp Mô hình Đặc trưng Sâu ArcFace và Chỉ mục Lượng tử hóa Vector Phân tán cho Bài toán Nhận diện Khuôn mặt và Phân tích Sự kiện Đa Camera Thời gian thực'**. Đề tài được nhóm tập trung giải quyết bài toán giao thoa giữa Trí tuệ nhân tạo thị giác máy tính và Kỹ thuật xử lý Dữ liệu lớn quy mô hàng triệu thực thể."*

#### Slide 2: Động lực thực tiễn - Tận dụng Camera IP RTSP sẵn có
* **Nội dung hiển thị:** Hình ảnh so sánh giữa việc thay mới toàn bộ AI Camera đắt đỏ và việc tận dụng hạ tầng Camera RTSP chuẩn H.264 sẵn có.
* **Lời thoại (Speaker Notes):**
  > *"Xuất phát từ thực tế, tại các tòa nhà văn phòng, nhà máy, trường học, hàng trăm camera IP thông thường đã được lắp đặt từ lâu. Chi phí để thay thế bằng các AI Camera chuyên dụng có chip NPU tích hợp là rất lớn, lên tới hàng tỷ đồng. Động lực lớn nhất của nhóm em là: Làm thế nào để tận dụng nguyên vẹn luồng RTSP của hạ tầng camera cũ, nhưng vẫn đạt được khả năng nhận diện khuôn mặt và cảnh báo tức thời với độ trễ dưới 1 giây trên toàn hệ thống?"*

#### Slide 3: Điểm nghẽn cổ chai khi mở rộng quy mô (The Big Data Bottleneck)
* **Nội dung hiển thị:** Đồ thị độ trễ tăng vọt từ < 1 ms lên > 100 ms khi số lượng vector tăng từ 10.000 lên hàng triệu người; nguy cơ tràn RAM.
* **Lời thoại (Speaker Notes):**
  > *"Khi số lượng camera tăng lên 50, 100 chiếc và danh sách nhân sự mở rộng lên hàng trăm nghìn hoặc hàng triệu người, bài toán lập tức đối mặt với 'điểm nghẽn cổ chai' của Dữ liệu lớn. Nếu chúng ta dùng phương pháp so khớp vét cạn truyền thống (Brute-Force) hoặc lưu vector trong cơ sở dữ liệu quan hệ SQL, độ phức tạp tính toán là $O(N \cdot D)$. Với 1 triệu vector 512 chiều, mỗi khuôn mặt cần tới hàng trăm phép tính tích vô hướng, khiến CPU quá tải, độ trễ vượt ngưỡng 100 ms và gây tràn bộ nhớ RAM."*

#### Slide 4: Mục tiêu và Phạm vi nghiên cứu
* **Nội dung hiển thị:** 3 mục tiêu cụ thể: (1) Kiến trúc lai không cần retrain; (2) Chỉ mục ANN nén RAM 32 lần, latency < 1ms; (3) Pipeline xử lý luồng Kafka + Spark chịu tải 500 camera.
* **Lời thoại (Speaker Notes):**
  > *"Để giải quyết thách thức này, nhóm đặt ra 3 mục tiêu trọng tâm: Thứ nhất, xây dựng kiến trúc lai tách biệt giữa trích xuất đặc trưng và tìm kiếm, không cần huấn luyện lại mô hình khi thêm người mới. Thứ hai, ứng dụng kỹ thuật lượng tử hóa tích IVF-PQ giúp giảm 96% dung lượng RAM và giữ độ trễ tìm kiếm dưới 1 ms trên hàng triệu vector. Thứ ba, thiết lập pipeline xử lý luồng phân tán chịu tải từ 10 đến 500 camera với độ trễ P95 đạt chuẩn thời gian thực."*

#### Slide 5: Tổng quan bài toán dưới góc nhìn Big Data (Mô hình 5Vs)
* **Nội dung hiển thị:** Phân tích Volume (hàng triệu vector, gigabyte sự kiện), Velocity (hàng ngàn frames/sec), Variety (video H.264, JSON, Parquet), Veracity (nhiễu, góc nghiêng, mờ nhòe), Value (an ninh, điểm danh).
* **Lời thoại (Speaker Notes):**
  > *"Dưới góc nhìn môn học Phân tích Dữ liệu lớn, bài toán này hội tụ đầy đủ đặc trưng 5Vs: Volume là khối lượng hàng triệu vector 512 chiều và hàng triệu bản ghi nhật ký. Velocity là vận tốc hàng nghìn khung hình và sự kiện đổ về mỗi giây. Variety là tính đa dạng từ luồng video RTSP đến dữ liệu bán cấu trúc JSON và dữ liệu cột Parquet. Veracity là độ xác thực khi hình ảnh bị mờ nhòe, góc nghiêng cần bộ lọc Laplacian; và cuối cùng Value là giá trị an ninh thực tiễn mang lại."*

#### Slide 6: Tiến hóa của các mô hình trích xuất đặc trưng khuôn mặt sâu
* **Nội dung hiển thị:** Dòng thời gian: DeepFace (2014) $\rightarrow$ FaceNet Triplet Loss (2015) $\rightarrow$ SphereFace (2017) $\rightarrow$ CosFace (2018) $\rightarrow$ ArcFace (Additive Angular Margin Loss, 2019).
* **Lời thoại (Speaker Notes):**
  > *"Nhìn lại lịch sử phát triển, từ DeepFace của Facebook dùng Softmax truyền thống, đến FaceNet dùng Triplet Loss gặp khó khăn trong việc chọn mẫu Semi-hard Mining. Bước ngoặt xuất hiện khi ArcFace của Deng et al. giới thiệu hàm mất mát biên góc cộng tính (Additive Angular Margin). ArcFace chuẩn hóa cả vector trọng số và vector đặc trưng lên mặt siêu cầu đơn vị, tạo ra khoảng cách góc phân biệt rõ rệt giữa các lớp, đạt độ chính xác kỷ lục 99.83% trên tập LFW."*

#### Slide 7: Tổng quan các kỹ thuật tìm kiếm láng giềng gần nhất xấp xỉ (ANN)
* **Nội dung hiển thị:** Sơ đồ so sánh: Tree-based (KD-Tree), Hash-based (LSH), Clustering (IVF), Quantization (PQ), Graph-based (HNSW).
* **Lời thoại (Speaker Notes):**
  > *"Để tìm kiếm siêu nhanh trong không gian 512 chiều, các cấu trúc cây cổ điển như KD-Tree hoàn toàn bất lực vì 'lời nguyền số chiều' (Curse of Dimensionality). Giải pháp hiện đại bắt buộc phải dùng Tìm kiếm láng giềng gần nhất xấp xỉ (ANN). Trong đó nổi bật là Inverted File (IVF) chia cụm không gian, Product Quantization (PQ) nén vector thành mã byte, và Hierarchical Navigable Small World (HNSW) xây dựng đồ thị phân cấp đa tầng."*

#### Slide 8: Tổng quan kiến trúc xử lý luồng và Data Lake
* **Nội dung hiển thị:** Apache Kafka (Event Streaming Ingestion), Apache Spark Structured Streaming (Stateful Processing), Apache Parquet (Columnar Storage).
* **Lời thoại (Speaker Notes):**
  > *"Ở tầng dữ liệu phân tán, Apache Kafka đóng vai trò là xương sống đệm thông điệp với cơ chế phân vùng theo Camera ID. Spark Structured Streaming xử lý theo vi lô (micro-batch) với cơ chế Watermarking giúp loại bỏ dữ liệu đến trễ và khử trùng lặp có trạng thái. Dữ liệu sau đó được ghi xuống Data Lake định dạng Apache Parquet nén Snappy để phục vụ phân tích OLAP lịch sử."*

#### Slide 9: Bảng đối sánh công trình liên quan và Khoảng trống nghiên cứu (Research Gap)
* **Nội dung hiển thị:** Bảng so sánh 4 nghiên cứu tiêu biểu (FaceNet + MySQL, DeepFace + Elasticsearch, ArcFace + Milvus độc lập) với giải pháp đề xuất của nhóm.
* **Lời thoại (Speaker Notes):**
  > *"Qua khảo cứu các công trình khoa học quốc tế, hầu hết các nghiên cứu trước đây hoặc chỉ tập trung vào độ chính xác của AI đơn lẻ mà bỏ qua bài toán mở rộng dữ liệu, hoặc sử dụng hệ thống tìm kiếm vector độc lập mà không tích hợp luồng xử lý sự kiện phân tán. Khoảng trống nghiên cứu mà nhóm chúng em giải quyết chính là kết hợp trọn vẹn mô hình biểu diễn ArcFace với chỉ mục nén IVF-PQ và quy trình xử lý luồng Spark thời gian thực."*

---

### PHẦN 2: PHƯƠNG PHÁP NGHIÊN CỨU & KIẾN TRÚC HỆ THỐNG (THÀNH VIÊN 2 - 8 PHÚT)

#### Slide 10: Kiến trúc Lai 4 tầng tổng thể (4-Tier Architecture)
* **Nội dung hiển thị:** Sơ đồ khối chi tiết 4 tầng từ Camera RTSP qua Tầng AI, Tầng Chỉ mục FAISS, đến Tầng Kafka/Spark/Parquet.
* **Lời thoại (Speaker Notes):**
  > *"Em xin phép tiếp tục với phần Phương pháp nghiên cứu. Đây là sơ đồ kiến trúc 4 tầng mà nhóm đã hiện thực hóa. Tầng 1 thu nhận luồng RTSP và lọc chất lượng khung hình. Tầng 2 phát hiện và trích xuất vector khuôn mặt bằng RetinaFace và ArcFace. Tầng 3 thực hiện đối sánh cực nhanh bằng thư viện FAISS. Và Tầng 4 xử lý luồng sự kiện phân tán qua Kafka và Spark. Sau đây em xin phân tích sâu chi tiết từng tầng."*

#### Slide 11: Tầng 1 - Thu nhận luồng RTSP và Lọc mờ Laplacian
* **Nội dung hiển thị:** Công thức toán tử Laplace $\Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$; ngưỡng lọc phương sai $\sigma^2_{Laplacian} \ge 120$; kỹ thuật Dynamic Frame Dropping.
* **Lời thoại (Speaker Notes):**
  > *"Để tránh lãng phí năng lực tính toán của GPU/CPU vào các khung hình vô giá trị, Tầng 1 áp dụng bộ lọc mờ dựa trên phương sai của toán tử Laplacian. Khi ảnh bị mờ chuyển động do người đi nhanh, các cạnh sắc nét biến mất, khiến phương sai $\sigma^2$ giảm mạnh. Hệ thống chỉ chuyển tiếp các khung hình có $\sigma^2 \ge 120$, đồng thời áp dụng cơ chế bỏ khung hình chủ động khi hàng đợi đệm vượt ngưỡng an toàn."*

#### Slide 12: Tầng 2 - Phát hiện RetinaFace & Căn chỉnh Affine 5 điểm mốc
* **Nội dung hiển thị:** Kiến trúc FPN + SSH Context module; Hàm mất mát đa nhiệm $L = L_{cls} + \lambda_1 L_{box} + \lambda_2 L_{pts}$; Ma trận biến đổi Affine $M \in \mathbb{R}^{2 \times 3}$ đưa ảnh về chuẩn $112 \times 112$.
* **Lời thoại (Speaker Notes):**
  > *"Tại Tầng 2, mô hình RetinaFace xác định vị trí khuôn mặt và 5 điểm mốc: 2 mắt, mũi, 2 khóe miệng. Dựa trên 5 điểm mốc này, hệ thống giải bài toán bình phương tối thiểu để tìm ma trận Affine 2D, xoay và chuẩn hóa khuôn mặt về kích thước chuẩn $112 \times 112$ pixels. Nhờ bước căn chỉnh hình học này, vector đặc trưng sinh ra ở bước sau sẽ có tính bất biến rất cao đối với các góc nghiêng đầu trong thực tế."*

#### Slide 13: Toán học ArcFace trên Mặt Siêu Cầu Đơn vị
* **Nội dung hiển thị:** Hàm mất mát ArcFace: $L = -\frac{1}{B}\sum \log \frac{e^{s \cos(\theta_{y_i}+m)}}{e^{s \cos(\theta_{y_i}+m)} + \sum_{j \neq y_i} e^{s \cos \theta_j}}$; Chuẩn hóa $L_2$ đặc trưng và trọng số; Biên góc $m = 0.5$, hệ số tỷ lệ $s = 64$.
* **Lời thoại (Speaker Notes):**
  > *"Về mặt toán học, ArcFace khắc phục hoàn toàn nhược điểm phân tán góc của Softmax cổ điển. Bằng cách chuẩn hóa $L_2$ cả ma trận trọng số và vector đặc trưng, mọi khuôn mặt đều được ánh xạ lên bề mặt của một siêu cầu 512 chiều. Việc cộng trực tiếp góc biên $m = 0.5$ vào góc đích $\theta_{y_i}$ ép buộc khoảng cách giữa các lớp khác nhau phải lớn hơn, đồng thời co cụm khoảng cách giữa các ảnh của cùng một người lại gần nhau nhất."*

#### Slide 14: Chứng minh Tương đương giữa Cosine Similarity và Khoảng cách Euclid
* **Nội dung hiển thị:** Các bước chứng minh: $\Vert{}u-v\Vert{}_2^2 = \Vert{}u\Vert{}_2^2 + \Vert{}v\Vert{}_2^2 - 2 u^T v = 1 + 1 - 2 S_{cos}(u, v) = 2 - 2 S_{cos}(u, v)$.
* **Lời thoại (Speaker Notes):**
  > *"Một đóng góp toán học rất quan trọng giúp hệ thống chạy nhanh là việc chứng minh sự tương đương giữa khoảng cách Euclid bình phương và độ đo Cosine trên mặt siêu cầu đơn vị. Nhóm chứng minh được rằng $\Vert{}u-v\Vert{}_2^2 = 2 - 2 S_{cos}(u, v)$. Điều này đồng nghĩa với việc tìm kiếm vector có Cosine Similarity lớn nhất hoàn toàn tương đương với việc tìm vector có khoảng cách Euclid nhỏ nhất, cho phép ứng dụng trọn vẹn toàn bộ các cấu trúc chỉ mục L2 tối ưu phần cứng của thư viện FAISS."*

#### Slide 15: Phân cụm Đảo ngược (IVF) và Lượng tử hóa Tích (PQ)
* **Nội dung hiển thị:** Phân rã không gian $\mathbb{R}^{512} \rightarrow 64 \times \mathbb{R}^8$; Codebook 256 centroids (8-bit); Asymmetric Distance Computation (ADC); Tỷ lệ nén RAM 32 lần (từ 2.048 byte xuống 64 byte/vector).
* **Lời thoại (Speaker Notes):**
  > *"Để giải bài toán hàng triệu vector, Tầng 3 áp dụng chỉ mục IVF-PQ. Không gian 512 chiều được chia thành 64 không gian con, mỗi không gian con 8 chiều. Thay vì lưu 512 số thực 32-bit (tốn 2.048 bytes), hệ thống chỉ lưu chỉ số 1 byte trỏ vào bảng mã Codebook. Kỹ thuật này nén dung lượng bộ nhớ đúng 32 lần. Khi truy vấn, thuật toán Asymmetric Distance Computation (ADC) tra cứu bảng khoảng cách tính sẵn, giúp tìm kiếm chỉ mất dưới 0.5 ms."*

#### Slide 16: Đồ thị Phân cấp Thế giới nhỏ (HNSW)
* **Nội dung hiển thị:** Cấu trúc phân tầng Skip-List đa mức; Thuật toán tìm kiếm tham lam (Greedy Search); Các tham số $M = 32$, $efConstruction = 64$, $efSearch = 64$.
* **Lời thoại (Speaker Notes):**
  > *"Bên cạnh IVF-PQ, nhóm cũng nghiên cứu cấu trúc đồ thị HNSW. HNSW tổ chức các vector thành một đồ thị thế giới nhỏ nhiều tầng tương tự như cấu trúc Skip-List. Tầng trên cùng có các liên kết xa giúp nhảy nhanh đến vùng lân cận của query, các tầng dưới dần dần tìm kiếm cục bộ chính xác. HNSW cho độ chính xác Recall@1 cao nhất, tuy nhiên tiêu thụ RAM lớn hơn so với IVF-PQ."*

#### Slide 17: Pipeline Xử lý Luồng Kafka & Spark Structured Streaming
* **Nội dung hiển thị:** Kiến trúc Kafka Topics, phân vùng theo MurmurHash(CameraID); Spark Micro-batching; Cơ chế Watermarking 10 phút; Thuật toán Stateful Deduplication khử trùng lặp khuôn mặt cùng người trong 5 giây.
* **Lời thoại (Speaker Notes):**
  > *"Tại Tầng 4, mỗi sự kiện nhận diện được bắn vào Kafka topic phân vùng theo ID camera. PySpark Structured Streaming đọc dữ liệu theo các vi lô 1 giây. Cơ chế Watermark 10 phút đảm bảo hệ thống chấp nhận các gói tin bị trễ mạng nhưng không bị rò rỉ bộ nhớ. Thuật toán lọc trùng có trạng thái (Stateful Deduplication) sẽ gộp các lần nhận diện cùng một người trên cùng camera trong vòng 5 giây thành một sự kiện duy nhất, giảm 80% tải ghi dữ liệu."*

---

### PHẦN 3: KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG (THÀNH VIÊN 3 - 8 PHÚT)

#### Slide 18: Môi trường Phần cứng & 3 Bộ Dữ liệu Thực nghiệm
* **Nội dung hiển thị:** Cấu hình CPU Intel Core i7 / RAM 32GB / GPU RTX / Ubuntu & Windows; Bộ dữ liệu A (Test set góc nghiêng RTSP), Bộ dữ liệu B ($10^4$ đến $5 \times 10^6$ vectors 512-D), Bộ dữ liệu C (5 triệu log sự kiện đa camera).
* **Lời thoại (Speaker Notes):**
  > *"Em xin đại diện nhóm trình bày Phần 3 - Kết quả Thực nghiệm Định lượng. Toàn bộ thực nghiệm được nhóm triển khai trên 3 bộ dữ liệu độc lập: Bộ dữ liệu A đánh giá nhận diện khuôn mặt; Bộ dữ liệu B gồm các mốc quy mô từ 10.000 đến 1.000.000 vector 512 chiều chuẩn hóa để đo đạc chỉ mục FAISS; và Bộ dữ liệu C gồm 500.000 đến 5.000.000 sự kiện nhận diện đa camera để đánh giá Spark và Data Lake."*

#### Slide 19: Quy trình Tiền xử lý Dữ liệu 4 bước
* **Nội dung hiển thị:** Sơ đồ 4 bước: (1) Lọc mờ Laplacian $\rightarrow$ (2) Căn chỉnh Affine $112 \times 112$ $\rightarrow$ (3) Chuẩn hóa vector $L_2$ $\rightarrow$ (4) Làm sạch và ép kiểu Schema trên Spark.
* **Lời thoại (Speaker Notes):**
  > *"Dữ liệu đi qua pipeline tiền xử lý 4 bước nghiêm ngặt: Đầu tiên lọc bỏ khung hình mờ; kế tiếp căn chỉnh hình học; tiếp theo vector đầu ra được chuẩn hóa L2 để nằm chính xác trên mặt siêu cầu đơn vị; và cuối cùng các bản ghi sự kiện được định kiểu dữ liệu chặt chẽ theo Spark Schema để tối ưu hóa việc nén cột Parquet."*

#### Slide 20: Kịch bản 1 - Đánh giá TAR/FAR & Lựa chọn Ngưỡng Cosine
* **Nội dung hiển thị:** Biểu đồ Fig 2: Đường cong TAR (Cùng camera & Khác camera), FAR, FRR; Bảng số liệu tại các ngưỡng từ 0.30 đến 0.70; Vùng tối ưu $\tau = 0.50$ (TAR = 92.5%, FAR = 0.021%).
* **Lời thoại (Speaker Notes):**
  > *"Kịch bản thực nghiệm 1 khảo sát sự thay đổi của Tỷ lệ chấp nhận đúng (TAR) và Chấp nhận sai (FAR) theo ngưỡng Cosine. Trong điều kiện camera thực tế khác góc sáng, ở ngưỡng $\tau = 0.50$, hệ thống đạt tỷ lệ nhận diện đúng TAR 92.54%, trong khi tỷ lệ kẻ giả mạo lọt qua chỉ là 0.021% (tương đương chỉ 2 trên 10.000 lần thử). Đây là điểm cân bằng vàng được nhóm lựa chọn làm ngưỡng chuẩn cho toàn bộ hệ thống."*

#### Slide 21: Kịch bản 2 - Khả năng Mở rộng Quy mô Chỉ mục FAISS
* **Nội dung hiển thị:** Biểu đồ Fig 3: So sánh Độ trễ (ms) và QPS giữa FlatIP, IVFFlat, IVFPQ, HNSW từ 10K đến 1.000.000 vectors; Bảng số liệu tại mốc 1 triệu vector.
* **Lời thoại (Speaker Notes):**
  > *"Kịch bản 2 là thực nghiệm cốt lõi chứng minh tính mở rộng của Dữ liệu lớn. Khi quy mô cơ sở dữ liệu tăng từ 10.000 lên 1.000.000 vector: Phương pháp FlatIP quét cạn tăng độ trễ từ 0.8 ms lên 42.5 ms, thông lượng QPS sụp đổ từ 1.250 xuống chỉ còn 23 query/giây. Trong khi đó, IndexIVFPQ và HNSW giữ độ trễ ổn định ở mức chỉ từ 0.3 đến 0.5 ms, đạt thông lượng hơn 2.500 query/giây, nhanh gấp hơn 80 lần so với phương pháp truyền thống."*

#### Slide 22: Hiệu quả Tiết kiệm 96% Bộ nhớ RAM của IVF-PQ
* **Nội dung hiển thị:** Biểu đồ Fig 4: Dung lượng RAM tại mốc 1.000.000 vector: FlatIP tốn 2.048 MB, HNSW tốn 2.621 MB, trong khi IVFPQ chỉ tốn 76 MB (giảm 96.3% RAM).
* **Lời thoại (Speaker Notes):**
  > *"Đặc biệt, biểu đồ Hình 4 minh họa rõ nét sức mạnh vượt trội của kỹ thuật Lượng tử hóa tích. Tại quy mô 1 triệu người: Nếu dùng FlatIP, bộ nhớ tiêu tốn 2.048 MB RAM; HNSW do phải lưu các liên kết đồ thị nên tốn tới 2.621 MB. Nhưng với IVFPQ, dung lượng RAM được nén xuống chỉ còn vỏn vẹn 76 MB, tức tiết kiệm tới 96.3% RAM! Điều này đồng nghĩa với việc một máy chủ thông thường 32 GB RAM hoàn toàn có thể phục vụ cơ sở dữ liệu lên tới hàng chục triệu khuôn mặt mà không lo tràn bộ nhớ."*

#### Slide 23: Kịch bản 3 - Đánh đổi Pareto giữa Recall và Latency theo nprobe
* **Nội dung hiển thị:** Biểu đồ Fig 5: Đường cong Pareto Recall@1 / Recall@10 theo nprobe từ 1 đến 128; Điểm tối ưu $nprobe = 16 - 32$ đạt Recall@1 > 93%, Recall@10 > 98.5% với độ trễ < 0.45 ms.
* **Lời thoại (Speaker Notes):**
  > *"Trong Kịch bản 3, nhóm khảo sát siêu tham số nprobe trên chỉ mục IVFPQ. Khi nprobe tăng từ 1 lên 128, độ chính xác tìm kiếm Recall@1 tăng từ 68% lên 96%. Tuy nhiên, thời gian truy vấn cũng tăng theo. Phân tích đường cong biên Pareto cho thấy vùng $nprobe = 16$ đến $32$ là điểm tối ưu tuyệt đối: đạt độ chính xác Recall@1 trên 93%, Recall@10 đạt 98.5%, trong khi độ trễ vẫn duy trì cực thấp ở mức 0.38 ms."*

#### Slide 24: Kịch bản 4 - Hiệu năng Xử lý Luồng Spark khi Tải từ 10 đến 500 Camera
* **Nội dung hiển thị:** Biểu đồ Fig 6: Thông lượng xử lý (Events/sec) và Độ trễ đầu-cuối P95 (giây) theo số lượng camera; Hiện tượng Consumer Lag khi vượt ngưỡng 400 camera.
* **Lời thoại (Speaker Notes):**
  > *"Kịch bản 4 đánh giá khả năng chịu tải của cụm Kafka và Spark Streaming khi tăng số lượng camera từ 10 lên 500 luồng. Với tải 100 camera (1.000 sự kiện/giây), thời gian vi lô là 0.54 giây, độ trễ đầu-cuối P95 là 1.15 giây, Consumer Lag bằng 0. Khi tải tăng lên 500 camera (5.000 sự kiện/giây), Spark vẫn xử lý được 4.985 sự kiện/giây với độ trễ P95 là 3.45 giây, đáp ứng hoàn hảo tiêu chuẩn cảnh báo an ninh thời gian thực."*

#### Slide 25: Kịch bản 5 - Đánh giá Data Lake Parquet và Truy vết Hành trình Liên Camera
* **Nội dung hiển thị:** Bảng so sánh Parquet vs JSON (Nén dung lượng 80.5%, tốc độ truy vấn nhanh gấp 7.8 lần); Minh họa truy vết lộ trình nhân viên qua các khu vực và phát hiện cảnh báo nhảy cóc thời gian thực.
* **Lời thoại (Speaker Notes):**
  > *"Kịch bản 5 chứng minh hiệu quả của Data Lake Parquet so với lưu trữ văn bản JSON truyền thống: Dung lượng lưu trữ giảm 80.5% nhờ nén Snappy theo cột. Khi thực hiện truy vấn phân tích tổng hợp trên 500.000 bản ghi, định dạng Parquet với kỹ thuật Columnar Pushdown chỉ mất 0.08 giây, nhanh gấp 7.8 lần so với JSON (0.62 giây). Dựa trên dữ liệu này, nhóm đã xây dựng thuật toán Cross-Camera Tracking, tự động tái hiện lộ trình di chuyển và phát hiện các trường hợp đổi khu vực bất thường dưới 2 giây."*

---

### PHẦN 4: KẾT LUẬN & ĐỊNH HƯỚNG TƯƠNG LAI (THÀNH VIÊN 4 / TRƯỞNG NHÓM - 3 PHÚT)

#### Slide 26: Tổng kết các Đóng góp Khoa học và Thực tiễn của Đồ án
* **Nội dung hiển thị:** 4 đóng góp chính: (1) Kiến trúc lai hoàn chỉnh tận dụng camera RTSP; (2) Chứng minh toán học tối ưu siêu cầu; (3) Tối ưu chỉ mục IVF-PQ nén 96% RAM, latency < 0.5 ms trên triệu vector; (4) Pipeline Spark phân tán và Data Lake Parquet thời gian thực.
* **Lời thoại (Speaker Notes):**
  > *"Tóm lại, đồ án đã giải quyết trọn vẹn mục tiêu đề ra với 4 đóng góp cốt lõi: Đề xuất kiến trúc lai tận dụng camera IP hiện hữu; thiết lập cơ sở toán học vững chắc cho bài toán đối sánh trên siêu cầu; chứng minh khả năng nén 96% RAM và truy vấn siêu tốc của IVF-PQ; và xây dựng thành công pipeline dữ liệu lớn phân tán xử lý hàng ngàn sự kiện mỗi giây."*

#### Slide 27: Hạn chế của Hệ thống và Hướng Nghiên cứu Mở rộng
* **Nội dung hiển thị:** Hạn chế: Chưa tích hợp chống giả mạo khuôn mặt (Face Anti-Spoofing / Liveness) trên luồng camera, giới hạn cụm FAISS đơn node; Hướng mở rộng: Tích hợp Silent Liveness Detection, chuyển đổi sang cơ sở dữ liệu vector phân tán Milvus hoặc Qdrant trên Kubernetes.
* **Lời thoại (Speaker Notes):**
  > *"Nhóm cũng thẳng thắn nhìn nhận hai hạn chế hiện tại: Thứ nhất là hệ thống chưa tích hợp thuật toán phát hiện gian lận khuôn mặt 3D (Anti-Spoofing); thứ hai là chỉ mục FAISS hiện đang vận hành trên máy chủ đơn node. Hướng phát triển trong tương lai của nhóm là tích hợp mô hình Silent Liveness Detection để ngăn chặn hình thức giả mạo bằng màn hình điện thoại, và mở rộng sang hệ quản trị cơ sở dữ liệu vector phân tán Milvus hoặc Qdrant trên môi trường Kubernetes."*

#### Slide 28: Lời Cảm ơn và Phiên Hỏi đáp (Q&A)
* **Nội dung hiển thị:** Lời cảm ơn chân thành tới Giảng viên hướng dẫn ThS. Hà Minh Tân và Hội đồng; Thông tin liên hệ và link kho mã nguồn GitHub; Sẵn sàng cho phần Q&A.
* **Lời thoại (Speaker Notes):**
  > *"Nhóm xin chân thành cảm ơn Thầy Hà Minh Tân đã luôn tận tình hướng dẫn, định hướng khoa học và tạo điều kiện thuận lợi nhất cho nhóm trong suốt quá trình thực hiện đồ án. Nhóm xin trân trọng cảm ơn quý Thầy Cô trong Hội đồng đã chú ý lắng nghe. Chúng em rất mong nhận được những nhận xét, góp ý quý báu của Thầy Cô. Nhóm xin sẵn sàng bước vào phần trả lời câu hỏi! Em xin cảm ơn ạ!"*
