# MFP-Thermal-EMT

A Python-based thermal conductivity modelling tool for **moulded fibre products (MFPs)** using **Effective Medium Theory (EMT)**.  
The model predicts how **porosity**, **fibre–air composition**, and **thin polymer barrier layers** influence effective thermal conductivity.

This project is inspired by sustainable fibre-based packaging applications and aligns with modelling approaches used in research on cellulose-based materials.

---

## Motivation

Moulded fibre products are porous cellulose structures used in sustainable packaging.  
Their thermal behaviour depends strongly on:

- Porosity (ε)
- Fibre/air phase ratio
- Intrinsic fibre conductivity
- Additional barrier layers (e.g., bio-based polymer coatings)

Understanding **how structure affects thermal performance** is essential for:
- Packaging design  
- Barrier optimization  
- Material selection  
- Recycling and biodegradability considerations  


---

##  Features

- **Series & parallel bounds** for two-phase (fibre + air) media  
- **Geometric mean EMT model** for porous fibrous networks  
- **Porosity–conductivity parametric study**  
- **1D series model with polymer barrier layer**  
- **Jupyter Notebook demo with visualisations**

---

## Repository structure

```text
mfp-thermal-emt/
│
├─ src/
│  └─ emt_models.py        # EMT models and 1D barrier model
│
├─ notebooks/
│  └─ 01_emt_mfp_demo.ipynb   # Main demonstration notebook
│
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore
 
 
