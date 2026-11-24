import random
import pandas as pd
import streamlit as st

issues_list = ["난민", "영토분쟁", "기후변화", "무역갈등"]
countries_list = ["한국", "중국", "일본", "미국", "영국", "이란", "시리아"]

refugee_policies = [
    ["지원금 부여제도", "난민의 경제적 부담 감소"],
    ["거주지 무료 제공제도", "난민이 안전하게 거주 가능"],
    ["언어 및 직업 교육 지원", "현지 사회 적응 및 자립 능력 향상"],
    ["긴급 의료 지원 확대", "취약계층 난민의 생명 보호 및 건강 증진"],
    ["난민 아동 교육권 보장", "미래 세대의 학습 공백 방지"],
    ["국제기구 연대 기금 조성", "안정적인 구호 물품 조달"],
    ["심리 상담 치료 프로그램", "전쟁 및 이주 트라우마 극복 지원"],
]

territory_policies = [
    ["국제사법재판소(ICJ) 중재 요청", "평화적이고 법적인 분쟁 해결 도모"],
    ["공동 개발 구역 설정", "경제적 이익 공유를 통한 군사적 긴장 완화"],
    ["정기 외교 실무 회담 개최", "상호 신뢰 구축 및 오해 방지"],
    ["비무장 완충 지대 설치", "우발적 무력 충돌 원천 차단"],
    ["다자간 평화 협정 체결", "주변국 보증을 통한 영구적 평화 정착"],
    ["역사·지리 공동 연구 위원회", "객관적 사료 검증으로 갈등 해소"],
    ["민간 교류 및 문화 협력 확대", "상호 적대감 완화 및 우호 증진"],
]

climate_policies = [
    ["탄소배출권 거래제 강화", "기업의 온실가스 감축 유도"],
    ["신재생 에너지 보조금 확대", "화석 연료 의존도 감소 및 친환경 전환"],
    ["일회용 플라스틱 사용 규제", "해양 및 토양 환경 오염 방지"],
    ["기후 취약국 기술 지원", "글로벌 탄소 중립 달성 가속화"],
    ["도심 내 대규모 산림 조성", "탄소 흡수원 확대 및 열섬 현상 완화"],
    ["친환경 대중교통 인프라 확충", "수송 부문 온실가스 배출 저감"],
    ["기업 ESG 경영 공시 의무화", "지속 가능한 친환경 산업 생태계 구축"],
]

trade_policies = [
    ["자유무역협정(FTA) 재협상", "관세 장벽 완화로 교역 활성화"],
    ["세계무역기구(WTO) 분쟁 해결 활용", "불공정 무역 행위 시정"],
    ["수출입 다변화 전략 추진", "특정 국가에 대한 경제 의존도 축소"],
    ["핵심 산업 기술 보호법 제정", "자국 산업 경쟁력 보호 및 기술 유출 방지"],
    ["글로벌 공급망 공동 모니터링", "원자재 수급 불안정 조기 대응"],
    ["디지털 통상 규범 표준화", "신산업 분야 무역 마찰 예방"],
    ["중소기업 수출 바우처 지원", "수출 기업의 해외 판로 개척 지원"],
]


def recommend_policies(issue, count):
    if issue == "난민":
        selected_list = refugee_policies
    elif issue == "영토분쟁":
        selected_list = territory_policies
    elif issue == "기후변화":
        selected_list = climate_policies
    else:
        selected_list = trade_policies

    return random.sample(selected_list, count)


st.title("국제 문제 해결을 위한 정책 추천서")

selected_issue = st.selectbox("(1) 국제 문제 선택 :", issues_list)
selected_country = st.selectbox("(2) 국가 선택 :", countries_list)
numbers = st.slider(
    "(3) 추천 정책 개수 입력 :", min_value=1, max_value=10, value=2
)

if st.button("추천받기"):
    st.divider()
    if numbers > 7:
        st.error("추천 정책 개수를 초과하였습니다.")
    else:
        st.write(
            f'"{selected_country}의 {selected_issue}문제를 선택하였습니다."'
        )

        result_list = recommend_policies(selected_issue, numbers)

        table_data = []
        for i in range(len(result_list)):
            table_data.append([i + 1, result_list[i][0], result_list[i][1]])

        df = pd.DataFrame(table_data, columns=["정책 번호", "정책 이름", "효과"])
        st.subheader("정책 추천서")
        st.table(df.set_index("정책 번호"))

        chosen_policy_num = random.randint(1, numbers)
        st.write(f'"내가 선택한 정책은 {chosen_policy_num}이다."')
