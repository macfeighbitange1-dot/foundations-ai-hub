import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# -------------------------
# 4_Amplifier_pro_fixed.py
# Fully corrected and enhanced version
# Fixes: formatting errors, NaN handling, multi-line strings
# -------------------------

st.set_page_config(page_title="📈 The Amplifier — Pro", layout="wide")

# Safe number formatting function
def fmt_num(value, default="N/A"):
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return default
    return f"{value:,.2f}"

# 1. Sidebar: navigation + presets (with custom save/load)
st.markdown("<style>[data-testid='stSidebarNav'] {display: none;}</style>", unsafe_allow_html=True)
with st.sidebar:
    st.title("💠 AI Ecosystem")
    st.page_link("hub.py", label="Home Dashboard", icon="🏠")
    st.markdown("---")
    st.write("🌍 **Industry Modules**")
    st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
    st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
    st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
    st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")
    st.markdown("---")
    st.info("Foundations AI v1.0 — Amplifier Pro+")
    st.markdown("---")
    st.header("Presets & Options")

    # Initialize custom presets
    if 'custom_presets' not in st.session_state:
        st.session_state.custom_presets = {}

    preset_options = ["Startup (low spend)", "Growth (mid)", "Enterprise (high)", "Custom"] + list(st.session_state.custom_presets.keys())
    preset = st.selectbox("Quick presets", preset_options, index=1)

    # Load preset values
    if preset == "Startup (low spend)":
        preset_vals = dict(budget=500, reach=25000, aov=35, ctr=0.8, conv_rate=3.0)
    elif preset == "Growth (mid)":
        preset_vals = dict(budget=3000, reach=200000, aov=50, ctr=1.2, conv_rate=2.5)
    elif preset == "Enterprise (high)":
        preset_vals = dict(budget=20000, reach=1500000, aov=80, ctr=1.5, conv_rate=2.0)
    elif preset in st.session_state.custom_presets:
        preset_vals = st.session_state.custom_presets[preset]
    else:
        preset_vals = dict(budget=1000, reach=50000, aov=50, ctr=1.0, conv_rate=2.5)

    # Save custom preset
    with st.expander("💾 Save current as custom preset"):
        custom_name = st.text_input("Preset name")
        if st.button("Save custom preset") and custom_name:
            current_vals = {
                'budget': budget_a if 'budget_a' in locals() else preset_vals['budget'],
                'reach': reach_a if 'reach_a' in locals() else preset_vals['reach'],
                'aov': aov_a if 'aov_a' in locals() else preset_vals['aov'],
                'ctr': ctr_a if 'ctr_a' in locals() else preset_vals['ctr'],
                'conv_rate': conv_rate_a if 'conv_rate_a' in locals() else preset_vals['conv_rate']
            }
            st.session_state.custom_presets[custom_name] = current_vals
            st.success(f"Saved '{custom_name}'")

    st.caption("Tip: use 'Custom' to enter your own values. Toggle the 'Direct conversion' if measured from impressions.")

# 2. Page title
st.title("📈 The Amplifier — Pro+: ROI & Sensitivity Studio")
st.write("Build two scenarios, compare results with deltas, and run uncertainty analysis.")

