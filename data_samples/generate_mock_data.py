import pandas as pd
import os
import numpy as np

# สร้างโฟลเดอร์ data_samples ถ้ายังไม่มี
if not os.path.exists('data_samples'):
    os.makedirs('data_samples')

# ==========================================
# 1. สร้างไฟล์สำหรับ Project 1: Steel Verification
# ==========================================
print("Generating mock_steel_list.xlsx ...")

steel_data = {
    'Material_ID': [f'MT-{i:04d}' for i in range(1, 16)],
    'Steel_Type': [
        'RB6', 'RB9', 'DB12', 'DB12', 'DB16', 
        'DB20', 'DB25', 'RB9', 'DB12', 'DB28',
        'RB6', 'DB12', 'DB20', 'DB12', 'RB9'
    ],
    'Lot_Number': [f'LOT-2025-{np.random.randint(10, 99)}' for _ in range(15)],
    'Measured_Weight_kg_m': [
        0.222, 0.499, 0.888, 0.950, 1.58,  # 0.950 คือจงใจให้เกิน (Fail)
        2.47, 3.85, 0.450, 0.880, 4.83,    # 0.450 คือจงใจให้ขาด (Fail)
        0.220, 0.890, 2.30, 0.888, 0.500   # 2.30 คือจงใจให้ขาด (Fail)
    ],
    'Supplier': ['Siam Yamato', 'Tata Steel', 'Millcon'] * 5
}

df_steel = pd.DataFrame(steel_data)
df_steel.to_excel('data_samples/mock_steel_list.xlsx', index=False)


# ==========================================
# 2. สร้างไฟล์สำหรับ Project 2: Concrete Estimation
# ==========================================
print("Generating mock_boq_structure.xlsx ...")

boq_data = {
    'Item_ID': [f'ITEM-{i:03d}' for i in range(1, 11)],
    'Zone': ['Zone A', 'Zone A', 'Zone B', 'Zone B', 'Zone C'] * 2,
    'Task_Type': [
        'flooring_ground', 'column_beam', 'precast', 'stairs', 'leveling',
        'flooring_upper', 'column_beam', 'precast', 'flooring_ground', 'stairs'
    ],
    'Description': [
        'Ground Floor Slab', 'Main Columns', 'Precast Wall Panel', 'Staircase ST1', 'Lean Concrete',
        '2nd Floor Slab', 'Roof Beams', 'Facade Panel', 'Walkway', 'Fire Exit Stair'
    ],
    'Length_m': np.random.uniform(5.0, 20.0, 10).round(2),
    'Width_m': np.random.uniform(2.0, 10.0, 10).round(2),
    'Height_Depth_m': [0.15, 3.5, 3.0, 1.2, 0.05, 0.20, 0.40, 2.8, 0.10, 1.5],
    'Quantity': [1, 12, 20, 2, 1, 1, 8, 15, 1, 2] # จำนวนชิ้น
}

df_boq = pd.DataFrame(boq_data)
df_boq.to_excel('data_samples/mock_boq_structure.xlsx', index=False)

print("✅ Success! Mock data files created in 'data_samples/' folder.")