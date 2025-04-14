
products = [{
    "제품명": "건망고 슬라이스",
    "가격": 4000,
    "분류": "식품",
    "원산지": "태국",
},  {
    "제품명": "건망고 슬라이스",
    "가격": 4000,
    "분류": "식품",
    "원산지": "태국",  # , 가 없으면 에러 발생생
}]

for product in products:
    for key in product:
        print(key)
        print(product[key])
        print()
    print("-" * 20)