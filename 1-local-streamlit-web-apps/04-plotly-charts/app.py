import pandas as pd
import streamlit as st
import plotly.graph_objects as go

#Título
st.title("Hierarchical Data Charts")

#load csv
df = pd.read_csv("1-local-streamlit-web-apps/04-plotly-charts/data/employees.csv", header=0).convert_dtypes()
#st.dataframe(df) #show Dataframe

labels = df[df.columns[0]]
parents = df[df.columns[1]]

data = go.Treemap(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgray"
)
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)


data = go.Icicle(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgrey")
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)


data = go.Sunburst(
    ids=labels,
    labels=labels,
    parents=parents,
    insidetextorientation='horizontal')
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)


data = go.Sankey(
    node=dict(label=labels),
    link=dict(
        source=[list(labels).index(x) for x in labels],
        target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
        label=labels,
        value=list(range(1, len(labels)))))
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)
