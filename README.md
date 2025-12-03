# MFP-Thermal-EMT  
Effective Medium Theory (EMT) Modelling for the Thermal Conductivity of Porous Moulded Fibre Products

---

## 1. Justification  
Moulded Fibre Products (MFPs) are increasingly used as sustainable alternatives to plastics in packaging applications.  
These materials are **porous cellulose networks**, where heat transfer is governed by a combination of fibre properties, pore structure, and thin polymer barrier coatings applied for moisture and grease resistance.

Understanding how **porosity** and **barrier layers** influence the **effective thermal conductivity** (k_eff) is essential for:

- Packaging performance and safety  
- Thermal resistance of food trays and serviceware  
- Oven / heat-exposure durability  
- Material optimisation and eco-design  
- Barrier engineering in sustainable products  

A lightweight, physics-based modelling tool helps researchers quickly explore structure–property relationships without requiring full CFD/FEM simulations.

---

## 2. Problem Statement  
MFPs exhibit complex heat-transfer behaviour due to their two-phase nature:

- **Solid fibre phase** with moderate thermal conductivity  
- **Air-filled pores** with very low thermal conductivity  

In addition, thin polymer coatings (e.g., PLA, PVOH, bio-barriers) are used as moisture/oxygen barriers, but their *thermal* impact is not well understood.

**Key questions:**

1. *How does porosity affect k_eff in a fibre–air composite?*  
2. *How much does a thin coating layer (5–50 µm) alter the overall thermal performance?*  
3. *Can simple analytical models approximate MFP behaviour efficiently?*

This project addresses these questions using Effective Medium Theory.

---

## 3. Rationale for Using Effective Medium Theory (EMT)  
Effective Medium Theory provides **closed-form analytical expressions** that approximate the effective thermal conductivity of heterogeneous media.

EMT is appropriate because:

- MFPs behave like **random fibrous porous materials**.  
- EMT offers **upper and lower bounds** for property estimation.  
- It is computationally light, intuitive, and ideal for **early-stage material screening**.
- It forms the theoretical foundation before switching to FEM/CFD or microstructure modelling.

The project uses three classical EMT formulations:

- **Series model** → lower bound  
- **Parallel model** → upper bound  
- **Geometric mean model** → realistic intermediate behaviour  

Additionally, a **1D layer-in-series model** is applied to incorporate polymer barrier coatings.

---

##  4. Design & Methodology  

### **4.1 Model Implementation**
### 
The mathematical models used in this project are implemented in `src/emt_models.py`.  
The module includes four core functions:

- `k_series(k_fibre, k_air, porosity)`  
- `k_parallel(k_fibre, k_air, porosity)`  
- `k_geometric(k_fibre, k_air, porosity)`  
- `keff_with_barrier(k_core, L_core, k_barrier, L_barrier)`

These functions correspond to the classical analytical formulations commonly used to approximate heat conduction in porous two-phase media.  
The first three functions (series, parallel, geometric mean) provide lower bound, upper bound, and realistic intermediate predictions of the effective thermal conductivity of fibre–air mixtures.

The `keff_with_barrier` function implements a simple **1D thermal resistance model**, enabling evaluation of how a thin polymer coating layer alters the overall thermal behaviour of the MFP structure.

Together, these formulations provide a lightweight but physically meaningful framework for analysing structure–property relationships in moulded fibre materials.


---

### **4.2 Parametric Studies**
A Jupyter Notebook (`notebooks/01_emt_mfp_demo.ipynb`) generates:

- **k_eff vs. porosity curves** for the three EMT models  
- **Barrier thickness vs. total k_eff** for 0–50 µm coatings  
- Optional comparisons for different fibre materials  

---

### **4.3 Visualisation**
Plots illustrate:

- Upper/lower conductivity bounds  
- Realistic intermediate behaviour (geometric mean)  
- Sensitivity of thermal conductivity to porosity  
- Thermal impact of surface barrier engineering  

---

## 5.Key Result Visualizations

  ### 5.1. k_eff vs Porosity

![k_eff vs Porosity](notebooks/figures/keff_vs_porosity.png)

Figure: Effective thermal conductivity (k_eff) as a function of porosity (ε) for moulded fibre products.
As porosity increases, k_eff decreases significantly across all models. The series model provides a lower bound, assuming heat flows only through air or fibre in sequence. The parallel model gives an upper bound, assuming perfect parallel conduction paths. The geometric mean EMT model predicts a realistic intermediate behaviour and is most representative of disordered porous structures. This highlights how increasing porosity reduces thermal performance, a key consideration in material design.

### 5.2. Barrier Thickness Effect on Thermal Conductivity

![Barrier Thickness Effect](notebooks/figures/barrier_thickness_effect.png)

Figure: Effect of polymer barrier thickness on total effective thermal conductivity (k_eff) for ε = 0.7.
The coating causes only a modest increase in k_eff, indicating that thin functional barrier layers (e.g., 10–30 µm) can be added for moisture protection with minimal impact on thermal insulation performance.

---
## 6. Future Work  

Potential extensions include:

- **Temperature-dependent conductivity models**  
- **Different fibre chemistries** (cellulose, lignin-rich, mineral-filled)  
- **2D/3D random fibre network generation**  
- **Finite Element (FEM) microstructure simulations** for validation  
- **Coupling with moisture diffusion or WVTR models**  
- **Streamlit dashboard** for interactive materials design  

---

## How to Run

```bash
git clone https://github.com/senacakici/mfp-thermal-emt.git
cd mfp-thermal-emt
python -m venv .venv
.\.venv\Scripts\activate      # Windows
pip install -r requirements.txt
jupyter notebook
