import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('startup_cleaned (1).csv')
st.set_page_config(layout='wide', page_title='Startup Analysis')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
# Data Cleaning

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])


def load_overall_analysis():
    st.title('Overall Analysis')
    # Total invested amount
    total = round(df['amount'].sum())
    # Max Total amount infused in a single startup
    max_invest = round(df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0])
    # Average Total amount infused in a single startup
    average_invest = round(df.groupby('startup')['amount'].sum().mean())
    # Total Startups to receive investment
    total_startup = df['startup'].nunique()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total Investment ', 'Rs  ' + str(total) + '  Cr')
    with col2:
        st.metric('Max Investment/Startup ', 'Rs  ' + str(max_invest) + '  Cr')
    with col3:
        st.metric('Average Investment/Startup ', 'Rs  ' + str(average_invest) + '  Cr')
    with col4:
        st.metric('Total invested Startups ', str(total_startup))
    st.header('MOM Graph :')

    selected_option = st.selectbox('Select Type', ['Total', 'Count'])
    if selected_option == 'Count':
        tempdf = df.groupby(['year', 'month'])['startup'].count().reset_index()
        tempdf['x_axis'] = tempdf['month'].astype('str') + '-' + tempdf['year'].astype('str')
        fig1, ax1 = plt.subplots()
        ax1.plot(tempdf['x_axis'], tempdf['startup'])
        st.pyplot(fig1)
    else:
        tempdf = df.groupby(['year', 'month'])['amount'].sum().reset_index()
        tempdf['x_axis'] = tempdf['month'].astype('str') + '-' + tempdf['year'].astype('str')
        fig1, ax1 = plt.subplots()
        ax1.plot(tempdf['x_axis'], tempdf['amount'])
        st.pyplot(fig1)


def load_investor_details(selected_investor):
    st.title(selected_investor)
    # To load the recent 5 investments of the investor!
    last5_df = df[df['investors'].str.contains(selected_investor)].head(5)[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    col1, col2 = st.columns(2)
    with col1:
        # Biggest Investment
        big_series = df[df['investors'].str.contains(selected_investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)
    with col2:
        vertical_series = df[df['investors'].str.contains(selected_investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig1)
    col1, col2 = st.columns(2)
    with col1:
        vertical_series = df[df['investors'].str.contains(selected_investor)].groupby('round')['round'].count()
        st.subheader('Round Invested')
        fig2, ax2 = plt.subplots()
        ax2.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)
    with col2:
        vertical_series = df[df['investors'].str.contains(selected_investor)].groupby('city')['city'].count()
        st.subheader('City Invested')
        fig3, ax3 = plt.subplots()
        ax3.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig3)

    year_series = df[df['investors'].str.contains(selected_investor)].groupby('year')['amount'].sum()
    st.subheader('YoY Investment')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)
    st.pyplot(fig4)


if option == 'Overall Analysis':
    load_overall_analysis()
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
