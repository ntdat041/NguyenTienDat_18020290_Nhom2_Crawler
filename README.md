# NguyenTienDat_18020290_Nhom2_Crawler
## Mô tả mã nguồn:
* Đây là mã nguồn cho việc crawl dữ liệu từ các trang báo hoặc trang thương mại điện tử, cụ thể là 3 trang [Vietnamnet](https://vietnamnet.vn/)
,[Lao Động](https://laodong.vn/) và [FPT Shop](https://fptshop.com.vn/)
* Mã nguồn sử dụng phiên bản Python 3.8 và phiên bản Scrapy 2.2.0
### Mã nguồn bao gồm:
* name: Tên của con bọ, với mục đích khi run mình sẽ gọi tên để chỉ định con bọ(spider) nào sẽ đi crawl cho mình
- start_urls: Có thể coi chính là địa chỉ bắt đầu cho spider
* total_pages= set() : tạo một tập hợp để tí nữa ta có thể đếm số link đã chạy và dừng lại
+ parse(): Là nơi mình viết code để điều khiển spider thực hiện những việc mình muốn làm như crawl dữ liệu rồi ghi vào file
_ yield scrapy.Request(response.urljoin(link),callback=self.parse): Lấy link được response trong next_links, rồi thực hiện lại hàm parse

## Các công việc đã thực hiện được:
* Lấy được dữ liệu từ các trang báo hoặc trang TMĐT
- Chạy được việc lan link
+ Có thể khống chế số lượng bài viết mong muốn
- Ghi dữ liệu ra file

## Kết quả thu được:
- Lấy được link bài viết, tiêu đề, nội dung, tags, chủ đề từ các bài báo của trang Vietnamnet và Lao Động
- Lấy được link sản phẩm, tên sản phẩm, giá hiện tại, giá gốc, đánh giá, ảnh, thông số kỹ thuật và mô tả của các sản phẩm ở trang FPT Shop
