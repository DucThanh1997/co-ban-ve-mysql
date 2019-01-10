# Import
Có 3 cách để import file dữ liệu vào database
## Import từ file text
Cấu trúc:
```
mysqlimport -u user_name -p database_name /var/lib/mysql-files/table_name.txt
```
Dữ liệu trong file text sẽ được tải vào bảng có tên cùng với tên file text. 
Nếu bảng chưatồn tại, chương trình sẽ tự tạo bảng mới. Định dạng của file text phải được trình bày theo quy định sau :

- Mỗi dòng dữ liệu được trình bày trên 1 dòng.
- Giá trị text phải được đóng bằng dấu nháy đơn (') hoặc nháy kép (").
- Các giá trị cách bởi dấu phẩy (,).
- Các giá trị phải được sắp theo thứ tự tương ứng

Ví dụ ta có file a.txt dưới dạng
```
'thanh'
```

Bây giờ chúng ta tạo database, tạo bảng a 
```
CREATE DATABASE db1;
USE db1;
CREATE TABLE a(ten VARCHAR(20));
```

Sau đó import file a.txt vào bảng a

` mysqlimport -u root -p db1 /var/lib/mysql-files/a.txt `

## Insert dữ liệu bằng tay thẳng vào bảng

```
USE db1
INSERT INTO a
VALUES
('Thanh');
```

## load data infile
```
USE db1
LOAD DATA INFILE "/home/a.txt" INTO TABLE a(ten);

# Export
## SQL dump
export cả database
```
mysqldump database_name > filename.txt
```

Ví dụ
```
mysqldump db1 > /home/thanh/db1.txt
```

export 1 bảng
```
mysqldump –u username –p database_name table_name > filename.txt
```

Ví dụ
```
mysqldump db1 a > /var/lib/mysql-files/a.txt
```

## Selcet into outfile
```
Select column_names from table_name Into Outfile filename.txt[ Fields Terminated by char 
Enclosed by char Lines Terminated by char ];
SELECT * FROM Customer INTO OUTFILE '/var/lib/mysql-files/SinhVien.txt' FIELDS TERMINATED BY ',' 
ENCLOSED BY ' " ' LINES TERMINATED BY '\r\n';
#Nội dụng file vừa tạo
...
"Ngo","Van","Ma","1234"
"Nguyen","Vi","Vu","3434"
"Nong","Quoc","Tuan","1424"
...
```












