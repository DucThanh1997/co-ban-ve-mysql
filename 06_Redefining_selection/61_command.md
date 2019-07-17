### Distinc
Loại bỏ các giá trị trùng nhau khi select
```
SELECT DISTINCT author_lname, author_rname FROM books;
```

### Sorting
- Sắp xếp theo alphabet với bảng chứa dữ liệu dạng text còn theo giá trị
số với bảng có chứa dữ liệu dạng number
```
SELECT author_lname FROM books ORDER BY author_lname DESC;
SELECT released_year FROM books ORDER By released_year DESC;
```
- Ta có thể viết kiểu short_cut 
```
SELECT title, author_fname, author_lname
FROM books ORDER_BY 2
```
2 ở đây là viết tắt cho author_fname

- Sort 2 tiêu chí
```
SELECT author_fname, author_lname
FROM books ORDER BY author_fname, author_lname;
```
sau khi sort bằng author_fname thì sort bằng author_lname


### LIMIT
Dùng để giới hạn số dòng in ra
```
SELECT title FROM books LIMIT 3;
```
Lấy 5 cuốn sách mới được xuất bản nhất
```
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 5;
```
cách khác
```
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 0,5;
```
Lấy top 2 đến top 4 cuốn sách mới nhất
```
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 2,4;
```

### LIKE
tìm tất cả các bản ghi có chứa từ đằng sau từ like
```
SELECT * FROM books WHERE author_fname LIKE "%da%";
```
**Lưu ý**: mấy %da lấy từ trước thôi không lấy từ sau Ví dụ Freida
                da% lấy từ sau thôi không lấy từ trước Ví dụ Dan
                %da% lấy cả trước lẫn sau

```
SELECT stock_quantity FROM books WHERE stock_quantity LIKE "____"
```
Tìm những cái books có stock chứa 4 chữ số

