import streamlit as st

feature_tuple = (
    "Cartilage signal and morphology",
    "Subarticular bonemarrow abnormality",
    "Subarticular cysts",
    "Bone attrition",
    "Osteophytes",
    "Menisci",
    "Ligaments",
    "Synovitis",
)

# UI starts here
st.title("WORMS GUI", text_alignment="center")

option = st.selectbox(
    "Get more info on a feature",
    feature_tuple,
    index=None,
    placeholder="Select feature ...",
)

st.write("You selected:", option)

# shows ----OR----
st.markdown(
    """
    <div style="display: flex; align-items: center; margin: 20px 0;">
        <div style="flex-grow: 1; height: 1px; background: #ccc;"></div>
        <span style="margin: 0 10px; color: #888; font-weight: bold;">OR</span>
        <div style="flex-grow: 1; height: 1px; background: #ccc;"></div>
    </div>
""",
    unsafe_allow_html=True,
)

st.button(
    "See venn diagrams", type="primary", icon=":material/join_inner:", width="stretch"
)
