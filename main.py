import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Board of Directors", layout="wide")
st.title("Autonomous Executive Boardroom")
st.caption("Aapka AI C-Suite Dashboard — CEO, COO, CFO, CMO Ready.")

# Sidebar API Key
st.sidebar.header("Configuration")
groq_api_key = st.sidebar.text_input(
    "Groq API Key (Free Token):", 
    type="password",
    value="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"
)

# User Input
user_instruction = st.text_area(
    "Sir, aapka kya aadesh hai? (Enter your project/business command):",
    placeholder="E.g., Naya business shuru karna hai / Factory setup karni hai...",
    height=120
)

if st.button("Execute Command"):
    if not groq_api_key:
        st.error("Sir, kripya pehle sidebar mein Groq API key enter karein.")
    elif not user_instruction.strip():
        st.warning("Sir, kripya koi command type karein.")
    else:
        try:
            with st.spinner("Sir, Board of Directors (CEO, COO, CFO, CMO) aapke project par kaam kar rahe hain..."):
                client = Groq(api_key=groq_api_key)

                system_prompt = """
                Aap ek elite Autonomous AI Board of Directors hain jo milkar user ko 'Sir' bolkar report present karte hain.
                Har command par aapko 4 C-Level officers ki complete, structured report deliver karni hai:

                1. 👑 Chief Executive Officer (CEO): Project Vision, Strategic Scope, Risk Audit.
                2. ⚙️ Chief Operating Officer (COO): Ground Execution Steps, Supply Chain/Operations, Timeline.
                3. 💰 Chief Financial Officer (CFO): Budget Breakdown, Initial Capital, Revenue & Profit Estimation.
                4. 📈 Chief Marketing Officer (CMO): Target Market, Branding, Distribution Strategy.
                5. 📋 Master Summary for Sir: Key Takeaways & First 3 Immediate Action Items.
                """

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Sir ka command: {user_instruction}"}
                    ],
                    temperature=0.3
                )

                st.success("Sir, Boardroom Master Report Ready Hai:")
                st.markdown(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {str(e)}")
              
