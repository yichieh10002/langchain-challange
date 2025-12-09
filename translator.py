import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key, temperature=0)

translation_prompt = PromptTemplate(
    input_variables=["content"],
    template="""
請將以下英文內容翻譯成「繁體中文（ZH-TW）」。
請保持段落格式，不要自行增加內容。

英文內容如下：
---
{content}
---
""",
)

# 建立 LCEL chain：prompt → llm → parser
translation_chain = translation_prompt | llm | StrOutputParser()


# 執行翻譯
def translate_text(text: str) -> str:
    return translation_chain.invoke({"content": text})
