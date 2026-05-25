import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title='CryptoPulse Streamlit', page_icon='💹', layout='wide')

portfolio_data = pd.DataFrame([
    {'coin': 'Bitcoin', 'symbol': 'BTC', 'holdings': '1.84 BTC', 'value': 127000, 'change': 4.8, 'allocation': 45},
    {'coin': 'Ethereum', 'symbol': 'ETH', 'holdings': '24.1 ETH', 'value': 90400, 'change': 3.2, 'allocation': 28},
    {'coin': 'Solana', 'symbol': 'SOL', 'holdings': '582 SOL', 'value': 109400, 'change': -2.1, 'allocation': 14},
    {'coin': 'Cardano', 'symbol': 'ADA', 'holdings': '14,302 ADA', 'value': 22100, 'change': 1.8, 'allocation': 13},
])

market_data = pd.DataFrame({
    'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'market_index': [120, 125, 123, 130, 135, 140, 138],
    'volume': [9.8, 10.2, 9.6, 10.8, 11.1, 10.7, 10.9],
})

heatmap_data = pd.DataFrame([
    {'sector': 'DeFi', 'risk': 'Low', 'value': 68},
    {'sector': 'NFT', 'risk': 'Medium', 'value': 58},
    {'sector': 'Layer 1', 'risk': 'High', 'value': 42},
    {'sector': 'Stablecoins', 'risk': 'Low', 'value': 74},
    {'sector': 'Gaming', 'risk': 'Medium', 'value': 51},
])

sentiment_data = pd.DataFrame({
    'sentiment': ['Bullish', 'Neutral', 'Bearish'],
    'score': [68, 21, 11],
})

page = st.sidebar.selectbox('Navigate', ['Home', 'Dashboard', 'Portfolio', 'Analytics'])

st.sidebar.markdown('---')
st.sidebar.markdown('**Streamlit app for CryptoPulse**')
st.sidebar.markdown('Click any page to explore the live Streamlit version.')

if page == 'Home':
    st.markdown('# CryptoPulse Live Dashboard')
    st.write('Track your crypto assets in real time, explore portfolio health, and compare market signals with Streamlit-powered charts.')
    c1, c2, c3 = st.columns(3)
    c1.metric('Total Balance', '$128.4K', '+12.4%')
    c2.metric('Active Assets', '16 Coins', 'Stable')
    c3.metric('Projected Growth', '+18.9%', '30-day outlook')

    st.markdown('## Market Pulse')
    trend_chart = alt.Chart(market_data).mark_line(point=True).encode(
        x='day',
        y='market_index',
        tooltip=['day', 'market_index'],
        color=alt.value('#5EBAE0')
    ).properties(height=360)
    st.altair_chart(trend_chart, width='stretch')

    st.markdown('## Portfolio Highlights')
    st.write('A quick summary of your asset allocation and high-performing coins.')
    cols = st.columns(4)
    for col, label, value, delta in zip(cols, ['Bitcoin', 'Ethereum', 'Solana', 'Cardano'], ['45%', '28%', '14%', '13%'], ['+4.8%', '+3.2%', '-2.1%', '+1.8%']):
        col.write(f'### {label}')
        col.write(f'**{value}**')
        col.write(delta)

elif page == 'Dashboard':
    st.markdown('# Dashboard')
    st.write('A modern dashboard view for portfolio performance, market trends, and allocation.')
    st.markdown('### Market Trend')
    line_chart = alt.Chart(market_data).mark_area(opacity=0.4, interpolate='monotone').encode(
        x='day',
        y='market_index',
        tooltip=['day', 'market_index']
    ).properties(height=360)
    st.altair_chart(line_chart, use_container_width=True)

    st.markdown('### Portfolio Allocation')
    pie_chart = alt.Chart(portfolio_data).mark_arc(innerRadius=50).encode(
        theta='allocation',
        color=alt.Color('coin', legend=None),
        tooltip=['coin', 'allocation']
    ).properties(height=360)
    st.altair_chart(pie_chart, width='stretch')

    st.markdown('### Top Movers')
    st.table(portfolio_data[['coin', 'holdings', 'value', 'change']].rename(columns={
        'coin': 'Coin',
        'holdings': 'Holdings',
        'value': 'Value',
        'change': 'Change (%)'
    }))

elif page == 'Portfolio':
    st.markdown('# Portfolio')
    st.write('Detailed asset breakdown and allocation insights for your crypto holdings.')
    cols = st.columns(2)
    with cols[0]:
        st.markdown('### Allocation by Coin')
        altair_pie = alt.Chart(portfolio_data).mark_arc(innerRadius=60).encode(
            theta='allocation',
            color=alt.Color('coin', legend=None),
            tooltip=['coin', 'allocation']
        ).properties(height=420)
        st.altair_chart(altair_pie, width='stretch')
    with cols[1]:
        st.markdown('### Asset Table')
        st.dataframe(portfolio_data[['coin', 'symbol', 'holdings', 'value', 'change']], height=420)

    st.markdown('### Allocation Bar Chart')
    bar_chart = alt.Chart(portfolio_data).mark_bar().encode(
        x='coin',
        y='allocation',
        color=alt.Color('coin', legend=None),
        tooltip=['coin', 'allocation']
    ).properties(height=360)
    st.altair_chart(bar_chart, width='stretch')

else:
    st.markdown('# Analytics')
    st.write('Analytics powered by live indicators, sentiment, and risk signals.')
    st.markdown('### Sentiment Pulse')
    sentiment_chart = alt.Chart(sentiment_data).mark_bar().encode(
        x='sentiment',
        y='score',
        color=alt.Color('sentiment', scale=alt.Scale(range=['#34d399', '#60a5fa', '#f87171'])),
        tooltip=['sentiment', 'score']
    ).properties(height=360)
    st.altair_chart(sentiment_chart, use_container_width=True)

    st.markdown('### Risk Heatmap')
    heatmap = alt.Chart(heatmap_data).mark_rect().encode(
        x='risk:O',
        y='sector:O',
        color='value:Q',
        tooltip=['sector', 'risk', 'value']
    ).properties(height=360)
    st.altair_chart(heatmap, use_container_width=True)

    st.markdown('### Scorecard')
    st.metric('Performance Score', '89 / 100', 'Strong portfolio health')
    st.markdown('---')
    st.write('- Macro volatility warning')
    st.write('- Liquidity remains high')
    st.write('- Rebalance opportunity in altcoins')
