import pandas as pd

# 1. ตารางมาตรฐานเหล็ก (Standard Table - TIS/ASTM)
standard_steel = {
    'RB9': {'weight_kg_m': 0.499, 'min_tol': 0.47, 'max_tol': 0.52},
    'DB12': {'weight_kg_m': 0.888, 'min_tol': 0.84, 'max_tol': 0.93},
    # ... ใส่เพิ่มได้
}

def verify_steel(steel_type, measured_weight):
    std = standard_steel.get(steel_type)
    if not std:
        return "Unknown Type"
    
    # เช็คว่าอยู่ในเกณฑ์มาตรฐานไหม (Tolerance Check)
    if std['min_tol'] <= measured_weight <= std['max_tol']:
        return "PASS"
    else:
        return f"FAIL (Std: {std['weight_kg_m']}, Diff: {measured_weight - std['weight_kg_m']:.3f})"

# ตัวอย่างการใช้งานจริง
# df['QC_Status'] = df.apply(lambda x: verify_steel(x['Steel_Type'], x['Weight_Per_Meter']), axis=1)