# 3. Compute metrics (includes CPC)
@st.cache_data
def compute_metrics(budget, reach, aov, ctr_pct, conv_pct, conv_from='clicks'):
    reach = float(max(reach, 0))
    budget = float(max(budget, 0.0))
    aov = float(max(aov, 0.0))
    ctr = float(max(ctr_pct, 0.0)) / 100.0
    conv_rate = float(max(conv_pct, 0.0)) / 100.0

    clicks = reach * ctr
    conversions = (clicks * conv_rate) if conv_from == 'clicks' else (reach * conv_rate)
    revenue = conversions * aov
    roas = revenue / budget if budget > 0 else np.nan
    profit = revenue - budget
    cpm = (budget / reach) * 1000 if reach > 0 else np.nan
    cpc = budget / clicks if clicks > 0 else np.nan
    cpa = budget / conversions if conversions > 0 else np.nan
    margin = (profit / revenue) * 100 if revenue > 0 else np.nan

    return dict(
        budget=budget, reach=int(reach), aov=aov, ctr_pct=ctr_pct,
        clicks=int(round(clicks)), conv_rate_pct=conv_pct,
        conversions=int(round(conversions)), revenue=round(revenue, 2),
        roas=round(roas, 2) if not np.isnan(roas) else np.nan,
        profit=round(profit, 2), cpm=round(cpm, 2) if not np.isnan(cpm) else np.nan,
        cpc=round(cpc, 2) if not np.isnan(cpc) else np.nan,
        cpa=round(cpa, 2) if not np.isnan(cpa) else np.nan,
        margin_pct=round(margin, 2) if not np.isnan(margin) else np.nan
    )

# 4. Inputs
tab1, tab2 = st.tabs(["Scenario A (Baseline)", "Scenario B (Variant)"])

with tab1:
    st.subheader("Scenario A — Baseline")
    col1, col2, col3 = st.columns(3)
    with col1:
        budget_a = st.number_input("Ad Spend ($)", min_value=0.0, value=float(preset_vals['budget']), step=50.0, key='budget_a')
        aov_a = st.number_input("Average Order Value ($)", min_value=0.01, value=float(preset_vals['aov']), key='aov_a')
    with col2:
        reach_a = st.number_input("Reach (Impressions)", min_value=0, value=int(preset_vals['reach']), step=1000, key='reach_a')
        ctr_a = st.number_input("Click-through Rate (CTR %)", min_value=0.0, value=float(preset_vals['ctr']), step=0.1, key='ctr_a')
    with col3:
        conv_rate_a = st.number_input("Conversion Rate (%)", min_value=0.0, value=float(preset_vals['conv_rate']), step=0.1, key='conv_rate_a')
        conv_from_a = st.selectbox("Conversion base", ["clicks", "impressions"], index=0, key='conv_from_a')

with tab2:
    st.subheader("Scenario B — Variant")
    col1b, col2b, col3b = st.columns(3)
    with col1b:
        budget_b = st.number_input("Ad Spend ($)", min_value=0.0, value=budget_a, step=50.0, key='budget_b')
        aov_b = st.number_input("Average Order Value ($)", min_value=0.01, value=aov_a, key='aov_b')
    with col2b:
        reach_b = st.number_input("Reach (Impressions)", min_value=0, value=reach_a, step=1000, key='reach_b')
        ctr_b = st.number_input("Click-through Rate (CTR %)", min_value=0.0, value=ctr_a, step=0.1, key='ctr_b')
    with col3b:
        conv_rate_b = st.number_input("Conversion Rate (%)", min_value=0.0, value=conv_rate_a, step=0.1, key='conv_rate_b')
        conv_from_b = st.selectbox("Conversion base", ["clicks", "impressions"], index=0, key='conv_from_b')

st.divider()

# 5. Sensitivity controls
with st.expander("Uncertainty & Sensitivity (quick)"):
    st.write("Add +/- uncertainty to conversion rate to see revenue and ROAS swings.")
    sensitivity_scenario = st.radio("Apply sensitivity to", ["Scenario A", "Scenario B", "Both"], horizontal=True)
    conv_uncert_pct = st.slider("Conversion rate uncertainty ± (%)", 0.0, 100.0, 15.0, step=1.0)
    samples = st.number_input("Samples for sensitivity curve", min_value=10, max_value=200, value=50, step=10)

# 6. Compute
metrics_a = compute_metrics(budget_a, reach_a, aov_a, ctr_a, conv_rate_a, conv_from_a)
metrics_b = compute_metrics(budget_b, reach_b, aov_b, ctr_b, conv_rate_b, conv_from_b)

