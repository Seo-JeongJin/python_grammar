
# 오전 오후 구분
from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))
if today.hour < 12:
    print("오전입니다.")
if today.hour >= 12:
    print("오후입니다.")