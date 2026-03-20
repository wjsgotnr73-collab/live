import requests

def get_exchange_rate():
    # 1. 환율 데이터를 가져올 주소 (KRW 기준)
    # 이 주소는 별도의 키 없이 연습용으로 제공되는 주소입니다.
    url = "https://open.er-api.com/v6/latest/KRW"

    try:
        # 2. 데이터 요청하기
        response = requests.get(url)
        data = response.json() # 가져온 데이터를 파이썬 딕셔너리 형태로 변환

        if data["result"] == "success":
            # 3. 원하는 통화의 환율 가져오기 (예: USD, JPY)
            rates = data["rates"]
            
            usd_rate = 1 / rates["USD"]  # 1달러당 원화 가격
            jpy_rate = (1 / rates["JPY"]) * 100 # 100엔당 원화 가격

            print(f"현재 실시간 환율 정보입니다.")
            print(f"💵 1 달러(USD): {usd_rate:.2f} 원")
            print(f"💴 100 엔(JPY): {jpy_rate:.2f} 원")
            
            # 4. 계산 기능
            won = int(input("\n환전할 원화(KRW)를 입력하세요: "))
            usd_result = won * rates["USD"]
            print(f"👉 {won}원은 약 {usd_result:.2f} 달러입니다.")

        else:
            print("데이터를 가져오는 데 실패했습니다.")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

# 실행
get_exchange_rate()