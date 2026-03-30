import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="BJT CE Characteristics Lab", layout="wide")

st.title("🔬 Virtual Lab: BJT Common Emitter Characteristics")
st.markdown("### Explore Input and Output Characteristics of an NPN Transistor")

# --- Sidebar Controls ---
st.sidebar.header("Transistor Parameters")
beta = st.sidebar.slider("Current Gain (β)", 50, 200, 100)
v_be_sat = 0.7  # Standard Silicon base-emitter voltage

tab1, tab2 = st.tabs(["Input Characteristics", "Output Characteristics"])

# --- Tab 1: Input Characteristics (I_B vs V_BE) ---
with tab1:
    st.header("Input Characteristics")
    st.write(r"Plotting $I_B$ vs $V_{BE}$ for a constant $V_{CE}$")
    
    v_ce_const = st.sidebar.number_input("Constant V_CE (V)", 1.0, 10.0, 5.0)
    v_be = np.linspace(0, 1.0, 100)
    # Shockley-style approximation for base current
    i_b = np.where(v_be > v_be_sat, (v_be - v_be_sat) * 100, 0) # in microAmps

    fig1, ax1 = plt.subplots()
    ax1.plot(v_be, i_b, color='blue', lw=2)
    ax1.set_xlabel("Base-Emitter Voltage V_BE (V)")
    ax1.set_ylabel("Base Current I_B (μA)")
    ax1.grid(True, linestyle='--')
    st.pyplot(fig1)

# --- Tab 2: Output Characteristics (I_C vs V_CE) ---
with tab2:
    st.header("Output Characteristics")
    st.write(r"Plotting $I_C$ vs $V_{CE}$ for various $I_B$ values")
    
    # Simulate multiple curves for different I_B
    ib_values = [10, 20, 30, 40, 50] # in microAmps
    v_ce = np.linspace(0, 15, 100)
    
    fig2, ax2 = plt.subplots()
    for ib in ib_values:
        # Ic = beta * Ib (in mA) with a saturation region approximation
        ic = (beta * ib / 1000) * (1 - np.exp(-v_ce / 0.5)) 
        ax2.plot(v_ce, ic, label=f"I_B = {ib} μA")

    ax2.set_xlabel("Collector-Emitter Voltage V_CE (V)")
    ax2.set_ylabel("Collector Current I_C (mA)")
    ax2.legend()
    ax2.grid(True, linestyle='--')
    st.pyplot(fig2)
