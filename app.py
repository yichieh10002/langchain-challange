import streamlit as st
import re
from translator import translate_text
from web_scraper import scrape_webpage

st.set_page_config(
    page_title="Translation App (EN → ZH-TW)", page_icon="🌐", layout="wide"
)

URL_PATTERN = re.compile(r"^https?://")

# 左右欄位
left_col, right_col = st.columns([1, 2])


# 1. L-User Input
with left_col:
    st.title("🌐 Translation App (EN to TW)")
    st.subheader("Run Once")

    url = st.text_input("Input URL")

    col1, col2 = st.columns([1, 1])
    with col1:
        clear = st.button("Clear", type="secondary", help="Clear all inputs")
    with col2:
        run = st.button("Execute", type="primary", help="Click to run the workflow")

    if clear:
        st.rerun()


# R-Workflow
with right_col:
    st.subheader("AI Completion")

    workflow_box = st.container()
    result_box = st.container()

    if run:
        # 先檢查 URL
        if not URL_PATTERN.match(url):
            st.error("❌ URL 格式錯誤！請確認是否以 http:// 或 https:// 開頭")
            st.stop()

        translated = ""  # 避免未定義錯誤

        # 流程記錄
        with workflow_box:
            with st.expander("Step 2. 這裡顯示執行過程中的工作", expanded=True):
                st.write("➤ Start 開始執行囉！")

                # Step 2-1: 網頁爬蟲
                with st.spinner("正在抓取網頁內容..."):
                    try:
                        scraped_text = scrape_webpage(url)
                        st.success("網頁搜尋完成")
                    except Exception as e:
                        st.error(f"❌ 抓取失敗：{e}")
                        st.stop()

                # Step 2-2: LLM 翻譯
                with st.spinner("正在將內容翻譯成繁體中文..."):
                    try:
                        translated = translate_text(scraped_text)
                        st.success("✨ 翻譯完成")
                    except Exception as e:
                        st.error(f"❌ 翻譯失敗：{e}")
                        st.stop()

                st.write("🐳 End 🐳")

        # Show Result

        with result_box:
            st.subheader("Step 3. 最後顯示翻譯的結果")
            st.markdown(
                f"""
                <div style="font-size:16px; line-height:1.6;">
                    {translated}
                </div>
                """,
                unsafe_allow_html=True,
            )
