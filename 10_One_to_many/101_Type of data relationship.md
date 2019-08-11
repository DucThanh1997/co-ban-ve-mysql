## Type
One to many: 1 tác giả có thể viết nhiều sách

Primary Key: là cái để phân biệt các bản ghi các đối tượng với nhau

Foreign Key: là cái id nối relationship từ bảng này sang bảng khác

## Join
- Inner Join
![image](https://user-images.githubusercontent.com/45547213/61436620-669f0780-a965-11e9-87e0-7c44e2e334dc.png)

```
SELECT first_name, last_name, amount, order_date
FROM customer
JOIN orders
    ON customer.id = orders.customer_id
```

- Left Join
![image](https://user-images.githubusercontent.com/45547213/61437180-a9151400-a966-11e9-9296-d27235383ff3.png)

```
SELECT first_name, last_name, order_date, IFNULL(SUM(amount), 0) AS total_spend
FROM customer
LEFT JOIN orders
    ON customer.id = orders.customer_id
GROUP BY customer.id
ORDER BY total_spend;
```

- Right Join
![image](https://user-images.githubusercontent.com/45547213/61438764-66553b00-a96a-11e9-807b-d134b87d760c.png)

```
