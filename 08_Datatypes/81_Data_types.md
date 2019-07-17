### CHAR
**Đặc điểm**: sẽ luôn lấp đầy khoảng trống

Ví dụ: 
-  nếu bạn khai báo là Char(5) mà dòng text bạn nhập vào là 10 nó sẽ
cắt đoạn text đấy cho chiều dài bằng 5, 

-  nếu đoạn text là 2 nó sẽ thêm " " cho chiều dài đoạn text bằng 5

## VARCHAR 
**Đặc điểm**: khác biệt với char nó không lấp khoảng trống nếu thừa 
khoảng trống    

## Decimal
![image](https://user-images.githubusercontent.com/45547213/61365484-08fdb300-a8b2-11e9-9bc3-77d6f1a79505.png)

khi bạn thêm số 7 vào kết quả sẽ lã 7.00 vì bạn khai báo có 2 số đằng 
sau dấu chấm    

nếu bạn nhập 298.9999 thì nó sẽ thành 299.00

## Float và Double
có thể lưu số lớn nhưng tốn ít bộ nhớ hơn

![image](https://user-images.githubusercontent.com/45547213/61366882-a659e680-a8b4-11e9-9e12-e7b4744cd77d.png)

double to hơn float

**Lưu ý**: nếu cần chính xác tuyệt đối thì nên dùng decimal

## Time DateTime
Date Format: `YYYY-MM-DD`

Time Format: `HH:MM:SS`

DateTime Format: `YYYY-MM-DD HH:MM:SS`

CURDATE() - đưa cho ngày hôm nay

CURTIME() - đưa cho thời gian hiện tại

NOW() - đưa ngày tháng năm giờ phút hiện tại

## Các method của Date
- DAY(BIRTHDATE): lấy số ngày từ kiểu dữ liệu birthdate ra
- DAYNAME(BIRTHDATE): lấy tên của ngày trong tuần 
- DAYOFWWEEK(BIRTHDATE): lấy số ngày trong tuần
- DAYOFYEAR(BIRTHDATE): lấy số ngày trong năm
- Tương tự với Hour Minute

- Sử dụng date format:
```
SELECT DATE_FORMAT(birthdt, '%m/%d/%Y') FROM people;
```


## Date math
- DATEDIFF lấy ngày đầu trừ ngày cuối là ra số ngày
```
SELECT DATEDIFF(NOW(), birthdate) FROM people;
```

- Các cách để cộng ngày giờ phút giây 
```
SELECT birthdt, DATE_ADD(birthdt, INTERVAL 1 MONTH) FROM people;

SELECT birthdt, DATE_ADD(birthdt, INTERVAL 10 SECOND) FROM people;

SELECT birthdt, DATE_ADD(birthdt, INTERVAL 3 QUARTER) FROM people;

SELECT birthdt, birthdt + INTERVAL 1 MONTH FROM people;

SELECT birthdt, birthdt - INTERVAL 5 MONTH FROM people;

SELECT birthdt, birthdt + INTERVAL 15 MONTH + INTERVAL 10 HOUR FROM people;
```

## TimeStamp

TimeStamp chỉ hỗ trợ từ 1970 đến 2038 thôi

DateTime hỗ trợ từ 1000 đến 9999

TimeStamp tốn 4 byte còn DateTime tốn 8 bytes
