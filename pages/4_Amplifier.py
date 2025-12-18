import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# -------------------------
# 4_Amplifier_improved.py
# A significantly upgraded Streamlit ROI + performance marketing simulator
# Features:
# - Two scenario comparison (Baseline vs Variant)
# - CTR -> Clicks -> Conversions flow (or direct impressions->conversion option)
# - Metrics: CPM, CPC (estimated), Clicks, Conversions, CPA, Revenue, ROAS, Profit, Margin
# - Sensitivity band for conversion rate (uncertainty analysis)
# - Charts and downloadable CSV
# - Input presets, validation, and helpful tooltips
# -------------------------

st.set_page_config(page_title="📈 The Amplifier — Pro", layout="wide")

# 1. Sidebar: navigation + presets
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
    st.info("Foundations AI v1.0 — Amplifier Pro")
    st.markdown("---")

    st.header("Presets & Options")
    preset = st.selectbox("Quick presets", ["Startup (low spend)", "Growth (mid)", "Enterprise (high)", "Custom"], index=1)

    if preset == "Startup (low spend)":
        preset_vals = dict(budget=500, reach=25000, aov=35, ctr=0.8, conv_rate=3.0)
    elif preset == "Growth (mid)":
        preset_vals = dict(budget=3000, reach=200000, aov=50, ctr=1.2, conv_rate=2.5)
    elif preset == "Enterprise (high)":
        preset_vals = dict(budget=20000, reach=1500000, aov=80, ctr=1.5, conv_rate=2.0)
    else:
        preset_vals = dict(budget=1000, reach=50000, aov=50, ctr=1.0, conv_rate=2.5)

    st.write("\n")
    st.caption("Tip: use 'Custom' to enter your own values. Toggle the 'Direct conversion' checkbox if your conversion rate is measured against impressions (less common).")

# 2. Page title and description
st.title("📈 The Amplifier — Pro: ROI & Sensitivity Studio")
st.write("Build two scenarios, compare results, and run a quick uncertainty check to understand upside / downside ranges.")

# 3. Helper function to compute metrics
@st.cache_data
def compute_metrics(budget, reach, aov, ctr_pct, conv_pct, conv_from='clicks'):
    # conv_from: 'clicks' or 'impressions'
    reach = float(max(reach, 0))
    budget = float(max(budget, 0.0))
    aov = float(max(aov, 0.0))
    ctr = float(max(ctr_pct, 0.0)) / 100.0
    conv_rate = float(max(conv_pct, 0.0)) / 100.0

    clicks = reach * ctr
    if conv_from == 'clicks':
        conversions = clicks * conv_rate
    else:
        # conversion rate directly on impressions
        conversions = reach * conv_rate

    conversions = float(conversions)
    revenue = conversions * aov
    roas = revenue / budget if budget > 0 else np.nan
    profit = revenue - budget
    cpm = (budget / reach) * 1000 if reach > 0 else np.nan
    cpa = (budget / conversions) if conversions > 0 else np.nan
    avg_order_value = aov
    margin = (profit / revenue) * 100 if revenue > 0 else np.nan

    return dict(
        budget=budget,
        reach=int(reach),
        aov=aov,
        ctr_pct=ctr_pct,
        clicks=int(round(clicks)),
        conv_rate_pct=conv_pct,
        conversions=int(round(conversions)),
        revenue=round(revenue, 2),
        roas=round(roas, 2) if not np.isnan(roas) else np.nan,
        profit=round(profit, 2),
        cpm=round(cpm, 2) if not np.isnan(cpm) else np.nan,
        cpa=round(cpa, 2) if not np.isnan(cpa) else np.nan,
        margin_pct=round(margin, 2) if not np.isnan(margin) else np.nan
    )

# 4. Input area: two scenarios in tabs
tab1, tab2 = st.tabs(["Scenario A (Baseline)", "Scenario B (Variant)"])

with tab1:
    st.subheader("Scenario A — Baseline")
    col1, col2, col3 = st.columns(3)
    with col1:
        budget_a = st.number_input("Ad Spend ($)", min_value=0.0, value=float(preset_vals['budget']), step=50.0, key='budget_a')
        aov_a = st.number_input("Average Order Value ($)", min_value=0.01, value=float(preset_vals['aov']), key='aov_a', help="Average price per order")
    with col2:
        reach_a = st.number_input("Reach (Impressions)", min_value=0, value=int(preset_vals['reach']), step=1000, key='reach_a')
        ctr_a = st.number_input("Click-through Rate (CTR %)", min_value=0.0, value=float(preset_vals['ctr']), step=0.1, key='ctr_a', help="% of impressions that click")
    with col3:
        conv_rate_a = st.number_input("Conversion Rate (%)", min_value=0.0, value=float(preset_vals['conv_rate']), step=0.1, key='conv_rate_a', help="% of clicks that convert (or % of impressions if direct conversion selected)")
        conv_from_a = st.selectbox("Conversion base", ["clicks", "impressions"], index=0, key='conv_from_a', help="Choose whether conversion rate is measured from clicks or impressions")

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

# 5. Uncertainty / sensitivity controls
with st.expander("Uncertainty & Sensitivity (quick)"):
    st.write("Add +/- uncertainty to conversion rate to see how revenue and ROAS might swing. This provides a simple downside/upside band.")
    conv_uncert_pct = st.slider("Conversion rate uncertainty ± (%)", 0.0, 100.0, 15.0, step=1.0)
    samples = st.number_input("Samples for sensitivity curve", min_value=10, max_value=200, value=50, step=10)

