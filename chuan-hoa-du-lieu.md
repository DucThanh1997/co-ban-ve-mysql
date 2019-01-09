# Phụ thuộc hàm
## Định nghĩa
Cái này giải thích hẳn ra thì khá khó nhưng có thể hiểu như này

SV (MSV, tên, tuổi, giới tính)

khi bạn biết msv thì bạn biết được tuổi và tên

đó là phụ thuộc hàm

1 ví dụ nữa nhé
MuonSach(MaThe,MaSach,NgayMuon,NgayTra)

khi bạn biết mã thẻ và mã sách thì bạn biết được ngày mượn

đó cũng là phụ thuộc hàm
Ký hiệu ` X -> Y `

## Các kiểu phụ thuộc hàm
Phụ thuộc hàm đầy đủ: Một phụ thuộc hàm X -> Y gọi là phụ thuộc hàm đầy đủ nếu khi loại bỏ bất kỳ 
thuộc tính A nào ra khỏi X thì phụ thuộc hàm không còn đúng nữa.

Phụ thuộc hàm bộ phận: Một phụ thuộc hàm X -> Y là phụ thuộc hàm bộ phận nếu có thể bỏ một thuộc tính A ra khỏi X mà phụ thuộc hàm vẫn đúng

![image](https://user-images.githubusercontent.com/45547213/50892616-8a6f1700-1431-11e9-903d-af9ccde8899e.png)

## Các quy tắc phụ thuộc hàm
![image](https://user-images.githubusercontent.com/45547213/50892687-affc2080-1431-11e9-87c9-b4349be6c7ff.png)

# Chuẩn hóa
## Định nghĩa:
Chuẩn hóa là quá trình phân tích lược đồ quan hệ dựa trên các phụ thuộc hàm và khóa chính để đạt được:

## Chức năng
- Giảm tối đa sự dư thừa
- Giảm tối đa các thao tác cập nhật dị thường

## Các kiểu chuẩn hóa
### Chuẩn hóa 1NF
#### Đặc điểm 
Thuộc tính không thể là thuộc tính đa trị, hay phức hợp

Chỉ có thể là thuộc tính đơn

```
SV_DIEM(__Masv__,__Mamon__, Diem)
Thỏa mãn dạng chuẩn 1

SV(__Masv__, Hoten,Gioitinh,Ngaysinh, Noisinh)
Không thỏa mãn do thuộc tính Hoten có chứa 3 giá trị : HO,TENDEM,TEN
```

### Chuẩn hóa 2NF
#### Đặc điểm
Là dạng chuẩn 1

Mọi thuộc tính không khóa của R phụ thuộc hàm đầy đủ vào khóa chính
![image](https://user-images.githubusercontent.com/45547213/50894725-8ee9fe80-1436-11e9-8eb1-4ea68fd9e42f.png)

### Chuẩn hóa 3NF
#### Đặc điểm
Là dạng chuẩn 2

Không có thuộc tính không khoá nào của R là phụ thuộc bắc cầu vào khoá chính.
```
NV_DV(Manv, Hoten, Ngaysinh, Madv, Tendv, MaQl)
Manv->Madv
Madv->Tendv ==> Manv -> Tendv : bắc cầu
MaDv->MaQl ==> Manv -> MaQl : bắc cầu
DV(Madv, Tendv, MaQl)
NV(Manv, Hoten, Ngaysinh, Madv)
```






