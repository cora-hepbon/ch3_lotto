import random
import streamlit as st

# 페이지 제목 설정
st.title("🎰 로또 번호 생성기")

# 세션 상태(Session State) 초기화: 버튼을 눌러도 이전 데이터가 유지되도록 함
if "lotto_history" not in st.session_state:
    st.session_state.lotto_history = []


# 공 색상 및 글자색 반환 함수
def get_ball_style(num):
    if num <= 10:
        bg_color, text_color = "#fbc02d", "#333333"  # 노란색
    elif num <= 20:
        bg_color, text_color = "#1e88e5", "#ffffff"  # 파란색
    elif num <= 30:
        bg_color, text_color = "#e53935", "#ffffff"  # 빨간색
    elif num <= 40:
        bg_color, text_color = "#8e8e8e", "#ffffff"  # 회색
    else:
        bg_color, text_color = "#43a047", "#ffffff"  # 초록색

    return f"""
    <div style="
        display: inline-block;
        width: 40px;
        height: 40px;
        line-height: 40px;
        border-radius: 50%;
        background-color: {bg_color};
        color: {text_color};
        font-weight: bold;
        text-align: center;
        margin: 4px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
    ">{num}</div>
    """


# [로또번호 생성] 버튼
if st.button("[로또번호 생성]"):
    # 1~45 중복 없는 6개 번호 무작위 추출 및 정렬
    new_numbers = sorted(random.sample(range(1, 46), 6))

    # 생성된 번호 세트를 리스트에 추가
    st.session_state.lotto_history.append(new_numbers)

    # 5개가 넘어가면 가장 오래된 세트(첫 번째) 삭제
    if len(st.session_state.lotto_history) > 5:
        st.session_state.lotto_history.pop(0)

# 추출 결과 화면에 출력
if st.session_state.lotto_history:
    st.write("---")
    for idx, lotto_set in enumerate(st.session_state.lotto_history, start=1):
        # 로또 공 HTML 태그 합성
        balls_html = "".join([get_ball_style(num) for num in lotto_set])

        # 화면 출력
        st.markdown(
            f"""
            <div style="
                background-color: #f8f9fa; 
                padding: 10px; 
                border-radius: 8px; 
                margin-bottom: 10px;
                display: flex;
                align-items: center;
                gap: 10px;
            ">
                <span style="font-weight: bold; color: #555; width: 60px;">Set {idx}:</span>
                <div>{balls_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )