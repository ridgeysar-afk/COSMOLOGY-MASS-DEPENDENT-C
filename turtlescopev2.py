"""
TurtleScope v2.1 — Fractal Ladder + Biology
Run with: streamlit run app_v2_1.py

Dependencies (install once):
    pip install streamlit sympy numpy matplotlib
"""

import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Core setup
# -------------------------
st.set_page_config(page_title="TurtleScope v2.1", page_icon="🐢", layout="wide")
st.title("🐢 TurtleScope v2.1 — Fractal Ladder")
st.caption("Physics ↔ Chemistry ↔ Biology ↔ Mind")

alpha = sp.symbols('alpha', positive=True)
M = sp.symbols('M', positive=True)
c = alpha
T_GUT = alpha
H = alpha**2
tau_p = (alpha/1e-3)**4 * 1e32
P_reset = 1 - sp.exp(-alpha)

with st.sidebar:
    st.header("Universe Settings")
    alpha_val = st.number_input("α (alpha)", min_value=1e-6, max_value=1.0,
                                value=1e-3, format="%.6f")
    st.caption("Tip: α = √M → c = α")

# -------------------------
# Tabs
# -------------------------
tab_phys, tab_chem, tab_bio, tab_mind = st.tabs(
    ["Physics Ladder", "Chemistry Ladder", "Biology Ladder", "Mind Ladder"]
)

# -------------------------
# Physics Ladder
# -------------------------
with tab_phys:
    st.subheader("Physics Ladder (Q → A)")
    query = st.text_input("Your question", placeholder="e.g., Why is gravity 1/r² here?")

    def explain(q):
        ql = q.lower().strip()
        if not ql:
            return "Ask me anything about light, gravity, unification, PBHs, or constants."
        if "light" in ql or "c " in ql or ql == "c":
            return f"In Turtle-Verse, c = α. With α={alpha_val:g}, c≈{alpha_val:g} (natural units)."
        if "gravity" in ql:
            return "Gravity emerges from entanglement entropy gradients (Ryu–Takayanagi). Effective 1/r² at macroscales."
        if "gut" in ql or "unification" in ql:
            return f"GUT scale tracks α: T_GUT = α. With α={alpha_val:g}, T_GUT≈{alpha_val:g}."
        if "proton" in ql and "decay" in ql:
            tp = float(tau_p.subs({alpha:alpha_val}))
            return f"Proton lifetime ~ τ_p=(α/1e-3)^4·1e32 y. For α={alpha_val:g}, τ_p≈{tp:.3e} years."
        if "reset" in ql or "cycle" in ql:
            pres = float(P_reset.subs({alpha:alpha_val}))
            return f"Reset probability per cycle: P=1−exp(−α). For α={alpha_val:g}, P≈{pres:.6f}."
        if "cmb" in ql:
            return "CMB near-isotropy follows entropy homogenization; anomalies map to local δα/α noise."
        if "pbh" in ql or "black hole" in ql:
            return "PBHs act as entropic seeds; matter/antimatter 50/50 enables rare reset cycles."
        return "Baseline answer: constants and behavior are set by α=√M."

    if st.button("Explain"):
        st.markdown("### Explanation")
        st.write(explain(query))

    st.markdown("### Core Relations")
    st.latex(r"c=\alpha,\quad T_{\mathrm{GUT}}=\alpha,\quad H=\alpha^2")
    st.latex(r"\tau_p=\left(\frac{\alpha}{10^{-3}}\right)^4 \times 10^{32}\ \text{years},\quad P_{\mathrm{reset}}=1-e^{-\alpha}")

    subs = {alpha: alpha_val}
    st.markdown("#### With your α")
    st.write({
        "c (natural units)": float(c.subs(subs)),
        "T_GUT": float(T_GUT.subs(subs)),
        "H (natural units)": float(H.subs(subs)),
        "tau_p (years)": float(tau_p.subs(subs)),
        "P_reset": float(P_reset.subs(subs))
    })

# -------------------------
# Chemistry Ladder
# -------------------------
with tab_chem:
    st.subheader("Chemistry Ladder — Slopes & Branches")
    st.caption("45° = molecules combine → 22.5° = buckyballs stack → vertical = diversity wall → cone = abiogenesis")

    s1 = st.slider("Stage-1 length (45°)", 0.2, 1.5, 0.7)
    s2 = st.slider("Stage-2 length (22.5°)", 0.2, 1.5, 0.5)

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot([0, s1], [0, s1], 'r-', lw=2, label="45° (molecules)")
    ax.plot([s1, s1+s2], [s1, s1+0.5*s2], color='orange', lw=2, label="22.5° (buckyballs)")
    ax.plot([s1+s2, s1+s2], [s1+0.5*s2, s1+0.5*s2+0.6], 'b-', lw=2, label="Vertical wall (diversity)")
    ax.set_xlabel("Complexity"); ax.set_ylabel("Energy density")
    ax.legend()
    st.pyplot(fig)

    st.caption("Not a puddle-platypus generator: slopes show how sharp the transition has to be.")

