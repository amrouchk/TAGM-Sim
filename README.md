# TAGM-Sim: Spatiotemporal Matching in Trust-Aware Ride-Sharing

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official repository for the simulation framework and interactive visualizations accompanying our research on the **Trust-Aware Collaborative Recommendation Mechanism (TAGM)** for Social IoT mobility networks.
## LINK TO TEST THE RESULTS SIMULATION
```bash

https://tagm-sim-results.streamlit.app/

````

## 📖 Overview

In modern urban mobility networks, pure distance-based matching algorithms often fall into an **"Efficiency Trap,"** pairing riders with proximate but historically unreliable (adversarial) providers. 

This repository contains the `TAGM-Sim` framework, which introduces a strict spatiotemporal trust engine that forcibly migrates matches from this danger zone into a secure operational envelope (the **"Security Shift"**). Crucially, the simulator enforces strict physical capacity constraints ($\text{cap}(v_j) > 0$), proving that TAGM's trust-filtering mechanism scales under real-world congestion and "spillover" effects without destroying network availability.

### Key Conceptual Contributions Visualized Here:
* **The Baseline ($\alpha = 0.0$):** High Quality of Experience (QoE) but dangerous adversarial exposure (The Efficiency Trap).
* **The TAGM Optimal ($\alpha = 0.9$):** A 42.7% reduction in adversarial failures through trust-prioritization and secondary candidate routing.
* **The Quarantine Threshold ($T_{min} = 0.2$):** The strict safety boundary preventing systemic network poisoning.

---

## 🚀 1. The Interactive Dashboard (Reviewer Quick-Start)

We have provided a lightweight, interactive web application built with Streamlit so reviewers and researchers can instantly visualize the core mathematical trade-offs between Trust ($\alpha$) and QoE without needing to run the full multi-GPU simulation.

### Installation
Ensure you have Python installed, then run:
```bash
pip install streamlit numpy matplotlib seaborn
````

### Launching the Dashboard

*Note: The dashboard must be launched from your operating system's command line (Terminal / CMD), not from inside an IDE like Spyder.*

1.  Clone the repository and navigate to the folder:
    ```bash
    git clone [https://github.com/YourUsername/TAGM-Sim.git](https://github.com/YourUsername/TAGM-Sim.git)
    cd TAGM-Sim
    ```
2.  Run the application:
    ```bash
    streamlit run app.py
    ```
3.  A browser window will automatically open. Use the interactive sliders to observe how shifting the trust weight ($\alpha$) physically moves the network's joint distribution out of the Efficiency Trap.

-----

## ⚙️ 2. The Full Multi-GPU Simulator (For Reproduction)

For researchers wishing to reproduce the full 2.5-million-interaction dataset or modify the core PyTorch trust engine, the complete simulation pipeline is included.

### Installation & Requirements

The core simulator relies on hardware-accelerated tensor operations.

```bash
pip install torch pandas scipy
```

### Running the Pipeline

The pipeline is divided into three distinct stages to manage memory efficiently:

1.  **Run the Simulation Engine:**
    Executes the dynamic ride-sharing environment across available CUDA devices, applying the TAGM framework to the Shenzhen electric taxi dataset.

    ```bash
    python main.py
    ```

2.  **Run the Alpha Sweep (Trade-off Analysis):**
    Generates the comparative logs across varying weights of $\alpha$ (0.0 to 1.0).

    ```bash
    python matcher.py
    ```

3.  **Generate Publication Figures:**
    Processes the simulation logs to generate high-fidelity, KDE-smoothed IEEE-formatted visualizations (Figures A through F).

    ```bash
    python visualize.py
    ```

-----

## 📁 Repository Structure

  * `app.py`: The interactive Streamlit dashboard source code.
  * `main.py`: The core `TAGMSimulator` class handling PyTorch state management and agent life-cycles.
  * `matcher.py`: The vectorized GPU matching logic and active occupancy/capacity constraints.
  * `config.py`: Hardcoded simulation parameters, bounds, and thresholds.
  * `visualize.py`: Advanced plotting scripts for generating paper-ready KDE and Lorenz curves.
  * `/results`: Generated logs, driver snapshots, and output `.png` figures.

-----

## 📝 Citation

If you use this simulator or find our research helpful in your own work, please cite our paper:

```bibtex
@article{khelloufi2026tagm,
  title={Research on the Reliability Verification and Safety-Aware Collaborative Recommendation Mechanism for Embodied AGI Agents in Industrial Social IoT},
  author={Khelloufi, Amar and [Co-Authors]},
  journal={[Journal Name]},
  year={2026}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

```
