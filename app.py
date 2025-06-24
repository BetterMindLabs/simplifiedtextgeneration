import streamlit as st
import google.generativeai as genai

# === Gemini API Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === UI ===
st.set_page_config(page_title="🧾 Simplified Text Generator")
st.title("🧾 Simplified Text Generator")
st.write("Paste any complex text and get a version that’s easier to understand, without losing the meaning.")

# === Input Field ===
input_text = st.text_area("📚 Complex Text", height=250, placeholder="e.g. The proliferation of digital ecosystems has fundamentally transformed how societies communicate and function...")

# === Generate Button ===
if st.button("Simplify"):
    if input_text.strip():
        with st.spinner("Simplifying text..."):
            prompt = f"""
Simplify the following passage. Make it easy to understand for a 12-year-old while keeping the original meaning. Avoid childish language. Keep sentences short and clear.

Text:
{input_text}
"""
            response = model.generate_content(prompt)
            simplified = response.text.strip()

            st.subheader("✅ Simplified Version")
            st.text_area("Result", simplified, height=250)
    else:
        st.warning("Please enter some text to simplify.")