# -------------------------
# Biology Ladder
# -------------------------
with tab_bio:
    st.subheader("Biology Ladder — Diversity Cone")

    n_branches = st.slider("Number of branches", 5, 50, 20)
    depth = st.slider("Branching depth", 1, 5, 3)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(0, 2.0)
    ax.set_xlabel("Complexity axis")
    ax.set_ylabel("Energy axis")

    # Draw cone outline
    ax.plot([-1, 0, 1], [0, 2, 0], 'k--', lw=1)

    # Recursive branch drawing
    def draw_branch(x, y, length, angle, d):
        if d == 0: return
        dx = length * np.cos(angle)
        dy = length * np.sin(angle)
        x2, y2 = x + dx, y + dy
        ax.plot([x, x2], [y, y2], color='green', lw=1)
        for new_angle in np.linspace(angle-0.6, angle+0.6, 2):
            draw_branch(x2, y2, length*0.7, new_angle, d-1)

    for i in range(n_branches):
        ang = np.pi/2 + np.random.uniform(-0.3, 0.3)
        draw_branch(0, 0, 0.5, ang, depth)

    st.pyplot(fig)
    st.caption("Cone fills with branching complexity: proteins, membranes, pathways, cells.")

# -------------------------
# Mind Ladder
# -------------------------
with tab_mind:
    st.subheader("Mind Ladder — Buckyball Core Weights")
    st.caption("Distribute 100 points across the 4 struts: Nutrition, Reproduction, Evolution, Trust.")

    N = st.slider("Nutrition", 0, 100, 25)
    R = st.slider("Reproduction", 0, 100, 25)
    E = st.slider("Evolution", 0, 100, 25)
    T = st.slider("Trust", 0, 100, 25)

    total = max(1, N+R+E+T)
    w = np.array([N, R, E, T]) / total

    foresight = 0.25*w[2] + 0.25*w[3] + 0.2*w[0] + 0.3*w[1]
    st.progress(float(foresight), text=f"Simulation/foresight ≈ {foresight:.2f}")
    st.write(f"Weights → Nutrition:{w[0]:.2f}, Reproduction:{w[1]:.2f}, Evolution:{w[2]:.2f}, Trust:{w[3]:.2f}")

st.caption("TurtleScope v2.1 • CC-BY 4.0 • Adds diversity cone in Biology Ladder.")"""
TurtleScope v2.1 — Fractal Ladder + Biology
Run with: streamlit run app_v2_1.py

Dependencies (install once):
    pip install streamlit sympy numpy matplotlib
"""

import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Core setup
# -------------------------
st.set_page_config(page_title="TurtleScope v2.1", page_icon="🐢", layout="wide")
st.title("🐢 TurtleScope v2.1 — Fractal Ladder")
st.caption("Physics ↔ Chemistry ↔ Biology ↔ Mind")

alpha = sp.symbols('alpha', positive=True)
M = sp.symbols('M', positive=True)
c = alpha
T_GUT = alpha
H = alpha**2
tau_p = (alpha/1e-3)**4 * 1e32
P_reset = 1 - sp.exp(-alpha)

with st.sidebar:
    st.header("Universe Settings")
    alpha_val = st.number_input("α (alpha)", min_value=1e-6, max_value=1.0,
                                value=1e-3, format="%.6f")
    st.caption("Tip: α = √M → c = α")

# -------------------------
# Tabs
# -------------------------
tab_phys, tab_chem, tab_bio, tab_mind = st.tabs(
    ["Physics Ladder", "Chemistry Ladder", "Biology Ladder", "Mind Ladder"]
)

