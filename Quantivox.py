############################################################
# IMPORT LIBRARIES
############################################################

import streamlit as st

############################################################
# PAGE CONFIG
############################################################

st.set_page_config(
    page_title="QUANTIVOX AI FINANCIAL SENTIMENT DASHBOARD",
    layout="wide"
)

############################################################
# OTHER LIBRARIES
############################################################

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime
import seaborn as sns

############################################################
# BACKGROUND / CANVAS
############################################################

st.markdown("""

<style>

/* MAIN BACKGROUND */

.stApp {

    background-color: black;

}

/* REMOVE WHITE HEADER */

[data-testid="stHeader"] {

    background: black;

}

/* REMOVE TOP WHITE LINE */

[data-testid="stDecoration"] {

    background: transparent;

}

/* REMOVE EXTRA SPACE */

.block-container {

    padding-top: 1rem;

    padding-bottom: 0rem;

    padding-left: 1rem;

    padding-right: 1rem;

}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background-color: #0d0d0d;

}

/* TEXT COLOR */

html,
body,
[class*="css"] {

    color: white;

}

</style>

""", unsafe_allow_html=True)

############################################################
# HEADER BOX
############################################################

from datetime import datetime

current_time = datetime.now().strftime("%d %b %Y | %I:%M %p")

header_html = f"""

<div style="
border:1px solid #1f3b5c;
border-radius:6px;
background:linear-gradient(to right, #06101c, #081524, #06101c);
padding:8px 18px;
height:52px;
margin-top:28px;
display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:8px;
box-shadow:0px 0px 10px #06101c;
">

<!-- LEFT -->

<div>

<p style="
color:#d0d0d0;
font-size:10px;
margin:0;
">
Real-Time Market Sentiment
</p>

</div>

<!-- CENTER -->

<div>

<h2 style="
color:white;
font-size:16px;
margin:0;
letter-spacing:1px;
white-space:nowrap;
">
QUANTIVOX AI FINANCIAL SENTIMENT
</h2>

</div>

<!-- RIGHT -->

<div style="
text-align:right;
">

<p style="
color:#d0d0d0;
font-size:10px;
margin:0;
">
Last Refresh : {current_time}
</p>

</div>

</div>

"""

st.markdown(header_html, unsafe_allow_html=True)





############################################################
# MARKET SENTIMENT + QSI
############################################################

# SAMPLE QSI VALUE
# Replace with your calculated QSI later

qsi = 52

# LAYOUT

col_scale, col_qsi = st.columns([4,1])

############################################################
# MARKET SENTIMENT SCALE
############################################################

with col_scale:

    market_html = f"""

    <div style="
    border:1px solid #1f3b5c;
    border-radius:6px;
    background-color:#06101c;
    padding:10px 15px;
    height:70px;
    box-shadow:0px 0px 8px #06101c;
    ">

<!-- TITLE -->

<h3 style="
color:white;
font-size:13px;
margin:0;
margin-bottom:8px;
margin-top:-18px
">
Market Sentiment
</h3>

<!-- SCALE -->

<div style="
width:100%;
height:8px;
background:linear-gradient(to right, red, orange, yellow, limegreen, green);
border-radius:20px;
position:relative;
margin-top:-15px;
">

<!-- POINTER -->

<div style="
position:absolute;
left:{qsi}%;
top:-5px;
width:10px;
height:18px;
background-color:white;
border-radius:4px;
box-shadow:0px 0px 8px white;
">
</div>

</div>

<!-- LABELS -->

<div style="
display:flex;
justify-content:space-between;
margin-top:5px;
font-size:12px;
font-weight:bold;
">

<span style="color:red;">
Strong Bearish
</span>

<span style="color:yellow;">
Neutral
</span>

<span style="color:lime;">
Strong Bullish
</span>

</div>

</div>

    """

    st.markdown(market_html, unsafe_allow_html=True)

############################################################
# DYNAMIC QSI STATUS
############################################################

############################################################
# DYNAMIC QSI STATUS
############################################################

if qsi >= 75:

    qsi_label = "Strong Bullish"
    qsi_color = "#00ff00"
    qsi_emoji = "😄"

