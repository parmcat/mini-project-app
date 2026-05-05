import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="US Economic Trends (1960-2026)",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .tab-content {
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="main-header">📈 US Economic Trends Analysis (1960-2026)</div>', unsafe_allow_html=True)
st.markdown("A comprehensive examination of economic indicators, growth patterns, and policy implications")
st.divider()

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Economic Upsides", "📉 Economic Downsides", "💡 What We Can Do", "📚 Appendix"])

# ============================================================================
# TAB 1: ECONOMIC UPSIDES
# ============================================================================
with tab1:
    st.header("Economic Upsides")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Real GDP Growth")
        st.markdown("""
        **Key Achievements:**
        - Overall GDP growth from ~$543B (1960) to over $28T+ (2026)
        - Sustained expansion periods creating jobs and wealth
        - Technological innovation driving productivity
        - Consumer spending and business investment
        """)
    
    with col2:
        st.subheader("Rising Standards of Living")
        st.markdown("""
        **Quality of Life Improvements:**
        - Increased homeownership rates
        - Better access to healthcare and education
        - Consumer goods became affordable
        - Rising median household incomes (adjusted for inflation in many periods)
        """)
    
    st.divider()
    
    # Example visualization - GDP Growth
    st.subheader("Real GDP Growth Over Time")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Sample data - replace with actual data
        years = [1960, 1970, 1980, 1990, 2000, 2010, 2020, 2026]
        gdp = [543, 1039, 2790, 5963, 10252, 15065, 20936, 28780]  # Billions, sample figures
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years, y=gdp,
            mode='lines+markers',
            name='Real GDP',
            line=dict(color='#2E7D32', width=3),
            marker=dict(size=8)
        ))
        fig.update_layout(
            title="US Real GDP Growth (1960-2026)",
            xaxis_title="Year",
            yaxis_title="GDP (Billions USD)",
            hovermode='x unified',
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.metric("GDP Growth (1960-2026)", "+5,200%", "Real growth")
    
    st.divider()
    
    st.subheader("Additional Positive Trends")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Technology & Innovation**
        - Digital revolution
        - Biotech advances
        - Green energy growth
        """)
    
    with col2:
        st.markdown("""
        **Employment**
        - Labor force expansion
        - Service sector growth
        - Entrepreneurship opportunities
        """)
    
    with col3:
        st.markdown("""
        **Global Trade**
        - International commerce growth
        - Export opportunities
        - Capital flows
        """)

# ============================================================================
# TAB 2: ECONOMIC DOWNSIDES
# ============================================================================
with tab2:
    st.header("Economic Downsides")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Income Inequality")
        st.markdown("""
        **Growing Disparities:**
        - Gini coefficient increased over decades
        - Wage stagnation for middle/working class
        - Executive compensation growth outpacing worker wages
        - Wealth concentration in top 1%
        """)
    
    with col2:
        st.subheader("Financial Crises")
        st.markdown("""
        **Major Disruptions:**
        - 1970s stagflation
        - 1987 stock market crash
        - 2008 Great Recession
        - 2020 COVID-19 economic shock
        """)
    
    st.divider()
    
    # Example visualization - Inflation
    st.subheader("Inflation Trends")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        years = [1960, 1970, 1975, 1980, 1985, 1990, 2000, 2010, 2020, 2026]
        inflation = [1.7, 5.7, 9.1, 13.5, 3.6, 5.4, 3.4, 1.6, 1.4, 3.2]  # Sample figures
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years, y=inflation,
            mode='lines+markers',
            name='Inflation Rate',
            fill='tozeroy',
            line=dict(color='#D32F2F', width=3),
            marker=dict(size=8)
        ))
        fig.update_layout(
            title="Annual Inflation Rate (1960-2026)",
            xaxis_title="Year",
            yaxis_title="Inflation (%)",
            hovermode='x unified',
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.metric("Peak Inflation", "13.5%", "1980")
    
    st.divider()
    
    st.subheader("Additional Concerns")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Debt & Deficits**
        - Rising national debt
        - Student loan crisis
        - Corporate debt growth
        """)
    
    with col2:
        st.markdown("""
        **Labor Issues**
        - Job displacement
        - Automation impacts
        - Benefit erosion
        """)
    
    with col3:
        st.markdown("""
        **Environmental Costs**
        - Unsustainable practices
        - Climate change impacts
        - Resource depletion
        """)

