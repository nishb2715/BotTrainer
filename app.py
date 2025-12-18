from src.utils import load_intent_metadata
import streamlit as st

from src.intent_classifier import classify_intent
from src.entity_extractor import extract_entities

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="BotTrainer – LLM-based NLU",
    layout="centered"
)

# ----------------- SESSION STATE -----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------- CUSTOM THEME (INFOSYS STYLE) -----------------
st.markdown("""
<style>

/* Layout padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0a2540, #102a44);
    color: white;
}

/* REMOVE ghost spacer blocks */
div[data-testid="stVerticalBlock"] > div:empty {
    display: none !important;
}

/* REMOVE markdown container background */
div[data-testid="stMarkdownContainer"] {
    background: transparent !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* REMOVE empty element containers */
div[data-testid="element-container"]:has(> div:empty) {
    display: none !important;
}

/* Input styling */
input {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 10px !important;
    padding: 12px !important;
}

/* Card styling */
.card {
    background-color: rgba(255, 255, 255, 0.12);
    padding: 20px;
    border-radius: 16px;
    margin-top: 20px;
}

/* Headers */
h1, h2, h3 {
    color: #e6f2ff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #081f36;
}

</style>
""", unsafe_allow_html=True)


# ----------------- SIDEBAR (BURGER MENU) -----------------
page = st.sidebar.radio(
    "Navigate",
    ["NLU Analyzer", "Interaction Log", "Intent List"]
)


# ----------------- HEADER -----------------
st.title("🤖 BotTrainer")
st.markdown(
    "<h4 style='color:#cfe3ff;'>LLM-Based NLU Model Trainer & Evaluator</h4>",
    unsafe_allow_html=True
)

# =========================
# PAGE 1: NLU ANALYZER
# =========================
if page == "NLU Analyzer":

    user_text = st.text_input(
        "Enter a message:",
        placeholder="e.g. Book a flight to Delhi tomorrow",
        label_visibility="visible"
    )

    if user_text:
        # Intent classification
        intent_result = classify_intent(user_text)
        intent = intent_result.get("intent", "unknown")

        # Entity extraction
        entities = extract_entities(user_text, intent)

        # Save interaction
        st.session_state.chat_history.append({
            "user": user_text,
            "intent": intent,
            "entities": entities
        })

        # Result card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🔍 NLU Result")
        st.write(f"**Intent:** `{intent}`")

        if entities:
            st.subheader("🧩 Extracted Entities")
            st.json(entities)
        else:
            st.write("No entities detected.")

        st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PAGE 2: INTERACTION LOG
# =========================
elif page == "Interaction Log":

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📜 Interaction Log")

    if not st.session_state.chat_history:
        st.write("No interactions yet.")
    else:
        for chat in reversed(st.session_state.chat_history):
            st.markdown(f"""
**User:** {chat['user']}  
**Intent:** `{chat['intent']}`  
**Entities:** `{chat['entities']}`  
---
""")

    st.markdown('</div>', unsafe_allow_html=True)


# =========================
# PAGE 3: INTENT LIST
# =========================
elif page == "Intent List":

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Supported Intents")

    intent_names, intent_entity_map = load_intent_metadata()

    for intent in sorted(intent_names):
        entities = intent_entity_map.get(intent, [])

        st.markdown(f"""
**🔹 Intent:** `{intent}`  
**Entities:** {entities if entities else "None"}  
---
""")

    st.markdown('</div>', unsafe_allow_html=True)


# ----------------- FOOTER -----------------
st.markdown("""
<hr>
<div style="text-align:center; color:#9bb7ff; font-size:14px;">
    BotTrainer • LLM-Powered NLU System <br>
    Designed for Infosys Springboard Internship • 2025
</div>
""", unsafe_allow_html=True)
