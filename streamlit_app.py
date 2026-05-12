import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import base64

# configuration
st.set_page_config(
    page_title="US Economic Trends 1960-2026",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# aesthet
st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        background-color: #ffffff;
        color: #1a1a1a;
    }
    
    .main-container {
        max-width: 900px;
        margin: 0 auto;
    }
    
    .article-header {
        margin-bottom: 60px;
        border-bottom: 3px solid #CC0000;
        padding-bottom: 10px;
    }
    
    .article-title {
        font-size: 56px;
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 10px;
        color: #000;
        letter-spacing: -1px;
    }
    
    .article-subtitle {
        font-size: 24px;
        font-weight: 400;
        line-height: 1.4;
        color: #666;
        margin-bottom: 15px;
    }
    
    .article-byline {
        font-size: 14px;
        color: #999;
        font-style: italic;
        margin-top: 20px;
    }
    
    .text-block {
        font-size: 18px;
        line-height: 1.8;
        margin: 40px 0;
        color: #1a1a1a;
        max-width: 100%;
    }
    
    .text-block p {
        margin-bottom: 20px;
    }
    
    .text-block strong {
        font-weight: 600;
        color: #000;
    }
    
    .article-image {
        width: 100%;
        margin: 50px 0;
        background-color: #e0e0e0;
        aspect-ratio: 16 / 10;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 4px;
        font-size: 16px;
        color: #999;
        font-style: italic;
    }
    
    .image-caption {
        font-size: 14px;
        color: #666;
        margin-top: 10px;
        margin-bottom: 20px;
        font-style: italic;
        border-left: 3px solid #CC0000;
        padding-left: 15px;
    }
    
    .section-divider {
        height: 2px;
        background-color: #e0e0e0;
        margin: 10px 0;
    }
    
    .source-item {
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .source-item:last-child {
        border-bottom: none;
    }
    
    .source-title {
        font-weight: 600;
        font-size: 16px;
        color: #000;
        margin-bottom: 8px;
    }
    
    .source-details {
        font-size: 14px;
        color: #666;
        margin-bottom: 5px;
    }
    
    .source-url {
        font-size: 13px;
        color: #CC0000;
        word-break: break-all;
        text-decoration: none;
    }
    
    .tab-content {
        padding: 40px 0;
    }
    
    [data-testid="stTabs"] [data-testid="stTab"] {
        font-size: 16px;
        font-weight: 600;
    }
    
    h1 {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# tabs
tab1, tab2 = st.tabs(["Main", "Sources & Methodology"])

with tab1:
    st.markdown("""
    <div class="main-container">
        <div class="article-header">
            <div class="article-title">The Numbers Lie: What Really Happened to the American Economy Since 1960</div>
            <div class="article-subtitle">GDP grew. Unemployment fell. But the metrics economists love mask a more complex reality about what happened in American households.</div>
            <div class="article-byline">A visual analysis of six decades of economic data</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # introduction
    st.markdown("""
    <div class="main-container">
        <div class="text-block">
        <p>Economics students are often taught that any large-scale economy is built around three metrics: GDP, inflation, and unemployment.</p>
        <p>And even in the real world, it often does appear that way. Every quarter, the Federal Reserve announces the latest GDP figures. Financial commentators dissect unemployment rates to decimal points. The Federal Open Market Committee monitors inflation with utmost vigilance. And yet, if you ask the average American how they're doing financially, the conversation rarely sounds like the official statistics.</p>
        <p>This disconnect is not accidental. The metrics economists have built their reporting around—Gross Domestic Product, inflation, and national unemployment—offer a bird's-eye view of the economy. They capture borrowing activity, motion, and some degree of workforce participation. But they don't measure meaning. They don't tell you if your paycheck goes further or if you can afford a home. They don't track whether prosperity reaches everyone or concentrates among the few.</p>
        <p>Between 1960 and today, the official story is one of steady progress. But beneath those aggregate numbers lies a tale of two countries: one where some have gained access to unprecedented opportunity, and another where the foundations of economic security have shifted beneath people's feet.</p>
        <p><strong>This analysis examines some less well known but more relevant metrics—real-dollar values, purchasing power, living-wage differentials, underemployment, and real and perceived income disparity to try and understand the economic realities that people in the United States face beyond flashy national aggregate values.</strong></p>
      </div>
    </div>
    """, unsafe_allow_html=True)
    
    # image 1: purchasing power
    st.image("dollar-value.png", use_column_width=True)
    st.markdown("""<div class="image-caption">The value of the dollar has decreased by about 90% since 1960.</div>""", unsafe_allow_html=True)
    
    
    # the real cost of inflation isn't just trouble borrowing, it translates to purchasing power reduction
    st.markdown("""
    <div class="main-container">
        <div class="text-block">
        <p> The value of the dollar has decreased by 90 percent since 1960, often taking major hits after major financial crises—the OPEC embargo in 1975 and ensuing disasters in the 80s, and the 2008 lending market crash to name a few. </p>   
        <p>Then there's living wages. The standard employment statistic—the unemployment rate—tells you what percentage of the labor force is actively seeking work but can't find it. It doesn't tell you that someone working full-time might still fall below the poverty line. Simply put, a job is not necessarily a good job in the sense that it meets an individual’s economic needs. To address this discrepancy, this analysis provides a breakdown of the gap between the minimum wage and the living wage in every sate, providing a reference point for the distance between the bare minimum wages and bare minimum economic needs for the average person.</p>
            </div>
    </div>
    """, unsafe_allow_html=True)
    
    # image purchasing power by state 
    st.image("purchasing_power_state.png", use_column_width=True)
    st.markdown("""<div class="image-caption">The purchasing power of a single dollar actually varies wildly by state.</div>""", unsafe_allow_html=True)
    
    
  
    # employment, or lack thereof
    st.markdown("""
    <div class="main-container">
        <div class="text-block">
            <p>Between 1960 and 2026, while unemployment figures improved and GDP expanded, the percentage of people making a living wage—one sufficient to cover basic needs without government assistance—has failed to keep pace with population growth. Many who are counted as "employed" are actually employed in precarity. Others are under-employed, marginally attached to the workforce, or have stopped looking for work entirely despite needing it. This scenario is called underemployment. While the Bureau of labor Statistics (BLS) and other sources do measure this (typically called “U-6 unemployment”) it doesn’t generate the same buzz or level of care and attention as the national unemployment figures, which are often the only ones cited by major news networks.</p>
             <p>The BLS has also come under fire for their constant and significant revisions of existing job numbers. The figures for non-farm payroll enrollment, a key metric used by many as an estimate for the number of available jobs in the nation, is typically revised three times a year. While there is no harm in scientific revision to promote accuracy—in fact, it is encouraged—these particular re-releases have come under scrutiny because they reveal massive discrepancies in some months, leading to questions about the agency’s rigor.</p>
               <p>Even when individuals are employed, opinion polls show that an increasing number of people are worried about losing their jobs, as markets prove more unsteady than they appear on paper.</p>

        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Image 5
    
    
    
    # Image 6
 
    
    # Image 7

        
    # income inequality 
    st.markdown("""
    <div class="main-container">
        <div class="text-block">
            </div>
            <p> While virtually everyone in the United States is aware of income inequality, few people estimate the actual extent of it. The vast majority of people overestimate how easily they or others can achieve economic mobility, as well as exactly how much wealth is tied to very few individuals at the top of the national income pyramid. In my undergrad study circles, we called the discrepancy between the income pyramid people believed in and the income pyramid that existed in reality the Ziggurat of Doom. It was named this due to its incredibly lopsided yet stepwise nature in comparison to a traditional pyramid.</p>
            <p> Part of the reason many people have a hard time visualizing realistic income distributions boils down to how we envision both numbers and lifestyles. Many people have a hard time picturing the sheer scale of numerical difference between one million and one billion—it doesn’t help that the words sound similar. In polls, the majority of people overestimate how many households make a million dollars or more, and the vast majority of people say that the existence of billionaires and the amount billionaires are taxed are both reasonable.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Image 8
    
    
    # Image 9
      
    # what can we do about this?
    st.markdown("""
    <div class="main-container">
        <div class="text-block">
        <p>Policies that focus on raising wages, eliminating wealth gaps at the very top through taxation and the closing of legal loopholes, are one way to start. These policies help mitigate the consequences of high inflation and slowing GDP, which are out of control of the average person. In addition, the appropriate reporting of existing metrics, such as job availability and holistic unemployment (unemployment which includes under-employment) and accurate reporting on others such as market availability, will go a long way in addressing the gaps in how we measure economic stability. </p>
     </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Image 10
    
    # Image 11


   
    # Section 6: Closing
    st.markdown("""
    <div class="main-container">
        <div class="text-block">
            <p> End notes </p>
            </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Image 13 - Final image
    

with tab2:
    st.markdown("""
    <div class="main-container">
        <div style="margin-bottom: 40px;">
            <h2 style="font-size: 42px; font-weight: 700; margin-bottom: 30px; border-bottom: 3px solid #CC0000; padding-bottom: 20px;">Sources & Methodology</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-container">
        <div style="margin-bottom: 50px;">
            <h3 style="font-size: 24px; font-weight: 600; margin-bottom: 20px;">Data Sources</h3>
            
            <div class="source-item">
                <div class="source-title">Bureau of Labor Statistics (BLS)</div>
                <div class="source-details">U.S. Department of Labor</div>
                <div class="source-details">Data on employment, unemployment rates, wage growth, purchasing power parity, and consumer price index (CPI) from 1960-2026</div>
                <div class="source-url">www.bls.gov</div>
            </div>
            
            <div class="source-item">
                <div class="source-title">Federal Reserve Economic Data (FRED)</div>
                <div class="source-details">Federal Reserve Bank of St. Louis</div>
                <div class="source-details">Real GDP growth, nominal GDP, inflation rates, real personal income, and macroeconomic indicators</div>
                <div class="source-url">fred.stlouisfed.org</div>
            </div>
            
            <div class="source-item">
                <div class="source-title">U.S. Census Bureau</div>
                <div class="source-details">Housing and Household Economic Statistics Division</div>
                <div class="source-details">Housing affordability indices, homeownership rates by demographic group, median home prices relative to median household income</div>
                <div class="source-url">www.census.gov</div>
            </div>
            """, unsafe_allow_html=True)
            
              
          
           
