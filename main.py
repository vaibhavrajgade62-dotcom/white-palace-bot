import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="AI Boardroom | Executive Suite",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium Light Mode CSS (White Background, Pure Black Text, Orange Accents)
st.markdown("""
<style>
    /* Global Base */
    .stApp {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    /* Headings & Text Color Fix */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #111111 !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #E5E7EB !important;
    }

    /* Custom Header Container with Final Infinity Logo */
    .header-container {
        display: flex;
        align-items: center;
        gap: 18px;
        background: #FFFFFF;
        padding: 16px 20px;
        border-radius: 12px;
        border: 1.5px solid #F3F4F6;
        border-bottom: 3px solid #FF6600;
        box-shadow: 0 4px 16px rgba(0,0,0,0.04);
        margin-bottom: 24px;
    }

    .header-title {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: 0.5px;
        color: #111111 !important;
        margin: 0;
    }

    .header-subtitle {
        color: #666666 !important;
        font-size: 13px;
        font-weight: 500;
        margin-top: 2px;
    }

    /* Action Buttons */
    .stButton>button {
        background-color: #FF6600 !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 12px rgba(255, 102, 0, 0.25) !important;
        transition: all 0.2s ease !important;
    }

    .stButton>button * {
        color: #FFFFFF !important;
    }

    .stButton>button:hover {
        background-color: #E65C00 !important;
        transform: translateY(-1px);
    }

    /* Text Area */
    .stTextArea textarea {
        background-color: #FAFAFA !important;
        color: #111111 !important;
        border: 1.5px solid #E5E7EB !important;
        border-radius: 8px !important;
        font-size: 15px !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #FF6600 !important;
        box-shadow: 0 0 0 2px rgba(255, 102, 0, 0.2) !important;
    }

    /* Output Container */
    .report-box {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-left: 4px solid #FF6600;
        border-radius: 8px;
        padding: 20px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Header with Final Infinity AI Logo (SVG)
st.markdown("""
<div class="header-container">
    <div style="width: 54px; height: 54px; display: flex; align-items: center; justify-content: center;">
        <svg viewBox="0 0 100 100" width="54" height="54">
            <!-- Left Charcoal Infinity Loop -->
            <path d="M 50 50 C 35 30, 10 30, 10 50 C 10 70, 35 70, 50 50" 
                  fill="none" stroke="#161922" stroke-width="11" stroke-linecap="round"/>
            <!-- Right Vibrant Orange Infinity Loop -->
            <path d="M 50 50 C 65 30, 90 30, 90 50 C 90 70, 65 70, 50 50" 
                  fill="none" stroke="#FF6600" stroke-width="11" stroke-linecap="round"/>
            <!-- Center 4-Point AI Spark Cutout -->
            <path d="M 50 44 Q 50 50 56 50 Q 50 50 50 56 Q 50 50 44 50 Q 50 50 50 44 Z" 
                  fill="#FF6600"/>
        </svg>
    </div>
    <div>
        <div class="header-title">AI BOARDROOM EXECUTIVE SUITE</div>
        <div class="header-subtitle">Autonomous C-Level Strategy Engine • CEO | COO | CFO | CMO</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Sidebar Configuration
st.sidebar.markdown("### ⚙️ System Settings")
groq_api_key = st.sidebar.text_input(
    "Groq API Key:", 
    type="password",
    value="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"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Quick Presets")

preset_text = ""
if st.sidebar.button("🚀 Naya Brand / Business Start"):
    preset_text = "Naya Premium Brand launch karna hai. Go-to-market strategy, budget estimation, supply chain aur customer acquisition plan taiyar karein."
elif st.sidebar.button("🏭 Production & Supply Chain"):
    preset_text = "Manufacturing unit setup karni hai. Equipment procurement, monthly operational workflow, ROI period aur risk mitigation audit dein."

# 5. User Input
st.subheader("🎯 Sir, aapka kya aadesh hai?")
user_instruction = st.text_area(
    "Apna Business Command / Project Plan yahan likhein:",
    value=preset_text,
    placeholder="E.g., Naye product launch ka complete strategic plan, budget, distribution aur timeline banayein...",
    height=120
)

# 6. Execute Command
if st.button("🔥 Execute Boardroom Command", use_container_width=True):
    if not groq_api_key:
        st.error("Sir, kripya sidebar mein API key enter karein.")
    elif not user_instruction.strip():
        st.warning("Sir, kripya pehle koi business command type karein.")
    else:
        try:
            with st.spinner("⚡ Boardroom Officers (CEO, COO, CFO, CMO) execute kar rahe hain..."):
                client = Groq(api_key=groq_api_key)

                system_prompt = """
                Aap ek elite Autonomous AI Board of Directors hain jo user ko 'Sir' bolkar report present karte hain.
                Har command par aapko 4 C-Level officers ki complete, structured report deliver karni hai:

                ## 👑 1. Chief Executive Officer (CEO) Report
                - **Project Vision & Strategic Direction:** Long-term goal.
                - **Market Positioning & Moat:** Competitive advantage.
                - **Risk Audit:** Major potential risks and mitigation steps.

                ## ⚙️ 2. Chief Operating Officer (COO) Report
                - **Execution Roadmap:** Step-by-step phases.
                - **Operations & Supply Chain:** Key resources and vendors.
                - **Milestones & Deadlines:** Day 1 to Month 6 targets.

                ## 💰 3. Chief Financial Officer (CFO) Report
                - **Capital Requirement:** Setup and working capital breakdown.
                - **Budget Allocation:** Operations vs Marketing vs Reserve.
                - **Projections & ROI:** Expected break-even and margins.

                ## 📈 4. Chief Marketing Officer (CMO) Report
                - **Target Persona:** Primary buyer group.
                - **Positioning & Messaging:** Core marketing angle.
                - **Growth Channels:** Organic, paid and referral strategy.

                ## 📋 5. Master Executive Summary
                - **Core Verdict:** 2-sentence summary for Sir.
                - **Top 3 Action Items:** Immediate steps to execute today.
                """

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Sir ka command: {user_instruction}"}
                    ],
                    temperature=0.3
                )

                report = response.choices[0].message.content

                st.success("✅ Sir, Boardroom Executive Report Ready Hai!")
                
                st.markdown(f'<div class="report-box">{report}</div>', unsafe_allow_html=True)

                st.download_button(
                    label="📥 Download Executive Report (.txt)",
                    data=report,
                    file_name="Boardroom_Executive_Report.txt",
                    mime="text/plain"
                )

        except Exception as e:
            st.error(f"Error executing command: {str(e)}")
                
