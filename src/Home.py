import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="CLaim Correspondent")


#Contact
with st.sidebar.expander("📬 Contact"):




    st.write("**Twitter:** [@duh.vinci85]")
    st.write("**Mail** : hassanahmad6085@gmail.com")
    st.write("**Created by Hassan**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Claim Correpondent \n Building Tomorrow Claim by Claim</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ **NOT SURE IF YOU SHOULD PUT IN A CLAIM FOR EXTENSION OF TIME??
                CLAIM CORRESPONDENT IS HERE TO HELP YOU**🧠</h2>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 Our Services")
st.write("""
- **Claim Correspondent**: Generating Notices and Claims on data set converted into vectorstore embedded with GPT 4. The data set can be any version of FIDIC, every version, every book.
""")
st.markdown("---")
st.write("""
- **FIDIC 1987 Reprinted in 1992**: Generating Notices and Claims based on FIDIC 1992 quoting accurate clauses and following the industry standard pattern of generating notices and claims """)
st.markdown("---")
st.write("""
- **FIDIC 2017 Red Book**: Generating Notices and Claims on clauses based on FIDIC 2017 Red Book quoting accurate clauses and following the industry standard pattern of generating notices and claims """)
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**Claim Correspondent is under regular development. Feel free to give you suggestions**
""", unsafe_allow_html=True)





