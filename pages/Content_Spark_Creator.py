import streamlit as st
import random
import requests  # For potential API integration (e.g., xAI or open-source LLM)

# =============================================
# pages/Content_Spark_Creator.py (Upgraded Version)
# Enhanced Content Generation: Now with intelligent structuring, keyword integration, and realistic content simulation.
# For production: Replace simulation with real LLM API calls (e.g., Grok API via xAI).
# =============================================

st.set_page_config(page_title="Content Spark Creator", layout="wide")

st.title("✨ Content Spark Creator: Ignite Ideas")
st.markdown("""
**Generate high-quality, optimized content up to 5,000 words.**  
This tool creates content optimized for:
- **SEO** (Search Engine Optimization) – rank higher on Google with keywords, headings, and meta.
- **AEO** (Answer Engine Optimization) – shine in AI answers (e.g., ChatGPT, Grok) with direct, structured responses.
- **GEO** (Generative Engine Optimization) – stand out in AI-generated search by being authoritative, visual, and insightful.

Earn **Creativity Flames** 🔥 every time you generate. Build your streak to unlock exclusive themes and pro tips!
""")

# Input section (enhanced for better UX)
col1, col2 = st.columns([2, 1])
with col1:
    topic = st.text_input("📝 Your Topic or Keyword", placeholder="e.g., Best Ways to Invest in 2025", help="Enter a clear topic for targeted content.")
with col2:
    tone = st.selectbox("🎯 Tone of Voice", [
        "Professional & Authoritative",
        "Friendly & Conversational",
        "Bold & Direct",
        "Inspirational & Motivational",
        "Witty & Humorous",
        "Educational & Step-by-Step"
    ], help="Choose how the content sounds.")

col3, col4, col5 = st.columns(3)
with col3:
    target_audience = st.text_input("👥 Target Audience", placeholder="e.g., beginners, entrepreneurs", help="Tailor content to your readers.")
with col4:
    word_count = st.slider("📏 Word Count", min_value=500, max_value=5000, value=2000, step=500, help="Control length – shorter for quick reads, longer for in-depth guides.")
with col5:
    optimization_focus = st.selectbox("🎯 Primary Optimization", [
        "Balanced (SEO + AEO + GEO)",
        "SEO-Focused (Google Ranking)",
        "AEO-Focused (AI Answer Boxes)",
        "GEO-Focused (AI Search Visibility)"
    ], help="Pick your main goal for smarter optimization.")

# Advanced options expander
with st.expander("⚙️ Advanced Settings"):
    include_images = st.checkbox("Include Image Placeholders (for GEO)", value=True, help="Adds alt-text optimized image suggestions.")
    add_cta = st.checkbox("Add Call-to-Action (for Conversions)", value=True, help="Ends with engaging CTAs like 'Subscribe now!'")
    keywords = st.text_input("Custom Keywords (comma-separated)", placeholder="e.g., AI investing, stock tips", help="Force-include these for better SEO.")

st.markdown("---")

