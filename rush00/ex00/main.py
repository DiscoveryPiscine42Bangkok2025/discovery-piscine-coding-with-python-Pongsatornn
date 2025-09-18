# from checkmate import checkmate

# def main():
# #     board = """\
# # R...
# # .K..
# # ..P.
# # ....\
# # """
    
# #     board = """\
# # ..
# # .K\
# # """
#     checkmate(board)

# if __name__ == "__main__":
#     main()

from checkmate import checkmate

def test_mixed_scenarios():
    print("=== เคสทดสอบแบบสุ่ม ===")
    
    test_cases = [
        # 1. มหาศึกใหญ่ - หลายตัวโจมตีพร้อมกัน
        ("1. มหาศึกใหญ่", """\
Q.R.
.B.P
..K.
....\
"""),
        
        # 2. เกมส์จบ - Queen กับ King เจอกัน
        ("2. เกมส์จบ", """\
QK..
....
....
....\
"""),
        
        # 3. ปราสาทล้อมโจมตี
        ("3. ปราสาทล้อมโจมตี", """\
R..R
....
.K..
R..R\
"""),
        
        # 4. Pawn Army โจมตี (ตามโค้ดเดิม)
        ("4. Pawn Army", """\
PP..
.PK.
PP..
....\
"""),
        
        # 5. เขาวงกต - ทางอึด
        ("5. เขาวงกต", """\
RPBR
P.KP
BPPR
RBBQ\
"""),
        
        # 6. ยักษ์ใหญ่ - กระดาน 5x5
        ("6. ยักษ์ใหญ่", """\
Q....
.....
..K..
.....
....R\
"""),
        
        # 7. การบุกทะลวง - Bishop vs Rook
        ("7. การบุกทะลวง", """\
B...
.R..
..K.
....\
"""),
        
        # 8. King หลบซ่อน
        ("8. King หลบซ่อน", """\
....
.PPP
.PKP
.PPP\
"""),
        
        # 9. สนามรบ - หมากเต็มไปหมด
        ("9. สนามรบ", """\
QRBP
PPPK
BRRQ
PPBR\
"""),
        
        # 10. โลกสงบ - ไม่มีการโจมตี
        ("10. โลกสงบ", """\
....
.Q.K
....
R...\
"""),
    ]
    
    for name, board in test_cases:
        print(f"{name}:")
        # แสดงกระดาน
        lines = board.strip().split('\n')
        for i, line in enumerate(lines):
            print(f"  แถว {i}: {line}")
        print(f"  ผลลัพธ์: ", end="")
        checkmate(board)
        print()

def test_edge_cases():
    print("=== เคสขอบเขต (Edge Cases) ===")
    
    edge_cases = [
        # 1. กระดานแปลก - ไม่ใช่สี่เหลี่ยม
        ("1. กระดานแปลก", """\
QK
R.
PPP\
"""),
        
        # 2. King หายตัว
        ("2. King หายตัว", """\
QRBP
PPRB
BRRQ
PPBR\
"""),
        
        # 3. Twin Kings
        ("3. Twin Kings", """\
K...
....
..Q.
...K\
"""),
        
        # 4. มินิกระดาน 2x2
        ("4. มินิกระดาน", """\
QK
..\
"""),
        
        # 5. กระดานใหญ่ 6x6
        ("5. กระดานใหญ่", """\
......
.Q....
......
...K..
......
.....R\
"""),
        
        # 6. กระดานเปล่า
        ("6. กระดานเปล่า", ""),
        
        # 7. กระดานบรรทัดเดียว
        ("7. บรรทัดเดียว", "QKR"),
        
        # 8. กระดานจิ๋ว 1x1
        ("8. จิ๋ว 1x1", "K"),
        
        # 9. มีแต่จุด
        ("9. มีแต่จุด", """\
....
....
....
....\
"""),
        
        # 10. ตัวเลขแปลกๆ
        ("10. ตัวเลขแปลก", """\
1K23
4567
89QR
BCDE\
""")
    ]
    
    for name, board in edge_cases:
        print(f"{name}:")
        print(f"  Input: {repr(board[:20])}{'...' if len(board) > 20 else ''}")
        print(f"  ผลลัพธ์: ", end="")
        checkmate(board)
        print()

def test_blocking_scenarios():
    print("=== เคสการบล็อก ===")
    
    blocking_cases = [
        # 1. Rook ถูก Pawn บล็อก
        ("1. Rook ถูก Pawn บล็อก", """\
R...
.P..
..K.
....\
"""),
        
        # 2. Bishop ถูก Queen บล็อก
        ("2. Bishop ถูก Queen บล็อก", """\
B...
.Q..
..K.
....\
"""),
        
        # 3. Queen ถูกบล็อกหลายชั้น
        ("3. Queen ถูกบล็อกหลายชั้น", """\
Q...
.P..
..R.
...K\
"""),
        
        # 4. King ไม่สามารถบล็อกได้ (ควร Success!)
        ("4. King ไม่บล็อกได้", """\
R...
.K..
..K.
....\
"""),
        
        # 5. ทางอ้อม - Queen หาทางใหม่
        ("5. ทางอ้อม", """\
QP..
....
..K.
....\
"""),
    ]
    
    for name, board in blocking_cases:
        print(f"{name}:")
        lines = board.strip().split('\n')
        for i, line in enumerate(lines):
            print(f"  แถว {i}: {line}")
        print(f"  ผลลัพธ์: ", end="")
        checkmate(board)
        print()

def test_pawn_weirdness():
    print("=== เคสพิเศษ Pawn (ตามโค้ดเดิม) ===")
    
    pawn_cases = [
        # 1. Pawn โจมตีทุกมุม (ตามโค้ดเดิม)
        ("1. Pawn ซ้าย-บน", """\
K...
.P..
....
....\
"""),
        
        ("2. Pawn ขวา-บน", """\
..K.
.P..
....
....\
"""),
        
        ("3. Pawn ซ้าย-ล่าง", """\
....
.P..
K...
....\
"""),
        
        ("4. Pawn ขวา-ล่าง", """\
....
.P..
..K.
....\
"""),
        
        # 5. Pawn กองกำลัง
        ("5. Pawn กองกำลัง", """\
KPK.
PPP.
KPK.
....\
"""),
    ]
    
    for name, board in pawn_cases:
        print(f"{name}:")
        lines = board.strip().split('\n')
        for i, line in enumerate(lines):
            print(f"  แถว {i}: {line}")
        print(f"  ผลลัพธ์: ", end="")
        checkmate(board)
        print()

def main():
    print("🏁 === ทดสอบโค้ด checkmate แบบครบครัน === 🏁")
    print()
    
    test_mixed_scenarios()
    print("=" * 60)
    
    test_edge_cases()
    print("=" * 60)
    
    test_blocking_scenarios()  
    print("=" * 60)
    
    test_pawn_weirdness()
    print("=" * 60)
    
    print("🎉 เสร็จสิ้นการทดสอบทั้งหมด! 🎉")

if __name__ == "__main__":
    main()