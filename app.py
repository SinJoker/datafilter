import streamlit as st
import pandas as pd
import plotly.express as px

# 设置为宽屏
st.set_page_config(layout="wide")
# 设置页面标题
st.title("烘烤器 数据过滤与分析")

# 文件上传
uploaded_file = st.file_uploader("上传CSV文件", type=["csv"])

if uploaded_file is not None:
    # 读取CSV文件
    df = pd.read_csv(uploaded_file)

    # 展示原始数据
    st.subheader("原始数据")
    st.dataframe(df)
    rowscount = df.shape[0]

    # 选择x轴和y轴
    st.subheader("选择图表坐标轴")
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("选择X轴", df.columns)
    with col2:
        y_axis = st.selectbox("选择Y轴", df.columns)

    # 使用plotly绘制折线图
    st.subheader("折线图")
    fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
    st.plotly_chart(fig)

    # 数据过滤

    # filter_col = st.selectbox("选择要过滤的列", df.columns)
    filtered_df = df[df[y_axis] >= 100]

    # # 显示过滤后的数据
    # st.write("过滤后的数据（去除值为0的条目）：")
    # st.dataframe(filtered_df)

    # 计算并显示所选列的平均值
    st.subheader("统计与计算结果")
    # avg_col = st.selectbox("选择要计算平均值的列", filtered_df.columns)
    avg_value = filtered_df[y_axis].mean()
    filterrowcount = filtered_df.shape[0]
    st.markdown(
        f"说明：过滤掉数值为0的条目，计算工作时间的平均流量，筛选掉数值小于100的条目，源文件中有{rowscount}行数据，过滤后剩余{filterrowcount}行数据。工作时间占比为：{round(filterrowcount/rowscount*100,2)} %"
    )
    st.title(f"**过滤后{y_axis} 列的平均值：** {avg_value:.2f}")
