# app.py
import streamlit as st
import random
import time

# 页面配置
st.set_page_config(page_title="黑客松破冰匹配器", page_icon="🧊")
st.title("🧊 现场破冰匹配器")
st.markdown("输入你的技能和兴趣，系统将为你随机匹配一位交流伙伴！")

# 模拟数据库（实际项目中可以使用简单的列表或数据库）
if 'users' not in st.session_state:
    st.session_state.users = []

# 侧边栏：用户注册
with st.sidebar:
    st.header("我是新来的")
    name = st.text_input("你的名字")
    skills = st.text_input("你的技能 (用逗号分隔)", placeholder="Python, Design, Marketing")
    interests = st.text_input("你的兴趣 (用逗号分隔)", placeholder="AI, Gaming, Coffee")
    
    if st.button("加入匹配池"):
        if name and skills:
            new_user = {
                "name": name,
                "skills": [s.strip() for s in skills.split(",")],
                "interests": [i.strip() for i in interests.split(",")]
            }
            st.session_state.users.append(new_user)
            st.success(f"欢迎 {name}！已加入匹配池。")
        else:
            st.error("请填写名字和技能！")

# 主界面：开始匹配
st.divider()
st.subheader("寻找我的伙伴")

if st.button("🎲 开始随机匹配", type="primary"):
    if len(st.session_state.users) < 2:
        st.warning("当前人数不足 2 人，无法匹配。快去拉人注册！")
    else:
        # 简单的随机匹配逻辑
        # 实际可以优化为：优先匹配有共同兴趣的人
        me = random.choice(st.session_state.users)
        
        # 排除自己
        others = [u for u in st.session_state.users if u['name'] != me['name']]
        partner = random.choice(others)
        
        # 计算共同点 (可选的高级功能)
        common_skills = set(me['skills']) & set(partner['skills'])
        common_interests = set(me['interests']) & set(partner['interests'])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"**你:** {me['name']}")
            st.caption(f"技能: {', '.join(me['skills'])}")
            
        with col2:
            st.success(f"**你的伙伴:** {partner['name']}")
            st.caption(f"技能: {', '.join(partner['skills'])}")
            
        if common_interests:
            st.balloons()
            st.write(f"🎉 你们有共同兴趣: **{', '.join(common_interests)}**，以此为话题开始聊天吧！")
        else:
            st.write("💡 话题建议：聊聊你们对这次黑客松的期待？")

# 显示当前在线人数
st.caption(f"当前匹配池人数: {len(st.session_state.users)}")