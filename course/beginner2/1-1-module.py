from pytz import common_timezones, timezone, utc
from datetime import datetime

# datetime 활용

now = datetime.now()
# 시간을 나타내는 기본 문자열 지정
date_format = "%Y{0} %m{1} %d{2} %H{3} %M{4} %S{5}"
# date.strftime(format): 지정된 format 맞춰 시간을 표현
print(now.strftime(date_format).format(*"년월일시분초"))

# pytz 활용

# 시간을 나타내는 기본 문자열 지정
fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# common_timezones: pytz가 제공하는 지역 이름이 문자열로 저장되어있음
# find(): 찾았으면 1 아니면 0
for tz in list(common_timezones):
    if tz.lower().find("paris") >= 0:
        print(tz)
        # 아래는 같은 출력 다른 방식(대륙과 도시 이름을 알 때 사용)
        # timezone(도시 이름): common_timezones에 있는 도시 이름을 입력하면 대륙/도시이름을 출력함
        # tz_paris = timezone('Europe/Paris')
        # print(tz_paris)
    elif tz.lower().find("seoul") >= 0:
        # UTC 현재 시각
        tz_utc = timezone(utc.zone)
        now_utc = datetime.now(tz_utc)

        # print(type(tz)) # <class 'str'>
        tz_seoul = timezone('Asia/Seoul')
        # print(type(tz_seoul)) # <class 'pytz.tzfile.Asia/Seoul'>

        # astimezone(): ()안 type이 <class 'pytz.tzfile.Asia/Seoul'> 이어야함
        # now_seoul = now_utc.astimezone(tz) # 출력 에러 (type error)
        now_seoul = now_utc.astimezone(tz_seoul)  # 출력

        print(now_utc.strftime(fmt))
        print(now_seoul.strftime(fmt))

        # 따라서 astimezone()을 사용하려면
        # common_timezones, find() 조합을 사용할 수 없고
        # timezone()을 사용.