# ============================================================================
# TAB 3: WHAT WE CAN DO ABOUT IT
# ============================================================================
with tab3:
    st.header("What We Can Do About It")
    
    st.subheader("Policy Solutions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Government & Fiscal Policy
        
        **Income & Wealth**
        - Progressive taxation reform
        - Strengthen social safety net
        - Raise minimum wage standards
        - Affordable housing initiatives
        
        **Education & Training**
        - Invest in public education
        - STEM program expansion
        - Affordable vocational training
        - Apprenticeship programs
        """)
    
    with col2:
        st.markdown("""
        ### Monetary & Structural Reforms
        
        **Financial Stability**
        - Strengthen banking regulations
        - Reduce speculation incentives
        - Improve consumer protection
        
        **Long-term Growth**
        - Infrastructure investment
        - R&D tax credits
        - Green energy transition
        - Small business support
        """)
    
    st.divider()
    
    st.subheader("Individual & Business Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **For Individuals**
        - Financial literacy
        - Skill development
        - Diversified investments
        - Sustainable consumption
        """)
    
    with col2:
        st.markdown("""
        **For Businesses**
        - Fair wage practices
        - Worker development
        - Stakeholder capitalism
        - Sustainable operations
        """)
    
    with col3:
        st.markdown("""
        **For Communities**
        - Local economic initiatives
        - Cooperative models
        - Community investment
        - Civic engagement
        """)
    
    st.divider()
    
    st.subheader("Comparative Policy Effectiveness")
    
    # Example comparison table
    policies = pd.DataFrame({
        'Policy Area': ['Tax Reform', 'Education Investment', 'Infrastructure', 'Wage Standards'],
        'Short-term Impact': ['High', 'Low', 'Medium', 'Medium'],
        'Long-term Impact': ['Medium', 'Very High', 'High', 'Medium'],
        'Implementation Difficulty': ['High', 'Medium', 'Medium', 'Medium']
    })
    
    st.dataframe(policies, use_container_width=True)

# ============================================================================
# TAB 4: APPENDIX
# ============================================================================
with tab4:
    st.header("Appendix")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Data Sources")
        st.markdown("""
        - **Bureau of Economic Analysis (BEA)** - GDP data
        - **Bureau of Labor Statistics (BLS)** - Employment, inflation
        - **Federal Reserve (FRED)** - Economic indicators
        - **Census Bureau** - Income, poverty statistics
        - **World Bank** - International comparisons
        """)
    
    with col2:
        st.subheader("Key Definitions")
        st.markdown("""
        - **GDP**: Total economic output
        - **Inflation**: Rate of price increase
        - **Unemployment**: % of labor force without jobs
        - **Gini Coefficient**: Income inequality measure (0-1)
        - **Real vs Nominal**: Adjusted vs unadjusted for inflation
        """)
    
    st.divider()
    
    st.subheader("Major Economic Events (1960-2026)")
    
    events = pd.DataFrame({
        'Year': [1973, 1987, 2001, 2008, 2020],
        'Event': ['Oil Crisis', 'Black Monday', '9/11 Attacks', 'Financial Crisis', 'COVID-19 Pandemic'],
        'Impact': ['Stagflation', 'Market Crash', 'Recession', 'Great Recession', 'Economic Shock'],
        'Recovery Time': ['5-7 years', '18 months', '2-3 years', '5-7 years', '1-2 years']
    })
    
    st.dataframe(events, use_container_width=True)
    
    st.divider()
    
    st.subheader("Recommended Further Reading")
    st.markdown("""
    - Piketty, T. "Capital in the Twenty-First Century"
    - Stiglitz, J. "The Price of Inequality"
    - Acemoglu, D. & Robinson, J. "Why Nations Fail"
    - Autor, D. "The Work of the Future"
    - World Economic Forum Reports
    """)
    
    st.divider()
    
    with st.expander("Project Metadata"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Created:** {datetime.now().strftime('%B %d, %Y')}")
            st.write("**Data Period:** 1960-2026")
        with col2:
            st.write("**Focus:** US Economic Trends")
            st.write("**Tool:** Streamlit + Plotly")

# Footer
st.divider()
st.caption("📊 US Economic Trends Analysis | Data sources: BEA, BLS, Federal Reserve | Last updated: 2026")
