import streamlit as st
import plotly.express as px

# 1. Load the built-in Gapminder dataset
df = px.data.gapminder()

st.title(" Global Development Dashboard")
st.markdown("Exploring the relationship between GDP, Life Expectancy, and Population.")

# 2. Sidebar Filters
year = st.sidebar.slider("Select Year", 1952, 2007, 2007)
continent = st.sidebar.multiselect("Select Continent", df['continent'].unique(), default=['Asia', 'Europe'])

# 3. Filter the data based on selection
filtered_df = df[(df['year'] == year) & (df['continent'].isin(continent))]

# 4. The "Wow" Visualization
fig = px.scatter(
    filtered_df, 
    x="gdpPercap", 
    y="lifeExp", 
    size="pop", 
    color="country", 
    hover_name="country", 
    log_x=True, 
    size_max=60,
    title=f"Global Health & Wealth in {year}"
)

st.plotly_chart(fig, use_container_width=True)

# 5. Show raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)