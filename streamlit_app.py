import streamlit as st

st.set_page_config(page_title="자기소개", layout="centered")

# 헤더
st.title("👋 안녕하세요!")
st.subheader("저를 소개합니다")

st.divider()

# 기본 정보
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://via.placeholder.com/200", caption="프로필 사진")

with col2:
    st.markdown("""
    **이름:** 홍길동
    
    **직책:** 개발자
    
    **위치:** 서울, 대한민국
    
    **이메일:** hong@example.com
    """)

st.divider()

# 자기소개
st.header("📖 소개")
st.write("""
안녕하세요, 저는 Python과 웹 개발에 관심 있는 개발자입니다.
최근에는 Streamlit을 활용한 데이터 애플리케이션 개발에 집중하고 있습니다.
새로운 기술을 배우고 더 나은 솔루션을 만드는 것을 좋아합니다.
""")

st.divider()

# 기술 스택
st.header("🛠️ 기술 스택")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("프로그래밍 언어")
    st.markdown("""
    - Python
    - JavaScript
    - SQL
    """)

with col2:
    st.subheader("라이브러리 & 프레임워크")
    st.markdown("""
    - Streamlit
    - Pandas
    - React
    """)

with col3:
    st.subheader("도구 & 기술")
    st.markdown("""
    - Git
    - Docker
    - AWS
    """)

st.divider()

# 경력 / 프로젝트
st.header("💼 경력 & 프로젝트")

with st.expander("📱 프로젝트 1: 데이터 분석 대시보드"):
    st.write("""
    **설명:** Streamlit과 Pandas를 활용한 실시간 데이터 분석 대시보드
    
    **기술:** Python, Streamlit, Pandas, Plotly
    
    **기간:** 2024.01 ~ 2024.06
    """)

with st.expander("🌐 프로젝트 2: 웹 애플리케이션"):
    st.write("""
    **설명:** React와 Flask를 활용한 전자상거래 플랫폼
    
    **기술:** React, Flask, PostgreSQL, AWS
    
    **기간:** 2023.06 ~ 2023.12
    """)

with st.expander("📊 프로젝트 3: 머신러닝 모델"):
    st.write("""
    **설명:** scikit-learn을 활용한 예측 모델 개발
    
    **기술:** Python, scikit-learn, TensorFlow
    
    **기간:** 2023.01 ~ 2023.05
    """)

st.divider()

# 교육 & 자격증
st.header("🎓 교육 & 자격증")
st.markdown("""
- **학위:** 컴퓨터공학 학사 - OO 대학교 (2020)
- **자격증:** AWS Certified Solutions Architect (2023)
- **자격증:** Python Professional (2022)
""")

st.divider()

# 연락처
st.header("📧 연락처")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("[📬 이메일](mailto:hong@example.com)")

with col2:
    st.markdown("[💼 LinkedIn](https://linkedin.com)")

with col3:
    st.markdown("[🐙 GitHub](https://github.com)")

st.divider()

# 메시지 입력
st.header("💬 인사말")
message = st.text_area("메시지를 남겨주세요:", placeholder="여기에 입력해주세요...")
if st.button("제출"):
    if message:
        st.success("메시지가 전송되었습니다! 감사합니다. 😊")
    else:
        st.warning("메시지를 입력해주세요.")
