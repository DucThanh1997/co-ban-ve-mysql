- Cách thêm data vào bảng

```
INSERT INTO TABLE_NAME (column, columns)
VALUES(data1, data2)
```

- Cách đọc toàn bộ data từ bảng
```
SELECT * from TABLE_NAME
```

- Bạn cũng có thể INSERT nhiều dòng 1 lúc:
```
INSERT INTO TABLE_NAME (column, columns)
VALUES(data1, data2),
      (data3, data4),
      (data5, data6)
```

- Bạn có thể in ra các warning bằng cách

` show warnings `

## NULL, NOT NULL

NULL là khi insert dữ liệu vào dòng đấy được bỏ trống

NOT NULL là ngược lại

thì vấn đề ở đây là bạn có thể đặt cho các trường này khi tạo bảng và
tạo các cột

## DEFAULT 
default là giá trị sẽ được insert vào nếu chúng ta để trống trường dữ liệu
đó,

default được set khi tạo bảng
```
CREATE TABLE cats3
(
    name VARCHAR(20) DEFAULT "no name provided",
    age INT DEFAULT 99
)
```

### Lưu ý: 
Khi đã set not null rồi thì sẽ không truyền vào null được nữa 


## Primary Key
**Định nghĩa: Là cái để phân biệt các dòng trong bảng với nhau**
```
CREATE TABLE unique_cats 
( name VARCHAR(30),
  age INT,
  catID INT NOT NULL,
  primary key(catID)
);
```
chúng ta cũng có thể để cho catID tức primary key tự động tăng 1 đơn vị
```