elif qsi >= 55:

    qsi_label = "Bullish"
    qsi_color = "#7fff00"
    qsi_emoji = "🙂"

elif qsi >= 45:

    qsi_label = "Neutral"
    qsi_color = "#ffff00"
    qsi_emoji = "😐"

elif qsi >= 25:

    qsi_label = "Bearish"
    qsi_color = "#ff9900"
    qsi_emoji = "😟"

else:

    qsi_label = "Strong Bearish"
    qsi_color = "#ff0000"
    qsi_emoji = "😡"


############################################################
# QSI CARD
############################################################

with col_qsi:

    qsi_html = f"""

    <div style="
    border:1px solid #1f3b5c;
    border-radius:6px;
    background-color:#06101c;
    padding:10px;
    height:70px;
    text-align:center;
    box-shadow:0px 0px 8px #06101c;
    ">

    <h3 style="
    color:white;
    font-size:13px;
    margin:0;
    margin-bottom:8px;
    margin-top:-18px
    ">
    Quantivox Sentiment Index
    </h3>

    <h1 style="
    color:{qsi_color};
    font-size:18px;
    margin:0;
    margin-bottom:8px;
    margin-top:-40px
    ">
    {qsi}/100
    </h1>

    <div style="
     display:flex;
     justify-content:center;
     align-items:center;
     gap:6px;
     margin-top:-25px
     ">

     <p style="
     color:{qsi_color};
     font-size:12px;
     margin:0;
     font-weight:bold;
     ">
     {qsi_label}
     </p>


    </div>

    """

    st.markdown(

        qsi_html,

        unsafe_allow_html=True

    )

############################################################
# KPI CARD FUNCTION
############################################################

def kpi_card(title, value, color):

    return f"""

    <div style="
    border:1px solid #1f3b5c;
    border-radius:6px;
    background-color:#06101c;
    padding:5px;
    padding-top:40px;
    height:40px;
    margin-top:10px;
    box-shadow:0px 0px 8px #06101c;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    ">

<!-- KPI TITLE -->

<h4 style="
color:white;
font-size:12px;
margin:0;
margin-bottom:-60px;
margin-top:30px;
text-align:center;
">

{title}

</h4>

<!-- KPI VALUE -->

<h2 style="
color:{color};
font-size:18px;
margin:0;
margin-top:0px;
margin-bottom:20px;
text-align:center;
">

{value}

</h2>

</div>

    """



############################################################
# LOAD DATASET
############################################################

df = pd.read_excel(
    "final_sentiment_analysis.xlsx"
)


############################################################
# FILTERS
############################################################
############################################################
# INDUSTRY FILTER
############################################################

industry_filter = st.sidebar.selectbox(

    "Select Industry",

    ["All"] + sorted(
        df['industry'].dropna().unique()
    )

)

############################################################
# FILTER DATA FOR TICKER
############################################################

ticker_df = df.copy()

if industry_filter != "All":

    ticker_df = ticker_df[

        ticker_df['industry'] == industry_filter

    ]

############################################################
# TICKER FILTER
############################################################

ticker_filter = st.sidebar.selectbox(

    "Select Ticker",

    ["All"] + sorted(
        ticker_df['ticker'].dropna().unique()
    )

)

############################################################
# FILTER DATA FOR SOURCE
############################################################

source_df = ticker_df.copy()

if ticker_filter != "All":

    source_df = source_df[

        source_df['ticker'] == ticker_filter

    ]

############################################################
# SOURCE FILTER
############################################################

source_filter = st.sidebar.selectbox(

    "Select Source",

    ["All"] + sorted(
        source_df['source'].dropna().unique()
    )

)

############################################################
# FINAL FILTERED DATA
############################################################

filtered_df = source_df.copy()

if source_filter != "All":

    filtered_df = filtered_df[

        filtered_df['source'] == source_filter

    ]




############################################################
# KPI VALUES
############################################################

avg_sentiment = round(

    filtered_df['vader_score'].mean(),

    2

)

momentum = round(

    filtered_df['vader_score'].diff().mean(),

    2

)

volatility = round(

    filtered_df['vader_score'].std(),

    2

)

