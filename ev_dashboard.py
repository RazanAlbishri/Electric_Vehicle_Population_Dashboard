import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="EV Dashboard", page_icon=":material/electric_car:", layout="wide")

TESLA_RED = "#C8102E"
BLUE = "#24507A"
LIGHT_BLUE = "#7FA1C3"
GRAY = "#B5BDC8"


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap');
html, body, .stApp, button, input, label { font-family: 'IBM Plex Sans Arabic', sans-serif; }
.block-container { direction: rtl; text-align: right; padding-top: 2rem; }
[data-testid="stSlider"] { direction: ltr; }
[data-testid="stMetricValue"] { color: #16202C; font-weight: 700; }
#MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

    df = df.drop_duplicates()
    df = df.dropna(subset=["Make", "Model", "Model Year", "City", "County"])

    df["Make"] = df["Make"].str.title().replace({"Bmw": "BMW", "Kia": "KIA"})
    df["Model"] = df["Model"].str.title()

    df["Electric Range"] = df["Electric Range"].replace(0, None)

    df["Electric Vehicle Type"] = df["Electric Vehicle Type"].replace({
        "Battery Electric Vehicle (BEV)": "كهربائية بالكامل",
        "Plug-in Hybrid Electric Vehicle (PHEV)": "هجينة قابلة للشحن",
    })

    df = df[df["Model Year"] < df["Model Year"].max()]

    df["Group"] = df["Make"].apply(lambda x: "Tesla" if x == "Tesla" else "باقي الشركات")
    return df


def style_chart(fig, height=380):
    """تنسيق موحد لكل الرسوم"""
    fig.update_layout(
        height=height,
        font_family="IBM Plex Sans Arabic",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=10, b=10),
        legend_title_text="",
    )
    return fig


df = load_data()


st.title(":material/electric_car: السيارات الكهربائية في ولاية واشنطن")
st.caption("تحليل السيارات الكهربائية المسجلة حسب الشركة والموديل والمدينة، مع تركيز على تسلا")


with st.container(border=True):
    st.markdown("##### :material/tune: الفلاتر")
    f1, f2, f3, f4 = st.columns(4)

    with f1:
        min_year = int(df["Model Year"].min())
        max_year = int(df["Model Year"].max())
        years = st.slider(":material/calendar_month: سنة الصنع", min_year, max_year, (2012, max_year))

    with f2:
        car_type = st.selectbox(":material/ev_station: نوع السيارة",
                                ["الكل"] + sorted(df["Electric Vehicle Type"].unique()))

    with f3:
        makes = st.multiselect(":material/directions_car: الشركة",
                               df["Make"].value_counts().index,
                               placeholder="كل الشركات")

    with f4:
        county = st.selectbox(":material/location_on: المقاطعة",
                              ["الكل"] + list(df["County"].value_counts().index))

data = df[df["Model Year"].between(years[0], years[1])]
if car_type != "الكل":
    data = data[data["Electric Vehicle Type"] == car_type]
if makes:  
    data = data[data["Make"].isin(makes)]
if county != "الكل":
    data = data[data["County"] == county]

if data.empty:
    st.warning("ما فيه بيانات بهذي الفلاتر، جرّب توسّعها", icon=":material/search_off:")
    st.stop()

tesla = data[data["Make"] == "Tesla"]


k1, k2, k3, k4 = st.columns(4)

with k1.container(border=True):
    st.metric(":material/directions_car: إجمالي السيارات", f"{len(data):,}")
with k2.container(border=True):
    st.metric(":material/bolt: حصة تسلا", f"{len(tesla) / len(data):.1%}")
with k3.container(border=True):
    bev = (data["Electric Vehicle Type"] == "كهربائية بالكامل").mean()
    st.metric(":material/battery_charging_full: كهربائية بالكامل", f"{bev:.0%}")
with k4.container(border=True):
    st.metric(":material/speed: متوسط المدى", f"{data['Electric Range'].mean():.0f} ميل")

st.write("")


tab1, tab2, tab3, tab4 = st.tabs([
    ":material/dashboard: نظرة عامة",
    ":material/bolt: تسلا",
    ":material/location_city: المدن",
    ":material/table_view: البيانات",
])

