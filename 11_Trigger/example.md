## Triggered

giả sử nếu Triggered là 1 skill của 1 hero thì nó là skill passive vì nó 
sẽ chạy ngầm còn Procedure là skill active

Triggered dành cho hoạt động thêm sửa xóa 

Ví dụ check tuổi rồi mới cho insert vào

```
DELIMITER $$

CREATE TRIGGER must_be_adult
     BEFORE INSERT ON users FOR EACH ROW
     BEGIN
          IF NEW.age < 18
          THEN
              SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Must be an adult!';
          END IF;
     END;
$$

DELIMITER ;
```

DELIMITER $$ để làm gì

như bạn thấy ở trigger này có nhiều dấu chấm phẩy, mà theo nguyên lí của 
sql thì sau dấu chấm phẩy nó sẽ ko chạy tiếp nữa mà chỉ excute đến đấy 
thôi , vậy nên ở đây dùng delimiter $$ để pass qua mấy cái chấm phẩu này

- xem có bao nhiêu trigger: `show trigger`

- xóa trigger: `drop trigger trigger_name`
