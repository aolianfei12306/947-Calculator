"""
947 Calculator - A Streamlit-based Calculator Web Application
Supports local deployment and ngrok for public access
"""

import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="947 Calculator",
    page_icon="🧮",
    layout="centered"
)

# Title and description
st.title("🧮 947 Calculator")
st.markdown("一个功能强大的在线计算器 / A powerful online calculator")

# Initialize session state for calculator history
if 'history' not in st.session_state:
    st.session_state.history = []

# Create tabs for different calculator modes
tab1, tab2, tab3 = st.tabs(["基础计算 / Basic", "科学计算 / Scientific", "历史记录 / History"])

with tab1:
    st.subheader("基础计算器 / Basic Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("第一个数 / First Number", value=0.0, format="%.6f")
    
    with col2:
        num2 = st.number_input("第二个数 / Second Number", value=0.0, format="%.6f")
    
    operation = st.selectbox(
        "选择运算 / Select Operation",
        ["加法 / Addition (+)", "减法 / Subtraction (-)", "乘法 / Multiplication (×)", "除法 / Division (÷)"]
    )
    
    if st.button("计算 / Calculate", key="basic_calc"):
        try:
            result = None
            op_symbol = ""
            
            if "加法" in operation or "Addition" in operation:
                result = num1 + num2
                op_symbol = "+"
            elif "减法" in operation or "Subtraction" in operation:
                result = num1 - num2
                op_symbol = "-"
            elif "乘法" in operation or "Multiplication" in operation:
                result = num1 * num2
                op_symbol = "×"
            elif "除法" in operation or "Division" in operation:
                if num2 == 0:
                    st.error("错误：除数不能为0 / Error: Division by zero")
                    result = None
                else:
                    result = num1 / num2
                    op_symbol = "÷"
            
            if result is not None:
                st.success(f"结果 / Result: {num1} {op_symbol} {num2} = {result}")
                st.session_state.history.append(f"{num1} {op_symbol} {num2} = {result}")
        except Exception as e:
            st.error(f"计算错误 / Error: {str(e)}")

with tab2:
    st.subheader("科学计算器 / Scientific Calculator")
    
    calc_type = st.radio(
        "选择函数 / Select Function",
        ["平方根 / Square Root", "平方 / Square", "立方 / Cube", 
         "对数 / Logarithm", "指数 / Exponential", "三角函数 / Trigonometry"]
    )
    
    num = st.number_input("输入数值 / Input Number", value=0.0, format="%.6f", key="sci_num")
    
    if calc_type in ["平方根 / Square Root"]:
        if st.button("计算 / Calculate", key="sci_calc1"):
            if num < 0:
                st.error("错误：负数没有实数平方根 / Error: Negative numbers don't have real square roots")
            else:
                result = math.sqrt(num)
                st.success(f"结果 / Result: √{num} = {result}")
                st.session_state.history.append(f"√{num} = {result}")
    
    elif calc_type in ["平方 / Square"]:
        if st.button("计算 / Calculate", key="sci_calc2"):
            result = num ** 2
            st.success(f"结果 / Result: {num}² = {result}")
            st.session_state.history.append(f"{num}² = {result}")
    
    elif calc_type in ["立方 / Cube"]:
        if st.button("计算 / Calculate", key="sci_calc3"):
            result = num ** 3
            st.success(f"结果 / Result: {num}³ = {result}")
            st.session_state.history.append(f"{num}³ = {result}")
    
    elif calc_type in ["对数 / Logarithm"]:
        log_base = st.selectbox("选择底数 / Select Base", ["自然对数 (e) / Natural (e)", "常用对数 (10) / Common (10)", "二进制 (2) / Binary (2)"])
        if st.button("计算 / Calculate", key="sci_calc4"):
            if num <= 0:
                st.error("错误：对数的真数必须大于0 / Error: Logarithm argument must be positive")
            else:
                if "自然" in log_base or "Natural" in log_base:
                    result = math.log(num)
                    st.success(f"结果 / Result: ln({num}) = {result}")
                    st.session_state.history.append(f"ln({num}) = {result}")
                elif "常用" in log_base or "Common" in log_base:
                    result = math.log10(num)
                    st.success(f"结果 / Result: log₁₀({num}) = {result}")
                    st.session_state.history.append(f"log₁₀({num}) = {result}")
                else:
                    result = math.log2(num)
                    st.success(f"结果 / Result: log₂({num}) = {result}")
                    st.session_state.history.append(f"log₂({num}) = {result}")
    
    elif calc_type in ["指数 / Exponential"]:
        if st.button("计算 / Calculate", key="sci_calc5"):
            result = math.exp(num)
            st.success(f"结果 / Result: e^{num} = {result}")
            st.session_state.history.append(f"e^{num} = {result}")
    
    elif calc_type in ["三角函数 / Trigonometry"]:
        trig_func = st.selectbox("选择函数 / Select Function", ["sin", "cos", "tan"])
        angle_unit = st.radio("角度单位 / Angle Unit", ["度 / Degrees", "弧度 / Radians"])
        
        if st.button("计算 / Calculate", key="sci_calc6"):
            angle = num
            if "度" in angle_unit or "Degrees" in angle_unit:
                angle = math.radians(num)
            
            if trig_func == "sin":
                result = math.sin(angle)
            elif trig_func == "cos":
                result = math.cos(angle)
            else:
                result = math.tan(angle)
            
            st.success(f"结果 / Result: {trig_func}({num}{'°' if '度' in angle_unit or 'Degrees' in angle_unit else ' rad'}) = {result}")
            st.session_state.history.append(f"{trig_func}({num}) = {result}")

with tab3:
    st.subheader("计算历史 / Calculation History")
    
    if st.session_state.history:
        st.write("最近的计算记录 / Recent Calculations:")
        for i, record in enumerate(reversed(st.session_state.history[-10:]), 1):
            st.text(f"{i}. {record}")
        
        if st.button("清空历史 / Clear History"):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("暂无计算记录 / No calculation history yet")

# Footer
st.markdown("---")
st.markdown("""
### 使用说明 / Instructions
- **本地部署 / Local Deployment**: 运行 `streamlit run app.py`
- **公网访问 / Public Access**: 使用 ngrok 或运行 `python run.py --ngrok`
""")