news_volume = len(filtered_df)



if not filtered_df.empty:

    top_bullish = filtered_df.groupby(
        'ticker'
    )['vader_score'].mean().idxmax()

else:

    top_bullish = "N/A"



if not filtered_df.empty:

    most_impact = filtered_df.groupby(
        'ticker'
    )['vader_score'].mean().idxmin()

else:

    most_impact = "N/A"



ai_confidence = round(

    filtered_df['bert_score'].mean() * 100,

    2

)

qsi = round(

    (avg_sentiment + 1) * 50,

    0

)



############################################################
# KPI ROW
############################################################

col1,col2,col3,col4,col5,col6,col7 = st.columns(7)

with col1:
    st.markdown(
        kpi_card("Avg Sentiment", avg_sentiment, "lime"),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        kpi_card("Momentum", momentum, "lime"),
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        kpi_card("Volatility", volatility, "red"),
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        kpi_card("News Volume", news_volume, "white"),
        unsafe_allow_html=True
    )

with col5:
    st.markdown(
        kpi_card("Top Bullish", top_bullish, "lime"),
        unsafe_allow_html=True
    )

with col6:
    st.markdown(
        kpi_card("Most Impact", most_impact, "red"),
        unsafe_allow_html=True
    )

with col7:
    st.markdown(
        kpi_card("AI Confidence", ai_confidence, "yellow"),
        unsafe_allow_html=True
    )


############################################################
############################################################



############################################################
# ANALYTICS DASHBOARD
# 8 CHARTS | 2 ROWS | 4 COLUMNS
############################################################


############################################################
# Space 1
############################################################

st.markdown(

    "<div style='height:5px;'></div>",

    unsafe_allow_html=True

)


############################################################
# ROW 1
############################################################

col1, col2, col3, col4 = st.columns(4)

############################################################
# 1 — DAILY SENTIMENT TREND
############################################################

daily_trend = filtered_df.groupby(

    'date'

)['vader_score'].mean().reset_index()

############################################################
# LINE CHART
############################################################

fig1 = px.line(

    daily_trend,

    x='date',

    y='vader_score',

    template='plotly_dark',

    title="Daily Sentiment Trend"

)

############################################################
# LINE COLOR
############################################################

fig1.update_traces(

    line=dict(
        color="#7c4dff",
        width=2
    )

)

############################################################
# CHART STYLING
############################################################

fig1.update_layout(

    height=170,

    paper_bgcolor="#06101c",

    plot_bgcolor="#06101c",

    font=dict(
        color="white",
        size=9
    ),

    title=dict(

       text="Daily Sentiment Trend",

       font=dict(
           size=12,
           color="#2c2f48"
       ),

       x=0.02

    ),


    margin=dict(
        l=5,
        r=5,
        t=25,
        b=0
    )

)

############################################################
# GRID COLOR
############################################################

fig1.update_xaxes(

    gridcolor="#1f3b5c"

)

fig1.update_yaxes(

    gridcolor="#1f3b5c"

)

############################################################
# LINE COLOR
############################################################

fig1.update_traces(

    line=dict(
        color="#00ff00",
        width=2
    )

)

############################################################
# SHOW CHART
############################################################

with col1:

    st.plotly_chart(

        fig1,

        use_container_width=True

    )




############################################################
# 2 — SECTOR COMPARISON
############################################################

sector_df = filtered_df.groupby(

    'industry'

)['vader_score'].mean().reset_index()

############################################################
# TAKE ONLY FIRST WORD
############################################################

sector_df['short_industry'] = sector_df['industry'].str.split().str[0]

############################################################
# COLOR BASED ON SENTIMENT
############################################################

sector_df['color'] = sector_df['vader_score'].apply(

    lambda x:

    "#00ff00" if x >= 0.30 else     # Extreme Greed
    "#7fff00" if x >= 0.10 else     # Greed
    "#ffff00" if x >= -0.10 else    # Neutral
    "#ff9900" if x >= -0.30 else    # Fear
    "#ff0000"                       # Extreme Fear

)

############################################################
# HORIZONTAL BAR CHART
############################################################


