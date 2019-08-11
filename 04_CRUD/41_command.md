## read

- Xem hết cả bảng:
```
SELECT * from TABLE_NAME
```
- Xem 1 hay nhiều cột bất kì trong bảng:
```
SELECT column_name1, column_name2, column_name3 from table_name
```

### where
cái này thường để thêm điều kiện vào CRUD
- lấy những con mèo có tuổi = 4
```
SELECT * FROM cats WHERE age=4
```

**Lưu ý: dấu "=" có case sensitive nên dù in hoa hay in thường nó vẫn sẽ
in ra**

### Aliases
dùng để đổi tên cột khi hiện ra kết quả
```
SELECT name AS 'cat name', breed AS 'kitty breed' FROM cats;
```

## UPDATE
dùng để sửa các dòng đã được thêm vào có điều kiện thỏa mãn
```
UPDATE cats SET breed = "shorthair" WHERE breed = "tabby";
```

### Lưu ý: trước khi update hãy thử select trước để kiểm tra xem có đúng
dòng mình muốn update không

## DELETE
- dùng để xóa các dòng có điều kiện thỏa mãn
```
DELETE FROM cats WHERE name = "Egg";
```

- dùng để xóa toàn bộ
```
DELETE FROM cats;
```