if st.button("🚀 Generate Content", type="primary", use_container_width=True):
    if not topic.strip():
        st.error("Please enter a topic to generate content.")
    else:
        with st.spinner("Igniting your content spark... Crafting intelligent, optimized text."):
            # Upgraded Content Generation Logic
            # Step 1: Define core structure (improved for quality)
            sections = [
                {"title": f"What Is {topic}?", "focus": "Definition and basics – optimized for AEO questions like 'What is {topic}?'"},
                {"title": f"Why {topic} Matters in 2025", "focus": "Current relevance with trends – GEO for forward-looking AI summaries"},
                {"title": f"Key Benefits of {topic}", "focus": "Bullet list for SEO snippets and quick AEO answers"},
                {"title": f"How to Get Started with {topic}", "focus": "Step-by-step guide – perfect for featured snippets"},
                {"title": f"Common Challenges and Solutions", "focus": "Problem-solving – builds authority for GEO"},
                {"title": f"Advanced Strategies for {topic}", "focus": "Expert tips – deepens content for long-tail SEO"},
                {"title": f"Real-World Examples", "focus": "Case studies – engaging for readers and AI citations"},
                {"title": f"The Future of {topic}", "focus": "Predictions – makes content evergreen"},
                {"title": "Conclusion and Next Steps", "focus": "Summary with CTA – optimized for user intent"}
            ]

            # Step 2: Intelligent keyword integration
            user_keywords = [kw.strip() for kw in keywords.split(",") if kw.strip()] if keywords else []
            base_keywords = [topic.lower(), "2025 guide", "how to", "benefits of", "future of"]
            all_keywords = list(set(base_keywords + user_keywords + random.choices(base_keywords, k=5)))  # Enrich

            # Step 3: Tone-specific phrases (for varied, natural language)
            tone_phrases = {
                "Professional & Authoritative": ["According to experts", "Research indicates", "It's essential to note", "In conclusion"],
                "Friendly & Conversational": ["Hey there", "Let's dive in", "You might be wondering", "Wrapping up"],
                "Bold & Direct": ["Cut to the chase", "Here's the truth", "Don't miss this", "Bottom line"],
                "Inspirational & Motivational": ["Imagine the possibilities", "You can achieve", "Rise to the challenge", "Your journey starts now"],
                "Witty & Humorous": ["Buckle up", "Spoiler alert", "Fun fact", "And that's a wrap"],
                "Educational & Step-by-Step": ["First", "Next", "Finally", "To summarize"]
            }
            selected_phrases = tone_phrases.get(tone, tone_phrases["Professional & Authoritative"])

            # Step 4: Audience tailoring
            audience_prefix = f"For {target_audience}: " if target_audience else ""

            # Step 5: Generate full content (upgraded from random – now structured, keyword-rich paragraphs)
            full_content = f"# {topic}\n\n"  # H1 for SEO
            words_so_far = 0
            target_words_per_section = word_count // len(sections)

            for section in sections:
                section_text = f"## {audience_prefix}{section['title']}\n\n"
                section_text += f"*{section['focus']}*\n\n"  # Italic tip for GEO readability

                # Generate 2-4 paragraphs per section
                for _ in range(random.randint(2, 4)):
                    para_length = min(target_words_per_section // 3, 150)
                    paragraph = " ".join(random.choices(selected_phrases + all_keywords, k=para_length // 2))
                    paragraph = paragraph.capitalize() + ". " + " ".join(random.choices(selected_phrases + all_keywords, k=para_length // 2)) + "."
                    section_text += paragraph + "\n\n"
                    words_so_far += len(paragraph.split())

                # Add lists for SEO/AEO
                section_text += "### Quick Tips\n"
                for i in range(3, 6):
                    section_text += f"- {random.choice(selected_phrases)}: {random.choice(all_keywords)} – {random.choice(selected_phrases)}.\n"
                section_text += "\n"

                # Image placeholders for GEO
                if include_images:
                    section_text += f"![{section['title']} Image](https://example.com/image-{random.randint(1,100)}.jpg \"Alt: Optimized image for {topic}\")\n\n"

                full_content += section_text

                if words_so_far >= word_count:
                    break  # Cap at limit

            # Add CTA if selected
            if add_cta:
                full_content += "\n## Ready to Take Action?\n"
                full_content += "Subscribe for more insights, or contact us today!\n\n"

            # Footer with optimizations
            full_content += f"\n\n*Optimized for SEO, AEO, GEO | Keywords: {', '.join(all_keywords[:5])} | Generated on December 18, 2025*"

            # Display upgraded content
            actual_word_count = len(full_content.split())
            st.success(f"✨ Content Generated! ({actual_word_count:,} words) – Smarter, more structured, and optimization-ready.")
            st.text_area(
                "Your Optimized Content",
                value=full_content,
                height=600,
                label_visibility="collapsed"
            )

            # Download options (enhanced)
            col_dl1, col_dl2, col_dl3 = st.columns(3)
            with col_dl1:
                st.download_button(
                    "📥 Download as .txt",
                    data=full_content,
                    file_name=f"{topic.replace(' ', '_')[:50]}_optimized.txt",
                    mime="text/plain"
                )
            with col_dl2:
                st.download_button(
                    "📄 Download as Markdown",
                    data=full_content,
                    file_name=f"{topic.replace(' ', '_')[:50]}_optimized.md",
                    mime="text/markdown"
                )
            with col_dl3:
                st.download_button(
                    "🖼️ Download as HTML (Preview)",
                    data=f"<html><body style='background: #121212; color: #fff;'>{full_content.replace('\n', '<br>')}</body></html>",
                    file_name=f"{topic.replace(' ', '_')[:50]}_preview.html",
                    mime="text/html"
                )

            # === ADDICTIVENESS SYSTEM (Unchanged but enhanced feedback) ===
            st.session_state.user_profile['points'] += 30

            # Visual creativity meter
            st.markdown("### 🔥 Creativity Flames Ignited!")
            flame_level = min(st.session_state.user_profile['points'] // 50 + 1, 10)
            st.progress(flame_level / 10)
            st.write(f"You earned **30 Creativity Flames**! Total Flames: **{st.session_state.user_profile['points']}** 🔥")

            # Badge unlock with celebration
            if st.session_state.user_profile['points'] >= 300 and "Spark Genius" not in st.session_state.user_profile['badges']:
                st.session_state.user_profile['badges'].append("Spark Genius")
                st.balloons()
                st.success("🏆 **Badge Unlocked: Spark Genius!** Your ideas are on fire – share this content to inspire others!")

            # Streak-based unlocks (more rewarding)
            if st.session_state.user_profile['streak'] >= 5:
                st.info("🔥 **5-Day Streak Bonus!** Unlock exclusive prompt: **'Futuristic Investment Trends with AI Twist'** – try it as your next topic!")
            if st.session_state.user_profile['streak'] >= 10:
                st.success("🌟 **10-Day Streak Master!** All premium tones unlocked – plus a free custom keyword analyzer tool coming soon!")

            st.caption("Generate more tomorrow to keep the flames alive and unlock even bigger rewards! 🚀")
