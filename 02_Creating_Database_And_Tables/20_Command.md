- Tạo database: **create database hello_world**
- Xóa database: **drop database hello_world**
- Sử dụng database: **use database hello_world**

## Tables - Bảng
- Nôm na database là 1 đống các bảng
- Các bảng chứa dữ liệu
- Columns (cột) là nơi chứa các header để cấu trúc dữ liệu
- Row(dòng) là các dữ liệu
- Trong 1 bảng cần có sự thống nhất về kiểu dữ liệu giữa các cột
 với nhau

Dưới đây là các kiểu dữ liệu 

![image](https://user-images.githubusercontent.com/45547213/61262425-5cd3a380-a7af-11e9-82f4-aff660ae0e20.png)

thường sẽ dùng int cho number và varchar cho string khi khai báo varchar
phải khai báo max có bao nhiêu chữ

- Cú pháp tạo 1 bảng

``` 
CREATE TABLE "TABLE_NAME"
(
    COLUMN_NAME DATA_TYPE,
    COLUMN_NAME DATA_TYPE,
)
```

- Xem tất cả bảng trong database : **show tables**
- Xem tất cả các cột từ bảng: **show columns from cat** hoặc
**DESC cat**

- Xóa 1 bảng trong database: **drop table TABLE_NAME**

