import streamlit as st


def feature_page():
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


def venn_diagram_page():
    pass


page_names_to_funcs = {
    "Feature Info": feature_page,
    "Venn Diagram Page": venn_diagram_page,
}

page_selection = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[page_selection]()