# -------------------------
# Physics Ladder
# -------------------------
with tab_phys:
    st.subheader("Physics Ladder (Q → A)")
    query = st.text_input("Your question", placeholder="e.g., Why is gravity 1/r² here?")

    def explain(q):
        ql = q.lower().strip()
        if not ql:
            return "Ask me anything about light, gravity, unification, PBHs, or constants."
        if "light" in ql or "c " in ql or ql == "c":
            return f"In Turtle-Verse, c = α. With α={alpha_val:g}, c≈{alpha_val:g} (natural units)."
        if "gravity" in ql:
            return "Gravity emerges from entanglement entropy gradients (Ryu–Takayanagi). Effective 1/r² at macroscales."
        if "gut" in ql or "unification" in ql:
            return f"GUT scale tracks α: T_GUT = α. With α={alpha_val:g}, T_GUT≈{alpha_val:g}."
        if "proton" in ql and "decay" in ql:
            tp = float(tau_p.subs({alpha:alpha_val}))
            return f"Proton lifetime ~ τ_p=(α/1e-3)^4·1e32 y. For α={alpha_val:g}, τ_p≈{tp:.3e} years."
        if "reset" in ql or "cycle" in ql:
            pres = float(P_reset.subs({alpha:alpha_val}))
            return f"Reset probability per cycle: P=1−exp(−α). For α={alpha_val:g}, P≈{pres:.6f}."
        if "cmb" in ql:
            return "CMB near-isotropy follows entropy homogenization; anomalies map to local δα/α noise."
        if "pbh" in ql or "black hole" in ql:
            return "PBHs act as entropic seeds; matter/antimatter 50/50 enables rare reset cycles."
        return "Baseline answer: constants and behavior are set by α=√M."

    if st.button("Explain"):
        st.markdown("### Explanation")
        st.write(explain(query))

    st.markdown("### Core Relations")
    st.latex(r"c=\alpha,\quad T_{\mathrm{GUT}}=\alpha,\quad H=\alpha^2")
    st.latex(r"\tau_p=\left(\frac{\alpha}{10^{-3}}\right)^4 \times 10^{32}\ \text{years},\quad P_{\mathrm{reset}}=1-e^{-\alpha}")

    subs = {alpha: alpha_val}
    st.markdown("#### With your α")
    st.write({
        "c (natural units)": float(c.subs(subs)),
        "T_GUT": float(T_GUT.subs(subs)),
        "H (natural units)": float(H.subs(subs)),
        "tau_p (years)": float(tau_p.subs(subs)),
        "P_reset": float(P_reset.subs(subs))
    })

# -------------------------
# Chemistry Ladder
# -------------------------
with tab_chem:
    st.subheader("Chemistry Ladder — Slopes & Branches")
    st.caption("45° = molecules combine → 22.5° = buckyballs stack → vertical = diversity wall → cone = abiogenesis")

    s1 = st.slider("Stage-1 length (45°)", 0.2, 1.5, 0.7)
    s2 = st.slider("Stage-2 length (22.5°)", 0.2, 1.5, 0.5)

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot([0, s1], [0, s1], 'r-', lw=2, label="45° (molecules)")
    ax.plot([s1, s1+s2], [s1, s1+0.5*s2], color='orange', lw=2, label="22.5° (buckyballs)")
    ax.plot([s1+s2, s1+s2], [s1+0.5*s2, s1+0.5*s2+0.6], 'b-', lw=2, label="Vertical wall (diversity)")
    ax.set_xlabel("Complexity"); ax.set_ylabel("Energy density")
    ax.legend()
    st.pyplot(fig)

    st.caption("Not a puddle-platypus generator: slopes show how sharp the transition has to be.")

# -------------------------
# Biology Ladder
# -------------------------
with tab_bio:
    st.subheader("Biology Ladder — Diversity Cone")

    n_branches = st.slider("Number of branches", 5, 50, 20)
    depth = st.slider("Branching depth", 1, 5, 3)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(0, 2.0)
    ax.set_xlabel("Complexity axis")
    ax.set_ylabel("Energy axis")

    # Draw cone outline
    ax.plot([-1, 0, 1], [0, 2, 0], 'k--', lw=1)

    # Recursive branch drawing
    def draw_branch(x, y, length, angle, d):
        if d == 0: return
        dx = length * np.cos(angle)
        dy = length * np.sin(angle)
        x2, y2 = x + dx, y + dy
        ax.plot([x, x2], [y, y2], color='green', lw=1)
        for new_angle in np.linspace(angle-0.6, angle+0.6, 2):
            draw_branch(x2, y2, length*0.7, new_angle, d-1)

    for i in range(n_branches):
        ang = np.pi/2 + np.random.uniform(-0.3, 0.3)
        draw_branch(0, 0, 0.5, ang, depth)

    st.pyplot(fig)
    st.caption("Cone fills with branching complexity: proteins, membranes, pathways, cells.")

# -------------------------
# Mind Ladder
# -------------------------
with tab_mind:
    st.subheader("Mind Ladder — Buckyball Core Weights")
    st.caption("Distribute 100 points across the 4 struts: Nutrition, Reproduction, Evolution, Trust.")

    N = st.slider("Nutrition", 0, 100, 25)
    R = st.slider("Reproduction", 0, 100, 25)
    E = st.slider("Evolution", 0, 100, 25)
    T = st.slider("Trust", 0, 100, 25)

    total = max(1, N+R+E+T)
    w = np.array([N, R, E, T]) / total

    foresight = 0.25*w[2] + 0.25*w[3] + 0.2*w[0] + 0.3*w[1]
    st.progress(float(foresight), text=f"Simulation/foresight ≈ {foresight:.2f}")
    st.write(f"Weights → Nutrition:{w[0]:.2f}, Reproduction:{w[1]:.2f}, Evolution:{w[2]:.2f}, Trust:{w[3]:.2f}")

st.caption("TurtleScope v2.1 • CC-BY 4.0 • Adds diversity cone in Biology Ladder.")
