## String Function

- Để chạy 1 file trong CLI
```
source __filename__
```
### CONCAT
dùng để nối 2 cột với nhau
```
SELECT CONCAT(author_fname, " ", author_lname)
FROM books
```

hoặc như này
```
SELECT author_fname AS first, author_lname AS last, CONCAT(author_fname, author_lname) as Full_name
FROM books
```

### CONCAT_WS
concat with seperator
```
SELECT author_fname AS first, author_lname AS last, CONCAT_WS("-", author_fname, author_lname) as Full_name
FROM books
```

### substring
dùng để Slice cái string ra gần giống string trong python nhưng bắt đầu từ 1
- In ra từ chữ 1 đến chữ 4
```
SELECT SUBSTRING("Hello World", 1, 4);
```
- In ra từ chữ số thứ 7 trở đi
```
SELECT SUBSTRING("Hello World", 7);
```
- In ra từ chữ số 7 từ cuối về
```
SELECT SUBSTRING("Hello World", -7);
```

- Lấy từ chữ 1 đến chỗ 10 từ cột title trong bảng book
```
SELECT SUBSTRING(title, 1, 10) FROM books
```

### Replace
dùng để thay cho 1 đoạn ghép khác
- Thay chữ hell bằng chữ **** trong cụm từ Hello world
```
SELECT REPLACE ("Hello world", "Hell", "****")
```

**Lưu ý**: vì nó là case sensitive nên nếu bạn muốn thay chữ o bạn sẽ 
thay được chữ o nhưng không thay được chữ o in hoa `O`

- Thay chữ e bằng số 3 trong cột title ở bảng books
```
SELECT REPLACE(title, "e", 3) FROM books;
```

### Reverse
- Đảo ngược hết chữ lại
``` 
SELECT REVERSE("hello world")
```



### CHAR_LENGTH
- Dùng để đếm số lượng chữ trong string
```
SELECT CHAR_LENGTH("Hello")
```

### UPPER, LOWWER
- In đậm in hoa cái string ra thôi
```
SELECT UPPER("hello")
```







