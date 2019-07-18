### NOT EQUAL
```
!=
SELECT title FROM books WHERE released_year != 2017
```

### NOT LIKE
```
 NOT LIKE
 SELECT title FROM books WHERE title NOT LIKE "%w%"
 ```

### GREATER THAN
```
SELECT * FROM books WHERE released_year > 2000
SELECT title, stock_quantity FROM books WHERE stock_quantity > 100
```

### LESS THAN
```
SELECT * FROM books WHERE released_year < 2000
```

### AND
```
SELECT * FROM books WHERE author_lname = "Eggers AND released_year > 2010;
```

**Lưu ý**: có 2 cách 1 là dùng AND 2 là dùng &&

### OR
```
SELECT title, author_lname, released_year FROM books
WHERE author_lname = "Eggers" || released_year > 2010;
```

### BETWEEN
```
SELECT title, released_year FROM books WHERE released_year 2004 AND 2010;
```
tương tự với `NOT BETWEEN`

### CAST
dùng để ép kiểu
```
SELECT CAST("2019-05-07" AS DATE)
```

### IN
lấy những phần tử có trong ngoặc ở IN
```
SELECT title, author_lname, released_year FROM books
WHERE author_lname IN ("Eggers", "Carver", "Smith");
```

ngược lại với NOT IN

### CASE
```
SELECT title , released_year 
    CASE 
        WHEN released_year > 200 then "Mordern list"
        ELSE "20th century list"
    END  AS gerne
from books;
