import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#
#
#    HOW TO RUN IT 
#    IN CMD WRITE : 
#   C:\Users\xxxxx\xxxx>py -3.11 -m streamlit run app.py
#   app.py: The interactive Streamlit dashboard source code.
#
#
#
#

# Set page configuration
st.set_page_config(page_title="TAGM-Sim Explorer", layout="wide")

# --- STATE MANAGEMENT (Callbacks) ---
# These functions safely update the slider value when buttons are clicked
def set_baseline():
    st.session_state.alpha_val = 0.0

def set_tagm():
    st.session_state.alpha_val = 0.9

# Initialize the slider state if it's the first time loading
if "alpha_val" not in st.session_state:
    st.session_state.alpha_val = 0.9

st.title("TAGM-Sim: Spatiotemporal Matching Distribution")
st.markdown("Explore the 'Efficiency Trap' vs. 'Security Shift' by adjusting the parameters below.")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Simulation Parameters")

st.sidebar.markdown("**Presets:**")
# The on_click parameter safely calls the functions above
st.sidebar.button("Set to Baseline (α=0.0)", on_click=set_baseline)
st.sidebar.button("Set to TAGM Optimal (α=0.9)", on_click=set_tagm)

st.sidebar.markdown("---")

# The slider reads from and writes to the 'alpha_val' session state key
alpha = st.sidebar.slider("Trust Weight (α)", min_value=0.0, max_value=1.0, step=0.1, key="alpha_val")
t_min = st.sidebar.slider("Quarantine Threshold (T_min)", min_value=0.0, max_value=1.0, value=0.2, step=0.05)

# --- DATA SIMULATION ---
np.random.seed(42)
n_samples = 2000

# Interpolate cluster centers based on alpha
trust_mean = 0.2 + (alpha * 0.4)
qoe_mean = 0.95 - (alpha * 0.45)

# Generate data
trust_data = np.random.normal(loc=trust_mean, scale=0.1, size=n_samples)
qoe_data = np.random.normal(loc=qoe_mean, scale=0.1, size=n_samples)

# Clip to valid ranges [0, 1]
trust_data = np.clip(trust_data, 0.0, 1.0)
qoe_data = np.clip(qoe_data, 0.0, 1.0)

# Calculate Failures (Points below T_min)
failed_mask = trust_data < t_min
failure_rate = (np.sum(failed_mask) / n_samples) * 100

# --- METRICS UI ---
col1, col2, col3 = st.columns(3)
col1.metric("Average Trust", f"{np.mean(trust_data):.2f}")
col2.metric("Average QoE", f"{np.mean(qoe_data):.2f}")
col3.metric("Adversarial Exposure", f"{failure_rate:.1f}%", delta_color="inverse")

# --- PLOTTING ---
# Determine color scheme: Danger (Reds) for low alpha, Safe (Blues) for high alpha
is_safe = alpha >= 0.5
cmap = "Blues" if is_safe else "Reds"
color = "#0B3D91" if is_safe else "#B22222"
label_text = "Secure / Trusted Matches" if is_safe else "High Risk / Efficiency Trap"

fig, ax = plt.subplots(figsize=(8, 6))

# Draw KDE Cloud
sns.kdeplot(
    x=trust_data, y=qoe_data, 
    fill=True, cmap=cmap, levels=10, thresh=0.05, ax=ax
)

# Draw Contour Lines
sns.kdeplot(
    x=trust_data, y=qoe_data, 
    color=color, linewidths=0.5, levels=10, thresh=0.05, ax=ax
)

# Draw T_min Threshold
ax.axvline(x=t_min, color='black', linestyle='--', linewidth=2, label=f"T_min = {t_min}")

# Annotations
ax.text(
    0.95 if is_safe else 0.4, 0.4 if is_safe else 0.8, 
    label_text, 
    fontsize=12, ha='right' if is_safe else 'left',
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5')
)

# Formatting
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("Trust Score ($T_{ij}$)")
ax.set_ylabel("QoE Score ($Q_{ij}$)")
ax.set_title(f"Joint Distribution (α = {alpha:.1f})")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right")

# Render plot in Streamlit
st.pyplot(fig)