fig2 = px.bar(

    sector_df,

    y='short_industry',

    x='vader_score',

    orientation='h',

    template='plotly_dark',

    title="Sector Comparison",

    color='color',

    color_discrete_map="identity"

)

############################################################
# SHOW VALUES ON BARS
############################################################

fig2.update_traces(

    text=sector_df['vader_score'].round(2),

    textposition='outside'

)


############################################################
# CHART STYLING
############################################################

fig2.update_layout(

    height=170,

    paper_bgcolor="#06101c",

    plot_bgcolor="#06101c",

    font=dict(
        color="white",
        size=9
    ),

    title=dict(

        text="Sector Comparison",

        font=dict(
            size=12,
            color="#2c2f48"
        ),

        x=0.02

    ),

    margin=dict(
        l=5,
        r=5,
        t=25,
        b=0
    ),

    yaxis_title="",

    xaxis_title="",

    showlegend=False

)

############################################################
# GRID COLOR
############################################################

fig2.update_xaxes(

    gridcolor="#1f3b5c"

)

fig2.update_yaxes(

    gridcolor="#1f3b5c"

)


############################################################
# SHOW CHART WITH BORDER
############################################################

with col2:

    st.plotly_chart(

        fig2,

        use_container_width=True

    )





############################################################
# 3 — SENTIMENT DISTRIBUTION
# VADER vs BERT DISTRIBUTION
############################################################

############################################################
# CREATE LONG FORMAT DATA
############################################################

distribution_df = pd.DataFrame({

    'score': pd.concat([

        filtered_df['vader_score'],
        filtered_df['bert_score']

    ], ignore_index=True),

    'model': (

        ['VADER'] * len(filtered_df) +

        ['BERT'] * len(filtered_df)

    )

})

############################################################
# HISTOGRAM
############################################################

fig3 = px.histogram(

    distribution_df,

    x='score',

    color='model',

    nbins=30,

    barmode='overlay',

    opacity=0.7,

    template='plotly_dark',

    title="Sentiment Distribution"

)

############################################################
# MARKET SENTIMENT COLORS
############################################################

fig3.update_traces(

    marker_line_width=0

)

############################################################
# SET COLORS
############################################################

fig3.for_each_trace(

    lambda t: t.update(

        marker_color=

        "#00ff00" if t.name == "VADER"

        else "#ff9900"

    )

)

############################################################
# CHART STYLING
############################################################

fig3.update_layout(

    height=170,

    paper_bgcolor="#06101c",

    plot_bgcolor="#06101c",

    font=dict(
        color="white",
        size=9
    ),

	title=dict(

        text="Sentiment Distribution",

        font=dict(
            size=12,
            color="#2c2f48"
        ),

        x=0.02

	    ),

    margin=dict(
        l=5,
        r=5,
        t=25,
        b=0
    ),

    legend=dict(

    orientation="v",

    yanchor="top",

    y=1,

    xanchor="left",

    x=1.02,

    bgcolor="#06101c",

    bordercolor="#1f3b5c",

    borderwidth=1,

    font=dict(
        color="white",
        size=8
    )

)

)

############################################################
# GRID COLOR
############################################################

fig3.update_xaxes(

    gridcolor="#1f3b5c"

)

fig3.update_yaxes(

    gridcolor="#1f3b5c"

)

############################################################
# SHOW CHART
############################################################

with col3:

    st.plotly_chart(

        fig3,

        use_container_width=True

    )



############################################################
# VADER vs BERT
############################################################

fig4 = px.scatter(

    filtered_df,

    x='vader_score',

    y='bert_score',

    color='vader_sentiment',

    template='plotly_dark',

    title="VADER vs BERT",

    color_discrete_map={

        'Positive':'#00ff00',   # Extreme Greed
        'Negative':'#ff0000',   # Extreme Fear
        'Neutral':'#ffff00'     # Neutral

    }

)

############################################################
# CHART STYLING
############################################################

