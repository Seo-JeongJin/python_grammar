
text = "apple banana orange apple kiwi apple mango"

searching = input("찾을 문자열을 입력하세요: ")

words = [] # 단어 넣을 리스트
word = "" # 직접 공백 기준으로 단어 분리
for char in text: 
    if char != " ":
        word += char
    else:
        words.append(word)
        word = ""
        
if word: # 마지막 단어는 공백이 없기 때문에 마지막 단어까지 리스트에 추가
    words.append(word)
    
position = [] # 인덱스 찾을 리스트
count = 0
for i in range(len(words)):
    if searching == words[i]:
        count += 1
        position.append(i)
        
print(f"'{searching}은 총 {count}번 등장합니다.'")
print(f" 위치 (인덱스): {position}")