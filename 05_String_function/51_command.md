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
lướt hệt như trong python
