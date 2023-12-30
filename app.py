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
option = st.sidebar.selectbox('Select One', ['Home', 'Overall Analysis', 'Startup', 'Investor'])


def load_home_page():
    st.title('Indian Startup Analysis')
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.header('What is a Startup???')
            st.write("""
            A startup is a new business that aims to provide a service or product—often in a large or growing market—to solve a specific and sometimes difficult problem. These businesses set goals to make a significant impact for their customers or clients in a short period of time and to expand production rapidly.
            \nStartups share similarities with small businesses, often including limited funding, minimal staff and uncertainty about success when they begin. There are also many differences that set them apart:
            \n-Industries
            \n-Target market
            \n-Growth
            \n-Financial investment""")
        with col2:
            st.image('home page - images/imhome1.jpeg')
    st.header("Some of India's biggest home-grown startups - ")
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image('home page - images/imhome2.jpeg')
            st.markdown("## BYJU'S")
            st.markdown("""
            <div style="text-align: justify">Founded by Byju Raveendran, BYJU'S is an Indian educational technology company offering online learning programs for students. It provides interactive lessons and personalized learning experiences through engaging video content and adaptive learning techniques across various subjects and grade levels.</div>
            """,unsafe_allow_html=True)
        with col2:
            st.image('home page - images/imhome3.jpeg')
            st.markdown("## SWIGGY")
            st.markdown("""
                        <div style="text-align: justify">Co-founded by Lakshmi Nandan Reddy, Rahul Jaimini, and Sriharsha Majety, Swiggy is an online food delivery platform that connects users with nearby restaurants, allowing them to order food from a wide range of cuisines and have it delivered to their doorstep with ease and convenience</div>
                        """, unsafe_allow_html=True)
        with col3:
            st.image('home page - images/imhome4.jpeg')
            st.markdown("## OYO ROOMS")
            st.markdown("""
                        <div style="text-align: justify">Founded by Ritesh Agarwal, OYO Rooms is a hospitality company that offers a network of budget hotels, homes, and lodging accommodations across various destinations globally. It provides affordable and standardized stays with a focus on convenience, quality, and consistent amenities, catering to diverse traveler needs.</div>
                        """, unsafe_allow_html=True)
        with col4:
            st.image('home page - images/imhome5.jpeg')
            st.markdown("## DREAM11")
            st.markdown("""
                        <div style="text-align: justify">Co-founded by Harsh Jain and Bhavit Sheth, Dream11 is a fantasy sports platform that allows users to create virtual teams composed of real-life players from various sports like cricket, football, etc. Participants compete against each other based on the statistical performance of these players in actual matches to win.</div>
                        """, unsafe_allow_html=True)
        with col5:
            st.image('home page - images/imhome6.jpeg')
            st.markdown("## OLA CABS")
            st.markdown("""
                        <div style="text-align: justify">Founded by Bhavish Aggarwal, OLA Cab is a renowned ride-hailing service providing convenient and on-demand transportation a mobile app. It connects passengers with various types of vehicles, including taxis, auto-rickshaws, and rental cars, offering a seamless and efficient travel experience across cities.</div>
                        """, unsafe_allow_html=True)
    st.header("Some of India's biggest home-grown individual investors - ")
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image('home page - images/imhome9.webp')
            st.markdown("## Mr. Radhakishan Damani")
            st.metric('Total Investment ', 'Rs  ' + '178,572.4' + '  Cr')
        with col2:
            st.image('home page - images/imhome10.jpeg')
            st.markdown("## Mr. Rakesh Jhunjhunwala")
            st.metric('Total Investment ', 'Rs  ' + '32,059.54' + '  Cr')
        with col3:
            st.image('home page - images/imhome12.jpeg')
            st.markdown("## Mr. Mukul Agrawal")
            st.metric('Total Investment ', 'Rs  ' + '4,695.6' + '  Cr')
        with col4:
            st.image('home page - images/imhome1333.jpeg')
            st.markdown("## Mr. Ashish Dhawan")
            st.metric('Total Investment ', 'Rs  ' + '3,561.34' + '  Cr')
        with col5:
            st.image('home page - images/imhome11.webp')
            st.markdown("## Mr. Hemendra Kothari")
            st.metric('Total Investment ', 'Rs  ' + '1,113.71' + '  Cr')


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


if option == 'Home':
    load_home_page()
elif option == 'Overall Analysis':
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
