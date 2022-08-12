# cis-sciweek-tester

## install package
```batch
pip install alive-progress
```

## ลำดับการทำงาน
1. นำไฟล์ผู้เข้าแข่งขันไว้ที่โฟลเดอร์ `answers`
2. เปิดไฟล์และเปิดการทำงาน `prepairfile.py` เพื่อทำการโหลดไฟล์ผู้เข้าแข่งขันทั้งหมดไปที่โฟลเดอร์ `input`
3. เปิดการทำงานไฟล์ `test.py` เพื่อทำการโหลดและตรวจคำตอบ
4. คะแนนที่ได้จะบันทึกไปยังไฟล์ `score.xlsx`