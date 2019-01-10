# Quản lý user và phân quyền
## Tạo user
```
CREATE USER 'thanh'@'localhost' IDENTIFIED BY 'thanh1997';
```
## Xóa user
```
DROP USER 'thanh'@'localhost'
```
Chỉ những user có quyền root mới làm được

## Phân quyền
### Phân quyền 1 số quyền
cú pháp
```
GRANT [permission type] ON [database name].[table name] TO ‘thanh’@'localhost’;
FLUSH PRIVILEGES;
#Ví dụ
GRANT SELECT,UPDATE ON mydb.nguoi TO 'thanh'@'localhost';
FLUSH PRIVILEGES;
```
Permission type:
* CREATE – Cho phép user tạo databases/tables
* SELECT – Cho phép user truy xuất data
* INSERT – Cho phép user tạo thêm dòng trong bảng
* UPDATE – Cho phép user chỉnh sửa các entry trong bảng
* DELETE – Cho phép user xóa entry trong bảng
* DROP – Cho phép user xóa hoàn toàn bảng/database

### Phân quyền root 
```
GRANT ALL PRIVILEGES ON * . * TO 'dung1'@'localhost';
#Thay đổi ngay lập tức
FLUSH PRIVILEGES;
```
## Thu hồi quyền
### Thu hồi tất cả quyền
```
REVOKE ALL PRIVILEGES ON *.* FROM 'non-root'@'localhost';
FLUSH PRIVILEGES;
```
### Thu hồi 1 số quyền nhất định
```
REVOKE [permission type] ON [database name].[table name] FROM ‘dung1’@‘localhost’;
FLUSH PRIVILEGES;
#Ví dụ
REVOKE UPDATE ON mydb.nguoi FROM ‘dung1’@‘localhost’;
FLUSH PRIVILEGES;
```
