### COUNT
dùng để đếm số bản ghi query ra được
```
SELECT COUNT(*) FROM books
```
- Đếm số dòng có title chứa chữ the
```
SELECT COUNT(*) FROM books WHERE title LIKE "%the%";
```

### GROUP BY
dùng để gộp số bản ghi lại với nhau
- Đếm số tác phẩm 1 nhà văn viết
```
SELECT author_fname, author_lname, COUNT(*) FROM books GROUP BY author_lname;
```
- Đếm số tác phẩm ra đời trong 1 năm
```
SELECT CONCAT("IN ", released_year, " ",  COUNT(*), " released") AS thong_ke  FROM books GROUP BY released_year;
```

### MIN, MAX
- Lấy ra tên tác phẩm và số trang của tác phẩm dài nhất và ngắn nhất
```
SELECT title, MAX(pages) FROM books;
SELECT title, MIN(pages) FROM books;
```

### SUM
- Tính tổng của 1 cột nào đó
```
SELECT sum(pages) FROM books
```
- Tính tổng số trang 1 author viết
```
SELECT author_fname, author_lname, sum(pages) FROM books 
GROUP BY author_fname, author_lname;
```

### AVG
- Tính trung bình cộng của 1 cột
```
SELECT AVG(pages) from books
```
- Tính 1 năm trung bình có bao nhiêu trang
```
SELECT released_year, AVG(pages) FROM books GROUP BY released_year;
```