# 6. Compute metrics (cached)
metrics_a = compute_metrics(budget_a, reach_a, aov_a, ctr_a, conv_rate_a, conv_from=conv_from_a)
metrics_b = compute_metrics(budget_b, reach_b, aov_b, ctr_b, conv_rate_b, conv_from=conv_from_b)

# 7. Display key KPIs in columns
st.subheader("Scenario comparison — Key KPIs")
colA, colB = st.columns(2)
with colA:
    st.markdown("**Scenario A — Baseline**")
    st.metric("Conversions", f"{metrics_a['conversions']}")
    st.metric("Projected Revenue", f"${metrics_a['revenue']:,}")
    st.metric("ROAS", f"{metrics_a['roas']}x")
    st.metric("CPA", f"${metrics_a['cpa']}")
with colB:
    st.markdown("**Scenario B — Variant**")
    st.metric("Conversions", f"{metrics_b['conversions']}")
    st.metric("Projected Revenue", f"${metrics_b['revenue']:,}")
    st.metric("ROAS", f"{metrics_b['roas']}x")
    st.metric("CPA", f"${metrics_b['cpa']}")

# 8. Health & recommendations
st.subheader("Health check & quick recommendations")

def quick_reco(m):
    if np.isnan(m['roas']):
        return "No spend or invalid inputs"
    if m['roas'] < 1:
        return "⚠️ Negative ROI — optimize creative, targeting, or increase AOV / decrease CPC"
    if m['roas'] < 2:
        return "⚖️ Marginal — test improvements before scaling"
    if m['roas'] < 4:
        return "✅ Healthy — consider controlled scale"
    return "🚀 Excellent — strong candidate for aggressive scaling"

colr1, colr2 = st.columns(2)
with colr1:
    st.write("**Scenario A**: ")
    st.info(quick_reco(metrics_a))
with colr2:
    st.write("**Scenario B**: ")
    st.info(quick_reco(metrics_b))

# 9. Chart: compare revenue, spend, profit
st.subheader("Visual comparison")
comp_df = pd.DataFrame([
    {**metrics_a, 'scenario': 'A'},
    {**metrics_b, 'scenario': 'B'}
])
# keep only columns we want to plot
plot_df = comp_df[['scenario', 'budget', 'revenue', 'profit', 'conversions']]
plot_df = plot_df.melt(id_vars='scenario', var_name='metric', value_name='value')

chart = alt.Chart(plot_df).mark_bar().encode(
    x=alt.X('scenario:N', title='Scenario'),
    y=alt.Y('value:Q', title='Value'),
    color='metric:N',
    column=alt.Column('metric:N', header=alt.Header(labelAngle=0, labelAlign='left'))
).properties(height=200)

st.altair_chart(chart, use_container_width=True)

# 10. Sensitivity analysis on conversion rate
st.subheader("Sensitivity: conversion rate uncertainty")
conv_base_a = conv_rate_a
low = max(0.0, conv_base_a * (1 - conv_uncert_pct/100.0))
high = conv_base_a * (1 + conv_uncert_pct/100.0)
conv_space = np.linspace(low, high, int(samples))

sensi_rows = []
for c in conv_space:
    m = compute_metrics(budget_a, reach_a, aov_a, ctr_a, c, conv_from=conv_from_a)
    sensi_rows.append({'conv_rate_pct': c, 'revenue': m['revenue'], 'roas': m['roas']})

sensi_df = pd.DataFrame(sensi_rows)
line = alt.Chart(sensi_df).mark_line().encode(x='conv_rate_pct', y='revenue')
st.altair_chart(line.properties(width=800, height=300), use_container_width=True)
st.caption(f"Range: conv_rate {low:.2f}% → {high:.2f}% produces revenue ${sensi_df['revenue'].min():,.2f} → ${sensi_df['revenue'].max():,.2f}")

# 11. Export results
st.subheader("Export / Share")
export_df = pd.DataFrame([
    dict(scenario='A', **metrics_a),
    dict(scenario='B', **metrics_b)
])
# flatten some nested types
export_df = export_df[['scenario','budget','reach','aov','ctr_pct','clicks','conv_rate_pct','conversions','revenue','roas','profit','cpm','cpa','margin_pct']]

csv = export_df.to_csv(index=False)
st.download_button("Download CSV of scenarios", csv, file_name='amplifier_scenarios.csv', mime='text/csv')

# 12. Small interactive playground: "What if I increase budget by X%"
st.subheader("What-if quick test")
inc_pct = st.slider("Increase budget by % for Scenario A (simulate)", 0, 500, 25)
new_budget = budget_a * (1 + inc_pct/100.0)
new_metrics = compute_metrics(new_budget, reach_a, aov_a, ctr_a, conv_rate_a, conv_from=conv_from_a)
colw1, colw2 = st.columns(2)
with colw1:
    st.write(f"Budget: ${budget_a:,} → ${int(new_budget):,} (+{inc_pct}%)")
    st.metric("New ROAS", f"{new_metrics['roas']}x")
    st.metric("New Revenue", f"${new_metrics['revenue']:,}")
with colw2:
    st.metric("Delta Profit", f"${new_metrics['profit'] - metrics_a['profit']:,}")

# 13. Footer / next steps
st.markdown("---")
st.write("Need more? I can: \n- add lifetime value (LTV) and repeat purchase modelling, \n- wire this to a campaign data source, or \n- create an A/B test simulator with statistical significance calculations.")

# End of file
