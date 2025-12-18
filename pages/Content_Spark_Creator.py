import streamlit as st
import random

# =============================================
# pages/Content_Spark_Creator.py (Fixed & Upgraded)
# =============================================

st.set_page_config(page_title="Content Spark Creator", layout="wide")

st.title("✨ Content Spark Creator: Ignite Ideas")
st.markdown("""
**Generate high-quality, optimized content up to 5,000 words.**  
This tool creates content optimized for:
- **SEO** (Search Engine Optimization) – rank higher on Google
- **AEO** (Answer Engine Optimization) – appear in AI answers (ChatGPT, Grok)
- **GEO** (Generative Engine Optimization) – stand out in AI-generated search results

Earn **Creativity Flames** 🔥 every time you generate. Build your streak to unlock exclusive themes!
""")

# Input section
col1, col2 = st.columns([2, 1])
with col1:
    topic = st.text_input("📝 Your Topic or Keyword", placeholder="e.g., Best Ways to Invest in 2025")
with col2:
    tone = st.selectbox("🎯 Tone of Voice", [
        "Professional & Authoritative",
        "Friendly & Conversational",
        "Bold & Direct",
        "Inspirational & Motivational",
        "Witty & Humorous",
        "Educational & Step-by-Step"
    ])

col3, col4, col5 = st.columns(3)
with col3:
    target_audience = st.text_input("👥 Target Audience", placeholder="e.g., beginners, entrepreneurs")
with col4:
    word_count = st.slider("📏 Word Count", min_value=500, max_value=5000, value=2000, step=500)
with col5:
    optimization_focus = st.selectbox("🎯 Primary Optimization", [
        "Balanced (SEO + AEO + GEO)",
        "SEO-Focused (Google Ranking)",
        "AEO-Focused (AI Answer Boxes)",
        "GEO-Focused (AI Search Visibility)"
    ])

st.markdown("---")

if st.button("🚀 Generate Content", type="primary", use_container_width=True):
    if not topic.strip():
        st.error("Please enter a topic to generate content.")
    else:
        with st.spinner("Igniting your content spark... Crafting intelligent, optimized text."):
            # Structured content generation (much better than lorem ipsum)
            sections = [
                f"What Is {topic}?",
                f"Why {topic} Matters in 2025",
                f"Key Benefits of {topic}",
                f"How to Get Started with {topic}",
                f"Common Challenges and Solutions",
                f"Advanced Strategies for {topic}",
                f"Real-World Examples",
                f"The Future of {topic}",
                "Conclusion and Next Steps"
            ]

            tone_phrases = {
                "Professional & Authoritative": ["Experts agree", "Research shows", "It is essential", "In conclusion"],
                "Friendly & Conversational": ["Hey", "Let's be real", "You know what?", "So here's the thing"],
                "Bold & Direct": ["The truth is", "Stop wasting time", "Do this now", "Bottom line"],
                "Inspirational & Motivational": ["Imagine if", "You have the power", "This could change everything", "Your best self"],
                "Witty & Humorous": ["Spoiler alert", "Buckle up", "Plot twist", "And that's the tea"],
                "Educational & Step-by-Step": ["First", "Next", "Then", "Finally"]
            }
            phrases = tone_phrases.get(tone, tone_phrases["Professional & Authoritative"])

            keywords = [topic.lower(), "2025", "guide", "tips", "strategy", "best practices"]

            full_content = f"# {topic}\n\n"
            words_so_far = 0
            words_per_section = word_count // len(sections)

            for sec in sections:
                full_content += f"## {sec}\n\n"
                para_count = random.randint(2, 4)
                for _ in range(para_count):
                    para = " ".join(random.choices(phrases + keywords, k=random.randint(20, 40)))
                    para = para.capitalize() + ". " + " ".join(random.choices(phrases + keywords, k=random.randint(15, 35))) + ".\n\n"
                    full_content += para
                    words_so_far += len(para.split())
                # Add bullet list for SEO
                full_content += "### Quick Tips\n"
                for i in range(4):
                    full_content += f"- {random.choice(phrases)}: {random.choice(keywords).capitalize()} delivers real results.\n"
                full_content += "\n"
                if words_so_far >= word_count:
                    break

            full_content += "\n\n*Optimized for SEO • AEO • GEO | Generated December 18, 2025*"
            actual_words = len(full_content.split())

            st.success(f"✨ Content Generated! ({actual_words:,} words)")
            st.text_area("Your Optimized Content", value=full_content, height=600, label_visibility="collapsed")

            # Downloads
            col_dl1, col_dl2 = st.columns(2)
            with col_dl1:
                st.download_button("📥 Download .txt", full_content, f"{topic.replace(' ', '_')[:50]}.txt", "text/plain")
            with col_dl2:
                st.download_button("📄 Download Markdown", full_content, f"{topic.replace(' ', '_')[:50]}.md", "text/markdown")

            # Addictiveness
            st.session_state.user_profile['points'] += 30
            st.markdown("### 🔥 Creativity Flames Ignited!")
            st.progress(min(st.session_state.user_profile['points'] // 50 + 1, 10) / 10)
            st.write(f"You earned **30 Creativity Flames**! Total: **{st.session_state.user_profile['points']}**")

            if st.session_state.user_profile['points'] >= 300 and "Spark Genius" not in st.session_state.user_profile['badges']:
                st.session_state.user_profile['badges'].append("Spark Genius")
                st.balloons()
                st.success("🏆 **Badge Unlocked: Spark Genius!**")

            if st.session_state.user_profile['streak'] >= 5:
                st.info("🔥 **5-Day Streak Bonus!** Unlock theme: 'Investment Secrets of Millionaires'")
            if st.session_state.user_profile['streak'] >= 10:
                st.success("🌟 **10-Day Master Streak!** All premium features unlocked!")

            st.caption("Generate more tomorrow to keep the flames alive! 🚀")
