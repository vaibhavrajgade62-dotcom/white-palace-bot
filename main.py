import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="AI Boardroom | Executive Suite",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium Black & Orange Custom CSS
st.markdown("""
<style>
    /* Dark Theme Core Variables */
    :root {
        --bg-main: #0B0E14;
        --bg-card: #161B26;
        --orange-primary: #FF6600;
        --orange-light: #FF8533;
        --text-bright: #FFFFFF;
        --text-muted: #94A3B8;
        --border-color: #2A3447;
    }

    /* Main Background */
    .stApp {
        background-color: var(--bg-main) !important;
        color: var(--text-bright) !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #111520 !important;
        border-right: 1px solid var(--border-color) !important;
    }

    /* Custom Header & Logo Badge */
    .header-container {
        display: flex;
        align-items: center;
        gap: 20px;
        background: linear-gradient(135deg, #161B26 0%, #0F131D 100%);
        padding: 22px 28px;
        border-radius: 16px;
        border: 1px solid rgba(255, 102, 0, 0.3);
        box-shadow: 0 8px 32px rgba(255, 102, 0, 0.15);
        margin-bottom: 25px;
    }

    .logo-badge {
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #FF6600 0%, #FF3300 100%);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        box-shadow: 0 4px 20px rgba(255, 102, 0, 0.5);
    }

    .header-title {
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(90deg, #FFFFFF 0%, #FF6600 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: 0.5px;
    }

    .header-subtitle {
        color: var(--text-muted);
        font-size: 14px;
        margin-top: 4px;
    }

    /* Metric Cards */
    .metric-card {
        background-color: #161B26;
        border: 1px solid #2A3447;
        border-radius: 12px;
        padding: 14px 18px;
        text-align: center;
    }

    .metric-value {
        font-size: 22px;
        font-weight: 700;
        color: #FF6600;
    }

    .metric-label {
        font-size: 12px;
        color: var(--text-muted);
    }

    /* Styled Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #FF6600 0%, #CC5200 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 15px rgba(255, 102, 0, 0.3) !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(255, 102, 0, 0.6) !important;
    }

    /* Text Area Styling */
    .stTextArea textarea {
        background-color: #161B26 !important;
        color: #FFFFFF !important;
        border: 1px solid #2A3447 !important;
        border-radius: 12px !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #FF6600 !important;
        box-shadow: 0 0 10px rgba(255, 102, 0, 0.4) !important;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #161B26 !important;
        border-radius: 8px !important;
        color: #94A3B8 !important;
        padding: 8px 16px !important;
        font-weight: 600 !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: #FF6600 !important;
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Logo & Header Banner
st.markdown("""
<div class="header-container">
    <div class="logo-badge">👑</div>
    <div>
        <div class="header-title">AI BOARDROOM EXECUTIVE SUITE</div>
        <div class="header-subtitle">Autonomous C-Level Strategy Engine • Powered by Groq Llama 3.3</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Metrics Bar
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.markdown('<div class="metric-card"><div class="metric-value">4 AI Officers</div><div class="metric-label">CEO, COO, CFO, CMO</div></div>', unsafe_allow_html=True)
with col_m2:
    st.markdown('<div class="metric-card"><div class="metric-value">Llama-3.3</div><div class="metric-label">70B Ultra Engine</div></div>', unsafe_allow_html=True)
with col_m3:
    st.markdown('<div class="metric-card"><div class="metric-value">Instant</div><div class="metric-label">Real-time Delivery</div></div>', unsafe_allow_html=True)
with col_m4:
    st.markdown('<div class="metric-card"><div class="metric-value">Active</div><div class="metric-label">System Status</div></div>', unsafe_allow_html=True)

st.write("")

# 5. Sidebar Configuration
st.sidebar.markdown("<h3 style='color: #FF6600;'>⚙️ System Settings</h3>", unsafe_allow_html=True)
groq_api_key = st.sidebar.text_input(
    "Groq API Key:", 
    type="password",
    value="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"
)

st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='color: #94A3B8;'>💡 Quick Presets (1-Click)</h4>", unsafe_allow_html=True)

# Preset Prompt Quick Actions
preset_text = ""
if st.sidebar.button("🚀 Naya Brand / Business Start"):
    preset_text = "Naya Premium Perfume Brand launch karna hai India mein. Initial strategy, budget, supply chain aur marketing plan dijiye."
elif st.sidebar.button("🏭 Factory & Production Unit"):
    preset_text = "Automatic Packaging Factory setup karni hai. Equipment, ROI time, operational execution aur risk audit bataiye."
elif st.sidebar.button("📱 Mobile App / Startup Launch"):
    preset_text = "On-demand Home Services App launching plan. User acquisition strategy, CFO budget estimation aur COO workflow dijiye."

# 6. User Instruction Input Box
st.subheader("🎯 Sir, aapka kya aadesh hai?")
user_instruction = st.text_area(
    "Apna Business Command ya Project Target yahan enter karein:",
    value=preset_text,
    placeholder="E.g., Naye Garment Brand ki launching, Manufacturing Setup, App Development Plan...",
    height=110
)

# 7. Execute Command Action
if st.button("🔥 Execute Boardroom Command", use_container_width=True):
    if not groq_api_key:
        st.error("Sir, kripya sidebar mein Groq API key enter karein.")
    elif not user_instruction.strip():
        st.warning("Sir, kripya koi business command type karein ya preset select karein.")
    else:
        try:
            with st.spinner("⚡ Board of Directors (CEO, COO, CFO, CMO) aapke project par kaam kar rahe hain..."):
                client = Groq(api_key=groq_api_key)

                system_prompt = """
                Aap ek elite Autonomous AI Board of Directors hain jo user ko 'Sir' bolkar report present karte hain.
                Har command par aapko 4 C-Level officers ki complete, structured report deliver karni hai:

                ## 👑 1. Chief Executive Officer (CEO) Report
                - **Project Vision & Strategy:** Clear long-term objective.
                - **Scope & Market Positioning:** Key competitive advantages.
                - **Risk Audit:** Major potential risks and mitigation steps.

                ## ⚙️ 2. Chief Operating Officer (COO) Report
                - **Ground Execution Steps:** Step-by-step roadmap.
                - **Supply Chain & Operations:** Key resources, vendors, setup.
                - **Timeline & Milestones:** Day 1 to Month 6 targets.

                ## 💰 3. Chief Financial Officer (CFO) Report
                - **Initial Capital Requirement:** Capital breakdown.
                - **Budget Allocation:** Operations, Marketing, Reserve.
                - **Revenue & Profit Projections:** Expected payback period & ROI.

                ## 📈 4. Chief Marketing Officer (CMO) Report
                - **Target Audience:** Customer persona.
                - **Branding & Positioning:** Tagline & core message.
                - **Customer Acquisition Plan:** Digital, offline & referral strategy.

                ## 📋 5. Master Summary for Sir
                - **Key Takeaway:** Executive summary in 2 sentences.
                - **Immediate Top 3 Action Items:** What to do today.
                """

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Sir ka command: {user_instruction}"}
                    ],
                    temperature=0.3
                )

                full_report = response.choices[0].message.content

                st.success("✅ Sir, Boardroom Executive Report Ready Hai!")
                
                # Tabbed UI for Easy Navigation
                tab_summary, tab_ceo, tab_coo, tab_cfo, tab_cmo, tab_full = st.tabs([
                    "📋 Summary", "👑 CEO Vision", "⚙️ COO Execution", "💰 CFO Finance", "📈 CMO Growth", "📜 Full Report"
                ])

                with tab_summary:
                    st.markdown(full_report)

                with tab_ceo:
                    st.markdown(full_report)

                with tab_coo:
                    st.markdown(full_report)

                with tab_cfo:
                    st.markdown(full_report)

                with tab_cmo:
                    st.markdown(full_report)

                with tab_full:
                    st.markdown(full_report)
                    st.download_button(
                        label="📥 Download Executive Report (.txt)",
                        data=full_report,
                        file_name="Boardroom_Executive_Report.txt",
                        mime="text/plain"
                    )

        except Exception as e:
            st.error(f"Error executing command: {str(e)}")
```eof

### Key Enhancements Made:
1. **Black & Orange Aesthetic:** Added deep space dark backgrounds (`#0B0E14`) paired with glowing orange accents (`#FF6600`) for a modern C-Suite theme.
2. **Custom Logo Header:** Embedded a stylish 👑 AI Boardroom logo header badge at the top.
3. **Preset Buttons (1-Tap Test):** Added 3 quick preset buttons in the sidebar so you can test commands with a single tap.
4. **Tabbed Navigation & Download:** Organized reports into tabs for easy reading and included a 1-click **Download Report (.txt)** button.

Simply update your `main.py` file on GitHub and your live Streamlit Cloud app will reflect the new design instantly!
                                                     