with tab1:
    left, right = st.columns(2)

    with left.container(border=True):
        st.markdown("##### :material/leaderboard: أكثر 10 شركات")
        top = data["Make"].value_counts().head(10).reset_index()
        top.columns = ["الشركة", "العدد"]
        fig = px.bar(top, x="العدد", y="الشركة", orientation="h",
                     color=top["الشركة"] == "Tesla",
                     color_discrete_map={True: TESLA_RED, False: LIGHT_BLUE})
        fig.update_layout(yaxis={"categoryorder": "total ascending"}, showlegend=False)
        st.plotly_chart(style_chart(fig), use_container_width=True)

    with right.container(border=True):
        st.markdown("##### :material/show_chart: تسلا مقابل باقي الشركات")
        by_year = data.groupby(["Model Year", "Group"]).size().reset_index(name="العدد")
        fig = px.line(by_year, x="Model Year", y="العدد", color="Group", markers=True,
                      color_discrete_map={"Tesla": TESLA_RED, "باقي الشركات": BLUE},
                      labels={"Model Year": "سنة الصنع"})
        st.plotly_chart(style_chart(fig), use_container_width=True)

    left, right = st.columns(2)

    with left.container(border=True):
        st.markdown("##### :material/ev_station: نوع السيارة")
        fig = px.pie(data, names="Electric Vehicle Type", hole=0.55,
                     color_discrete_sequence=[BLUE, GRAY])
        st.plotly_chart(style_chart(fig), use_container_width=True)

    with right.container(border=True):
        st.markdown("##### :material/speed: متوسط المدى لأكثر الشركات (ميل)")
        top10 = data["Make"].value_counts().head(10).index
        avg_range = (data[data["Make"].isin(top10)]
                     .groupby("Make")["Electric Range"].mean()
                     .dropna().sort_values().reset_index())
        fig = px.bar(avg_range, x="Electric Range", y="Make", orientation="h",
                     color=avg_range["Make"] == "Tesla",
                     color_discrete_map={True: TESLA_RED, False: LIGHT_BLUE},
                     labels={"Electric Range": "المدى", "Make": ""})
        fig.update_layout(showlegend=False)
        st.plotly_chart(style_chart(fig), use_container_width=True)

with tab2:
    if tesla.empty:
        st.info("تسلا مو ضمن الشركات المختارة", icon=":material/info:")
    else:
        t1, t2, t3 = st.columns(3)
        with t1.container(border=True):
            st.metric(":material/directions_car: سيارات تسلا", f"{len(tesla):,}")
        with t2.container(border=True):
            st.metric(":material/star: الموديل الأكثر", tesla["Model"].value_counts().index[0])
        with t3.container(border=True):
            st.metric(":material/location_city: المدينة الأكثر", tesla["City"].value_counts().index[0])

        left, right = st.columns(2)

        with left.container(border=True):
            st.markdown("##### :material/pie_chart: توزيع موديلات تسلا")
            fig = px.pie(tesla, names="Model", hole=0.55,
                         color_discrete_sequence=[TESLA_RED, "#16202C", LIGHT_BLUE, GRAY])
            st.plotly_chart(style_chart(fig), use_container_width=True)

        with right.container(border=True):
            st.markdown("##### :material/timeline: موديلات تسلا عبر السنين")
            models_year = tesla.groupby(["Model Year", "Model"]).size().reset_index(name="العدد")
            fig = px.bar(models_year, x="Model Year", y="العدد", color="Model",
                         color_discrete_sequence=[TESLA_RED, "#16202C", LIGHT_BLUE, GRAY],
                         labels={"Model Year": "سنة الصنع", "Model": "الموديل"})
            st.plotly_chart(style_chart(fig), use_container_width=True)

with tab3:
    with st.container(border=True):
        st.markdown("##### :material/location_city: أكثر المدن")
        n = st.slider("عدد المدن", 5, 20, 10)
        cities = data["City"].value_counts().head(n).reset_index()
        cities.columns = ["المدينة", "العدد"]
        fig = px.bar(cities, x="العدد", y="المدينة", orientation="h",
                     color_discrete_sequence=[BLUE])
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(style_chart(fig, height=n * 35 + 100), use_container_width=True)

with tab4:
    with st.container(border=True):
        st.markdown(f"##### :material/table_view: البيانات بعد الفلترة ({len(data):,} سجل)")
        columns = ["Make", "Model", "Model Year", "Electric Vehicle Type", "Electric Range", "City", "County"]
        st.dataframe(data[columns], use_container_width=True, hide_index=True)
        st.download_button(":material/download: تحميل CSV",
                           data[columns].to_csv(index=False).encode("utf-8-sig"),
                           file_name="ev_filtered.csv")
