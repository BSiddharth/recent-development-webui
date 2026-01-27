import streamlit as st
import os
import json
import matplotlib.pyplot as plt
from marsilea.upset import Upset, UpsetData

feature_tuple = (
    "Cartilage signal and morphology",
    "Subarticular bonemarrow abnormality",
    "Subarticular cysts",
    "Bone attrition",
    "Osteophytes",
    "Menisci",
    "Ligament",
    "Synovitis",
)


def feature_page():
    st.title("WORMS GUI", text_alignment="center")
    st.header("Get more info on a feature")
    selected_feature = st.selectbox(
        "Get more info on a feature",
        feature_tuple,
        index=None,
        placeholder="Select feature ...",
        label_visibility="collapsed",
    )

    if selected_feature:
        for file in os.listdir("./json data/"):
            if "_".join(selected_feature.split()).lower() in file:
                stats = {
                    "Unique GO terms": 0,
                    "Unique Genes found": 0,
                    "Unique Pathways found": 0,
                }
                with open(f"./json data/{file}") as f:
                    json_data = json.load(f)
                    stats["Unique GO terms"] = len(set(json_data.keys()))
                    stats["Unique Genes found"] = len(
                        set(
                            gene_info["Gene_symbol"]
                            for entry in json_data.values()
                            for gene_info in entry["genes"]
                        )
                    )
                    stats["Unique Pathways found"] = len(
                        set(
                            pathway_info["pathway_name"]
                            for entry in json_data.values()
                            for pathway_info in entry["pathways"]
                        )
                    )

                keys = list(stats.keys())
                col_num = 3
                cols = st.columns(col_num)

                for index, key in enumerate(keys):
                    col_index = index % col_num
                    with cols[col_index]:
                        st.metric(label=key, value=stats[key])

                st.json(json_data, expanded=False)


def upset_diagram_page():
    st.title("WORMS GUI", text_alignment="center")

    # Create upset plot
    upset_data = {}
    for file in os.listdir("./json data/"):
        for feature in feature_tuple:
            if "_".join(feature.split()).lower() in file:
                with open(f"./json data/{file}") as f:
                    json_data = json.load(f)
                    upset_data[feature] = set(
                        pathway_info["pathway_name"]
                        for entry in json_data.values()
                        for pathway_info in entry["pathways"]
                    )

    data = UpsetData.from_sets(upset_data.values(), sets_names=upset_data.keys())
    us = Upset(data, add_sets_size=False)
    us.render()
    fig = plt.gcf()
    st.pyplot(fig)

    # Option to filter out common pathways
    st.divider()
    st.header("Filter out common pathways")
    st.subheader("Choose one or more feature(s)")

    col_num = 2
    cols = st.columns(col_num)

    checked = {}

    for i, opt in enumerate(feature_tuple):
        with cols[i % col_num]:
            checked[opt] = st.checkbox(opt)

    checked_options = [opt for opt, is_checked in checked.items() if is_checked]
    if len(checked_options) != 0:
        common_pathways = set.intersection(
            *[upset_data[checked_option] for checked_option in checked_options]
        )
        common_pathways_len = len(common_pathways)
        st.write(f"Total common pathways found: {common_pathways_len}")
        st.write(common_pathways)


page_names_to_funcs = {
    "Feature Info": feature_page,
    "Upset Diagram Page": upset_diagram_page,
}

page_selection = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[page_selection]()
