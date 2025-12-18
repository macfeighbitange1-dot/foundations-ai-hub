import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# ================================
# 2_Architect_improved.py
# The Architect — Realistic Systems & Strategy Designer
# Upgrades:
# - Business-model–specific logic
# - Cost & ROI-aware resource allocation
# - Risk scoring and maturity assessment
# - Phased roadmap with effort weighting
# - Executive-ready outputs (still lightweight)
# ================================

st.set_page_config(page_title="🏗️ The Architect — Pro", layout="wide")

# Hide default Streamlit nav
st.markdown("<style>[data-testid='stSidebarNav'] {display: none;}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("💠 AI Ecosystem")
    st.page_link("hub.py", label="Home Dashboard", icon="🏠")
    st.markdown("---")
    st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
    st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
    st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
    st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")
    st.markdown("---")
    st.info("Foundations AI v1.1 — Architect Pro")

# ================================
# Page header
# ================================
st.title("🏗️ The Architect: Systems & Strategy")
st.write("Design a realistic AI operating model based on business context, scale, and execution risk.")

# ================================
# 1. Strategic Inputs
# ================================
with st.expander("🌐 Core Business Inputs", expanded=True):
    c1, c2, c3 = st.columns(3)

    with c1:
        biz_model = st.selectbox(
            "Business Model",
            ["B2B SaaS", "E-commerce", "Professional Services", "Manufacturing"]
        )
        company_stage = st.selectbox(
            "Company Stage",
            ["Idea / MVP", "Early Revenue", "Growth", "Enterprise"]
        )

    with c2:
        scale_target = st.select_slider(
            "Scaling Ambition",
            options=["Lean", "Balanced", "Aggressive"]
        )
        ai_maturity = st.select_slider(
            "AI Maturity",
            options=["None", "Experimental", "Operational", "AI-Native"]
        )

    with c3:
        annual_budget = st.number_input(
            "Annual Transformation Budget ($)",
            min_value=10_000,
            value=100_000,
            step=10_000
        )
        risk_tolerance = st.select_slider(
            "Risk Tolerance",
            options=["Low", "Medium", "High"]
        )

# ================================
# 2. Technology Stack Selection
# ================================
st.divider()
st.subheader("🧱 Core Technology Stack")

tech_stack = st.multiselect(
    "Select technologies to deploy",
    [
        "Generative AI",
        "Predictive Analytics",
        "Workflow Automation",
        "Computer Vision",
        "Data Warehouse / Lake",
        "Cloud Infrastructure"
    ],
    default=["Generative AI", "Cloud Infrastructure"]
)

# ================================
# 3. Architecture Intelligence Engine
# ================================

def architecture_engine(biz_model, stage, scale, maturity):
    if biz_model == "B2B SaaS":
        focus = "Product-led growth, retention intelligence, usage analytics"
        allocation = {"Product": 45, "Data": 25, "Growth": 20, "Ops": 10}
    elif biz_model == "E-commerce":
        focus = "Demand forecasting, pricing optimization, supply chain AI"
        allocation = {"Marketing": 30, "Inventory": 35, "Data": 20, "Ops": 15}
    elif biz_model == "Manufacturing":
        focus = "Predictive maintenance, quality automation, cost control"
        allocation = {"Operations": 40, "Engineering": 30, "Data": 20, "Admin": 10}
    else:
        focus = "Process automation, decision support, margin protection"
        allocation = {"Delivery": 35, "Ops": 30, "Sales": 20, "Admin": 15}

    maturity_gap = {
        "None": 3,
        "Experimental": 2,
        "Operational": 1,
        "AI-Native": 0
    }[maturity]

    return focus, allocation, maturity_gap

focus, allocation, maturity_gap = architecture_engine(
    biz_model, company_stage, scale_target, ai_maturity
)

# ================================
# 4. Cost & Risk Modeling
# ================================
st.divider()
st.subheader("📊 Feasibility & Risk Assessment")

execution_risk = min(100, maturity_gap * 25 + (30 if scale_target == "Aggressive" else 10))
expected_roi_band = "High" if execution_risk < 40 else "Medium" if execution_risk < 70 else "Low"

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Execution Risk", f"{execution_risk}%")
with c2:
    st.metric("Expected ROI Quality", expected_roi_band)
with c3:
    st.metric("Budget Intensity", f"${annual_budget:,.0f}")

if execution_risk > 70:
    st.warning("⚠️ High execution risk detected. Reduce scope or improve AI maturity before scaling.")
elif execution_risk > 40:
    st.info("⚖️ Moderate risk. Proceed with phased rollout and strong governance.")
else:
    st.success("✅ Risk profile acceptable for execution.")

# ================================
# 5. Resource Allocation Visualization
# ================================
st.divider()
st.subheader("🗺️ Resource Allocation Blueprint")

alloc_df = pd.DataFrame({
    "Department": allocation.keys(),
    "Allocation (%)": allocation.values()
})

alloc_chart = alt.Chart(alloc_df).mark_arc(innerRadius=60).encode(
    theta="Allocation (%):Q",
    color="Department:N",
    tooltip=["Department", "Allocation (%)"]
).properties(height=300)

st.altair_chart(alloc_chart, use_container_width=True)

# ================================
# 6. Phased Implementation Roadmap
# ================================
st.divider()
st.subheader("📅 Phased Implementation Roadmap")

roadmap = pd.DataFrame([
    {"Phase": "Foundation", "Start": 0, "End": 3, "Focus": "Data, infra, governance"},
    {"Phase": "Deployment", "Start": 3, "End": 7, "Focus": "Core AI use-cases"},
    {"Phase": "Optimization", "Start": 7, "End": 12, "Focus": "Automation & scale"}
])

roadmap_chart = alt.Chart(roadmap).mark_bar().encode(
    x=alt.X("Start:Q", title="Month"),
    x2="End:Q",
    y=alt.Y("Phase:N", sort=None),
    tooltip=["Phase", "Focus"]
).properties(height=220)

st.altair_chart(roadmap_chart, use_container_width=True)

# ================================
# 7. Executive Summary Output
# ================================
st.divider()
st.subheader("🧠 Architect Summary")

st.markdown(f"""
**Strategic Focus:** {focus}

**Primary Technologies:** {', '.join(tech_stack) if tech_stack else 'None selected'}

**Risk Outlook:** {execution_risk}% execution risk with **{expected_roi_band}** expected ROI quality.

**Guidance:** Prioritize disciplined rollout, strong data foundations, and measurable business KPIs.
""")

summary_payload = {
    "business_model": biz_model,
    "stage": company_stage,
    "scale": scale_target,
    "ai_maturity": ai_maturity,
    "risk": execution_risk,
    "allocation": allocation,
    "tech_stack": tech_stack
}

st.download_button(
    "Export Architecture Summary (JSON)",
    data=str(summary_payload),
    file_name="architecture_summary.json",
    mime="application/json"
)

# End of file