# 7. KPIs with deltas
st.subheader("Scenario comparison — Key KPIs")
colA, colDelta, colB = st.columns([2, 1, 2])

with colA:
    st.markdown("**Scenario A — Baseline**")
    st.metric("Conversions", f"{metrics_a['conversions']:,}")
    st.metric("Revenue", f"${fmt_num(metrics_a['revenue'])}")
    st.metric("ROAS", f"{fmt_num(metrics_a['roas'])}x")
    st.metric("CPA", f"${fmt_num(metrics_a['cpa'])}")
    st.caption(f"CPM: ${fmt_num(metrics_a['cpm'])} | CPC: ${fmt_num(metrics_a['cpc'])}")

with colDelta:
    st.markdown("**Δ (B vs A)**")
    rev_delta = ((metrics_b['revenue'] / metrics_a['revenue']) - 1) * 100 if metrics_a['revenue'] > 0 else np.nan
    roas_delta = metrics_b['roas'] - metrics_a['roas'] if not np.isnan(metrics_b['roas']) and not np.isnan(metrics_a['roas']) else np.nan
    profit_delta = metrics_b['profit'] - metrics_a['profit']
    conv_delta = ((metrics_b['conversions'] / metrics_a['conversions']) - 1) * 100 if metrics_a['conversions'] > 0 else np.nan

    st.metric("Revenue Δ", f"{rev_delta:+.1f}%" if not np.isnan(rev_delta) else "N/A")
    st.metric("ROAS Δ", f"{roas_delta:+.2f}x" if not np.isnan(roas_delta) else "N/A")
    st.metric("Profit Δ", f"${profit_delta:+,.0f}")
    st.metric("Conv. Δ", f"{conv_delta:+.1f}%" if not np.isnan(conv_delta) else "N/A")

with colB:
    st.markdown("**Scenario B — Variant**")
    st.metric("Conversions", f"{metrics_b['conversions']:,}")
    st.metric("Revenue", f"${fmt_num(metrics_b['revenue'])}")
    st.metric("ROAS", f"{fmt_num(metrics_b['roas'])}x")
    st.metric("CPA", f"${fmt_num(metrics_b['cpa'])}")
    st.caption(f"CPM: ${fmt_num(metrics_b['cpm'])} | CPC: ${fmt_num(metrics_b['cpc'])}")

# 8. Recommendations
st.subheader("Health check & quick recommendations")
def quick_reco(m):
    if np.isnan(m['roas']):
        return "No spend or invalid inputs"
    if m['roas'] < 1: return "⚠️ Negative ROI — optimize creative/targeting"
    if m['roas'] < 2: return "⚖️ Marginal — test before scaling"
    if m['roas'] < 4: return "✅ Healthy — consider scaling"
    return "🚀 Excellent — scale aggressively"

colr1, colr2 = st.columns(2)
with colr1:
    st.write("**Scenario A**: ")
    st.info(quick_reco(metrics_a))
with colr2:
    st.write("**Scenario B**: ")
    st.info(quick_reco(metrics_b))

# 9. Visual comparison
st.subheader("Visual comparison")
comp_df = pd.DataFrame([
    {**metrics_a, 'scenario': 'A (Baseline)'},
    {**metrics_b, 'scenario': 'B (Variant)'}
])
plot_df = comp_df.melt(id_vars='scenario', value_vars=['budget', 'revenue', 'profit', 'conversions'], var_name='metric', value_name='value')

chart = alt.Chart(plot_df).mark_bar().encode(
    x=alt.X('scenario:N', title='Scenario'),
    y=alt.Y('value:Q', title='Value'),
    color='metric:N',
    column=alt.Column('metric:N', header=alt.Header(labelAngle=0)),
    tooltip=['scenario', 'metric', 'value']
).properties(height=250)
st.altair_chart(chart, use_container_width=True)

# 10. Sensitivity chart
st.subheader("Sensitivity: conversion rate uncertainty")
sensi_dfs = []

