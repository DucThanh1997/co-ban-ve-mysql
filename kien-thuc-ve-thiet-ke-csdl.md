# Các bước thiết kế cơ sở dữ liệu bao gồm các bước sau
- Khảo sát yêu cầu
- Thiết kế ER
- Lược đồ quan hệ
- Hệ quản trị CSDL quan hệ

# Bước 1: Khảo sát yêu cầu
Đây là bước đầu tiên cũng là bước quan trọng nhất. Xác định yêu cầu một cách đầy đủ,
cụ thể sẽ giúp cho việc thiết kế CSDL trở lên dễ dàng hơn. Luôn đặt ra câu hỏi:

- CSDL sẽ được sử dụng như thế nào?
- Những thông tin gì cần được lưu vào CSDL?

Chúng ta có thể tham khảo các hệ thống dữ liệu sẵn có. Có thể là trong hoá đơn bán hàng, tập lưu trữ hồ sơ khách hàng.. vv.v.v
# Bước 2: Thiết kế mô hình thực thể liên kết (ER)
![image](https://user-images.githubusercontent.com/45547213/50875328-70661200-13fa-11e9-88ab-4c42261d6d80.png)
## Các thành phần có trong mồ hình thực thể liên kết
### Các kiểu quan hệ
1-1

1-n

n-1

n-n

Ngoài ra còn kiểu min max này nữa
![image](https://user-images.githubusercontent.com/45547213/50881899-9cdb5780-1415-11e9-9166-ffe40ec83915.png)
![image](https://user-images.githubusercontent.com/45547213/50876142-37c83780-13fe-11e9-9aa8-9d092469d972.png)
### Các kiểu thực thể
- Thực thể thường: Có khóa chính đầy đủ 
- Thực thể yếu: 
    
    Không có khóa chính. 

    Được xác định bằng cách liên kết với các thực thể khác phối hợp với một số giá trị thuộc tính của nó (kiểu thực thể nào cũng được)

    Mô tả kiểu thực thể yếu và liên kết xác định bằng hình chữ nhật và hình thoi nét đôi

![image](https://user-images.githubusercontent.com/45547213/50876266-c63cb900-13fe-11e9-86dd-37cecfdebac8.png)
### Các kiểu liên kết
- Liên kết thường: 1 đường
- Liên kết xác định 2 đường để xác định cho cái thực thể 

### Các kiểu thuộc tính
- thuộc tính thường
- thuộc tính khóa
- thuộc tính đa trị: tức là thuộc tính này có thể có nhiều giá trị
   
   Ví dụ thuộc tính ngôn ngữ nói được có nhiều giá trị: nói được tiếng anh,tiêng ta, tiếng tàu
- thuộc tính phức hợp: thuộc tính phức hợp là thuộc tính được tạo từ những thuộc tính đơn khác nhau.

    Ví dụ: Thuộc tính Ngày sinh là gộp của 3 thuộc tính ngày, tháng và năm sinh.

### Các kiểu ràng buộc

* Ràng buộc tham gia toàn bộ : kí hiệu -> hoặc ==
* Ràng buộc tham gia bộ phận : kí hiệu --
![image](https://user-images.githubusercontent.com/45547213/50876337-25023280-13ff-11e9-8aae-9494f1ac5767.png)
## Các bước thiết kế mô hình thực thể liên kết

1. Xác định tập thực thể
2. Xác định mối quan hệ
3. Xác định thộc tính và gắn thuộc tính cho tập thực thể
4. Quyết định miền giá trị
5. Quyết định thuộc tính khóa
6. Xác định ràng buộc(tỉ số min max)


# Bước 3 Tạo lược đồ quan hệ
## Với quan hệ 1-1
Đưa mỗi thực thể thành 1 bảng.Chuyển khóa chính của bảng này thành khóa ngoại của bảng kia

Ví dụ:
![image](https://user-images.githubusercontent.com/45547213/50884704-4cb4c300-141e-11e9-8410-06499d9b1ce4.png)

![image](https://user-images.githubusercontent.com/45547213/50884864-aae1a600-141e-11e9-9995-40229f6a6040.png)

## Với quan hệ 1-n
Chuyển khóa chính của bảng bên 1 sang làm khóa chính của bảng bên n
![image](https://user-images.githubusercontent.com/45547213/50884936-e11f2580-141e-11e9-94be-380d629ae49e.png)

## Với quan hệ n-n
Đưa 2 cái thực thể thành 1 bảng bình thương rồi đưa cái liên kết của nó thành 1 bảng có 2 khóa chính là 2 khóa chính của 2 thực thể kia. 


![image](https://user-images.githubusercontent.com/45547213/50884995-0ad84c80-141f-11e9-82b2-f2c6208592bf.png)

# Bước 4 Dựa vào các cái bảng ở phần lược đồ quan hệ tạo các bảng và kiểu dữ liệu trên mysql bằng các câu lệnh
























