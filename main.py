from marsilea.upset import UpsetData
from marsilea.upset import Upset
import streamlit as st
import os
import json

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

    selected_feature = st.selectbox(
        "Get more info on a feature",
        feature_tuple,
        index=None,
        placeholder="Select feature ...",
    )

    if selected_feature:
        for file in os.listdir("./json data/"):
            if '_'.join(selected_feature.split()).lower() in file:
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
                cols = st.columns(3)

                for index, key in enumerate(keys):
                    col_index = index % 3
                    with cols[col_index]:
                        st.metric(label=key, value=stats[key])

                st.json(json_data, expanded=False)


def venn_diagram_page():
    st.title("WORMS GUI", text_alignment="center")

    upset_data = {}
    for file in os.listdir("./json data/"):
        for feature in feature_tuple:
            if '_'.join(feature.split()).lower() in file:
                with open(f"./json data/{file}") as f:
                    json_data = json.load(f)
                    upset_data[feature] = set(
                        pathway_info["pathway_name"]
                        for entry in json_data.values()
                        for pathway_info in entry["pathways"]
                    )

    data = UpsetData.from_sets(upset_data.values(),sets_names=upset_data.keys())
    us = Upset(data,add_sets_size=False)
    st.pyplot(us.render())

    

page_names_to_funcs = {
    "Feature Info": feature_page,
    "Venn Diagram Page": venn_diagram_page,
}

page_selection = st.sidebar.selectbox(
    "Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[page_selection]()