def add_sensitivity(scenario, budget, reach, aov, ctr, conv_rate, conv_from):
    low = max(0.0, conv_rate * (1 - conv_uncert_pct/100.0))
    high = conv_rate * (1 + conv_uncert_pct/100.0)
    space = np.linspace(low, high, int(samples))
    for c in space:
        m = compute_metrics(budget, reach, aov, ctr, c, conv_from)
        sensi_dfs.append({'conv_rate_pct': c, 'revenue': m['revenue'], 'roas': m['roas'], 'scenario': scenario})

if "A" in sensitivity_scenario or "Both" in sensitivity_scenario:
    add_sensitivity('A', budget_a, reach_a, aov_a, ctr_a, conv_rate_a, conv_from_a)
if "B" in sensitivity_scenario or "Both" in sensitivity_scenario:
    add_sensitivity('B', budget_b, reach_b, aov_b, ctr_b, conv_rate_b, conv_from_b)

if sensi_dfs:
    sensi_df = pd.DataFrame(sensi_dfs)
    revenue_chart = alt.Chart(sensi_df).mark_line().encode(
        x='conv_rate_pct:Q', y='revenue:Q', color='scenario:N', tooltip=['scenario', 'conv_rate_pct', 'revenue', 'roas']
    )
    roas_chart = alt.Chart(sensi_df).mark_line(strokeDash=[5,5]).encode(
        x='conv_rate_pct:Q', y='roas:Q', color='scenario:N'
    )
    combined = alt.layer(revenue_chart, roas_chart).resolve_scale(y='independent').properties(
        width=800, height=400, title="Revenue (solid) | ROAS (dashed)"
    )
    st.altair_chart(combined, use_container_width=True)
    st.caption(f"Revenue range: ${fmt_num(sensi_df['revenue'].min())} → ${fmt_num(sensi_df['revenue'].max())}")

# 11. Export
st.subheader("Export / Share")
export_df = pd.DataFrame([
    dict(scenario='A (Baseline)', **metrics_a),
    dict(scenario='B (Variant)', **metrics_b),
])
export_df = export_df[['scenario','budget','reach','aov','ctr_pct','clicks','conv_rate_pct','conversions','revenue','roas','profit','cpm','cpc','cpa','margin_pct']]
csv = export_df.to_csv(index=False)
st.download_button("Download CSV", csv, "amplifier_scenarios.csv", "text/csv")

# 12. What-if
st.subheader("What-if quick test")
inc_pct = st.slider("Increase budget by % for Scenario A", 0, 500, 25)
new_budget = budget_a * (1 + inc_pct/100.0)
new_metrics = compute_metrics(new_budget, reach_a, aov_a, ctr_a, conv_rate_a, conv_from_a)
colw1, colw2 = st.columns(2)
with colw1:
    st.write(f"Budget: ${budget_a:,.0f} → ${new_budget:,.0f} (+{inc_pct}%)")
    st.metric("New ROAS", f"{fmt_num(new_metrics['roas'])}x")
    st.metric("New Revenue", f"${fmt_num(new_metrics['revenue'])}")
with colw2:
    st.metric("Delta Profit", f"${new_metrics['profit'] - metrics_a['profit']:+,.0f}")

# 13. Roadmap
st.markdown("---")
st.subheader("Roadmap & feature availability")
col1, col2 = st.columns(2)
with col1:
    st.success("✅ Enhanced Amplifier (Active)")
    st.markdown("""
    - Delta metrics & comparison
    - Custom preset saving
    - CPC/CPM display
    - Dual-axis sensitivity analysis
    - Scenario selector for sensitivity
    """)
with col2:
    st.warning("🔒 Advanced (Future)")
    st.markdown("""
    - LTV & repeat-purchase modeling
    - A/B significance testing
    - Pitch-ready exports
    """)
st.caption("Polished, robust, and production-ready. 🚀")
