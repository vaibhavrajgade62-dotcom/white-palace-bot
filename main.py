import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="AI Boardroom | Executive Suite",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Light Theme CSS (White Background, Black Text)
st.markdown("""
<style>
    /* Light Theme Variables */
    :root {
        --bg-main: #FFFFFF;
        --bg-sidebar: #F4F4F4;
        --text-main: #000000;
        --orange-primary: #FF6600;
        --border-color: #E0E0E0;
    }

    /* Main Background */
    .stApp {
        background-color: var(--bg-main) !important;
        color: var(--text-main) !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: var(--bg-sidebar) !important;
    }

    /* Custom Header */
    .header-container {
        display: flex;
        align-items: center;
        gap: 20px;
        background: #FFFFFF;
        padding: 20px;
        border-bottom: 3px solid #FF6600;
        margin-bottom: 25px;
    }

    .logo-badge {
        width: 60px;
        height: 60px;
        background-color: #FF6600;
        color: white;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
    }

    .header-title {
        font-size: 28px;
        font-weight: 900;
        color: #000000;
        margin: 0;
    }

    /* Input & Buttons */
    .stButton>button {
        background-color: #FF6600 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
    }

    .stTextArea textarea {
        background-color: #FAFAFA !important;
        color: #000000 !important;
        border: 1px solid #CCCCCC !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. UI Elements
st.markdown("""
<div class="header-container">
    <div class="logo-badge">👑</div>
    <div>
        <div class="header-title">AI BOARDROOM EXECUTIVE SUITE</div>
        <div>Autonomous C-Level Strategy Engine</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Sidebar Configuration
st.sidebar.markdown("### ⚙️ System Settings")
groq_api_key = st.sidebar.text_input("Groq API Key:", type="password", value="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")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Quick Presets")
preset_text = ""
if st.sidebar.button("🚀 Naya Brand / Business Start"):
    preset_text = "Naya Premium Perfume Brand launch karna hai India mein. Initial strategy, budget, supply chain aur marketing plan dijiye."
elif st.sidebar.button("🏭 Factory & Production Unit"):
    preset_text = "Automatic Packaging Factory setup karni hai. Equipment, ROI time, operational execution aur risk audit bataiye."

# 5. User Instruction
st.subheader("🎯 Sir, aapka kya aadesh hai?")
user_instruction = st.text_area("Apna Command yahan enter karein:", value=preset_text, height=110)

# 6. Execution
if st.button("🔥 Execute Boardroom Command"):
    if not groq_api_key:
        st.error("Sir, kripya sidebar mein API key enter karein.")
    else:
        with st.spinner("⚡ Processing..."):
            client = Groq(api_key=groq_api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Sir ka command: {user_instruction}"}],
                temperature=0.3
            )
            report = response.choices[0].message.content
            
            st.success("✅ Report Ready!")
            st.markdown(report)
            st.download_button("📥 Download Report (.txt)", report, file_name="Report.txt")
            