fig4.update_layout(

    height=170,

    paper_bgcolor="#06101c",

    plot_bgcolor="#06101c",

    font=dict(
        color="white",
        size=9
    ),

    title=dict(

        text="VADER vs BERT",

        font=dict(
            size=12,
            color="#2c2f48"
        ),

        x=0.02

    ),

    margin=dict(
        l=5,
        r=5,
        t=25,
        b=0
    ),

    legend=dict(

    orientation="v",

    yanchor="top",

    y=1,

    xanchor="left",

    x=1.02,

    bgcolor="#06101c",

    bordercolor="#1f3b5c",

    borderwidth=1,

    font=dict(
        color="white",
        size=8
    )

)

)

############################################################
# SCATTER DOT STYLE
############################################################

fig4.update_traces(

    marker=dict(

        size=5,

        line=dict(
            width=0.3,
            color="white"
        ),

        opacity=0.8

    )

)

############################################################
# AXIS STYLE
############################################################

fig4.update_xaxes(

    gridcolor="#1f3b5c",

    zerolinecolor="white",

    tickfont=dict(size=8)

)

fig4.update_yaxes(

    gridcolor="#1f3b5c",

    zerolinecolor="white",

    tickfont=dict(size=8)

)

############################################################
# SHOW CHART
############################################################

with col4:

    st.plotly_chart(

        fig4,

        use_container_width=True,


    )

############################################################
# space 2
############################################################


st.markdown(

    "<div style='height:2px;'></div>",

    unsafe_allow_html=True

)


############################################################
# ROW 2
############################################################

col5, col6, col7, col8 = st.columns(4)




############################################################
# 5 — MARKET SESSION ANALYSIS
############################################################

session_df = filtered_df.groupby(

    'market_session'

)['vader_score'].mean().reset_index()

############################################################
# CHANGE SESSION ORDER
############################################################

session_order = [

    'Pre-Market',

    'Market Hours',

    'After Market'

]

session_df['market_session'] = pd.Categorical(

    session_df['market_session'],

    categories=session_order,

    ordered=True

)

session_df = session_df.sort_values(

    'market_session'

)

############################################################
# MARKET SENTIMENT COLORS
############################################################

session_df['color'] = session_df['vader_score'].apply(

    lambda x:

    "#00ff00" if x >= 0.30 else
    "#7fff00" if x >= 0.10 else
    "#ffff00" if x >= -0.10 else
    "#ff9900" if x >= -0.30 else
    "#ff0000"

)

############################################################
# BAR CHART
############################################################

fig5 = px.bar(

    session_df,

    x='market_session',

    y='vader_score',

    color='color',

    template='plotly_dark',

    title="Market Session Analysis",

    color_discrete_map="identity"

)

############################################################
# SHOW VALUES
############################################################

fig5.update_traces(

    text=session_df['vader_score'].round(2),

    textposition='outside'

)

############################################################
# CHART STYLING
############################################################

fig5.update_layout(

    height=170,

    paper_bgcolor="#06101c",

    plot_bgcolor="#06101c",

    font=dict(
        color="white",
        size=9
    ),

    title=dict(

        text="Market Session Analysis",

        font=dict(
            size=12,
            color="#2c2f48"
        ),

        x=0.02

    ),

    margin=dict(
        l=5,
        r=5,
        t=25,
        b=0
    ),

    xaxis_title="",

    yaxis_title="",

    showlegend=False

)

############################################################
# GRID COLOR
############################################################

fig5.update_xaxes(

    gridcolor="#1f3b5c"

)

fig5.update_yaxes(

    gridcolor="#1f3b5c"

)

############################################################
# SHOW CHART
############################################################

with col5:

    st.plotly_chart(

        fig5,

        use_container_width=True

    )



############################################################
# 6 — HOURLY NEWS ACTIVITY
############################################################

hourly_df = filtered_df.groupby(

    'hour'

).size().reset_index(name='count')

############################################################
# LINE CHART
############################################################

fig6 = px.line(

    hourly_df,

    x='hour',

    y='count',

    template='plotly_dark',

    title="Hourly News Activity"

)

############################################################
# MARKET SENTIMENT LINE COLOR
############################################################

fig6.update_traces(

    line=dict(
        color="#00ff00",
        width=2
    ),

    mode='lines+markers',

    marker=dict(
        size=5,
        color="#ffff00",
        line=dict(
            color="#00ff00",
            width=1
        )
    )

)

############################################################
# CHART STYLING
############################################################

fig6.update_layout(

    height=170,

    paper_bgcolor="#06101c",

    plot_bgcolor="#06101c",

    font=dict(
        color="white",
        size=9
    ),

    title=dict(

        text="Hourly News Activity",

        font=dict(
            size=12,
            color="#2c2f48"
        ),

        x=0.02

    ),

    margin=dict(
        l=5,
        r=5,
        t=25,
        b=0
    ),

    xaxis_title="",

    yaxis_title=""

)

############################################################
# GRID COLOR
############################################################

fig6.update_xaxes(

    gridcolor="#1f3b5c",

    tickfont=dict(size=9)

)

fig6.update_yaxes(

    gridcolor="#1f3b5c",

    tickfont=dict(size=9)

)

############################################################
# SHOW CHART
############################################################

with col6:

    st.plotly_chart(

        fig6,

        use_container_width=True

    )

############################################################
# 7 — WORD CLOUD
############################################################

text = " ".join(

    filtered_df['headline'].astype(str)

)

wordcloud = WordCloud(

    width=500,

    height=170,

    background_color='#06101c',

    colormap='viridis',

    contour_width=1,

    contour_color='#1f3b5c'

).generate(text)

############################################################
# FIGURE
############################################################

fig_wc, ax = plt.subplots(

    figsize=(5,2.2)

)

############################################################
# SHOW WORD CLOUD
############################################################

ax.imshow(

    wordcloud,

    interpolation='bilinear'

)

############################################################
# REMOVE AXIS
############################################################

ax.axis("off")

############################################################
# BACKGROUND
############################################################

fig_wc.patch.set_facecolor('#06101c')

ax.set_facecolor('#06101c')

############################################################
# REMOVE SPACE
############################################################

plt.tight_layout(

    pad=0

)

############################################################
# TITLE
############################################################

ax.set_title(

    "Word Cloud",

    color="#2c2f48",

    fontsize=12,

    loc='left',

    pad=2

)

############################################################
# SHOW CHART
############################################################

with col7:

    st.pyplot(

        fig_wc,

        use_container_width=True

    )

############################################################
# 8 — SECTOR SENTIMENT HEATMAP
############################################################

heatmap_df = filtered_df.pivot_table(

    values='vader_score',

    index='industry',

    columns='market_session',

    aggfunc='mean'

)

############################################################
# TAKE ONLY FIRST WORD
############################################################

heatmap_df.index = heatmap_df.index.str.split().str[0]


############################################################
# CHANGE COLUMN ORDER
############################################################

heatmap_df = heatmap_df[

    ['Pre-Market', 'Market Hours', 'After Market']

]


############################################################
# HEATMAP
############################################################


fig8 = px.imshow(

    heatmap_df,

    template='plotly_dark',

    title="Sector Sentiment Heatmap",

    aspect="auto",

    color_continuous_scale=[

        [0.0, "#ff0000"],
        [0.25, "#ff9900"],
        [0.50, "#ffff00"],
        [0.75, "#7fff00"],
        [1.0, "#00ff00"]

    ]

)

############################################################
# SHOW VALUES
############################################################

fig8.update_traces(

    text=heatmap_df.round(2),

    texttemplate="%{text}"

)

############################################################
# CHART STYLING
############################################################

fig8.update_layout(

    height=170,

    paper_bgcolor="#06101c",

    plot_bgcolor="#06101c",

    font=dict(
        color="white",
        size=9
    ),

    title=dict(

        text="Sector Sentiment Heatmap",

        font=dict(
            size=12,
            color="#2c2f48"
        ),

        x=0.02

    ),

    margin=dict(
        l=5,
        r=5,
        t=25,
        b=0
    ),

    coloraxis_colorbar=dict(

        title="",

        tickfont=dict(
            color="white",
            size=8
        )

    )

)

############################################################
# AXIS STYLE
############################################################

fig8.update_xaxes(

    tickfont=dict(size=9)

)

fig8.update_yaxes(

    tickfont=dict(size=9)

)

############################################################
# SHOW CHART
############################################################

with col8:

    st.plotly_chart(

        fig8,

        use_container_width=True

    )