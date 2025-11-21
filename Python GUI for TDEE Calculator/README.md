# 🧮 Interactive TDEE Calculator (Python GUI)

A simple, user-friendly **Python GUI application** that helps users estimate their **Total Daily Energy Expenditure (TDEE)** based on gender, age, height, weight, and exercise level.  
The app also provides helpful reference information such as average TDEE values and standard BMR ranges.

---

## 🧠 What Is TDEE?

**Total Daily Energy Expenditure (TDEE)** is the total number of calories your body burns in a day. It combines:

- Basal Metabolic Rate (**BMR**) – energy needed to keep you alive at rest  
- Physical activity / exercise  
- Thermic effect of food (digestion)  
- Other minor factors  

In this app, we first calculate **BMR**, then multiply it by an **activity factor** (exercise level) to estimate TDEE.

---

## 🎯 App Objectives

- Allow users to **input** their personal details via a GUI
- Calculate **BMR** using gender-specific formulas  
- Adjust BMR by exercise level to compute **TDEE**
- Display **clear, easy-to-understand results** in calories per day
- Provide reference values for **average TDEE** and **standard BMR ranges**
<img width="490" height="239" alt="image" src="https://github.com/user-attachments/assets/e8c8705e-dff5-4f18-93cd-0792734cf7e0" />
<img width="394" height="361" alt="image" src="https://github.com/user-attachments/assets/b89c2618-6988-4198-a331-c747a2aaad7b" />
---

## 📥 Inputs & 📤 Outputs

### User Inputs (via GUI)

- **Gender**: Male / Female  
- **Age** (years)  
- **Height** (centimetres)  
- **Weight** (kilograms)  
- **Exercise Level** (one of the following):
  - No Exercise  
  - Light Exercise (1–3 times per week)  
  - Normal Exercise (4–5 times per week)  
  - Hard Exercise (6–7 times per week)  
  - Extreme Exercise (harsh intensity)  

### Program Output

- **Calculated TDEE** in **kcal/day**, displayed clearly on the interface.
<img width="226" height="203" alt="image" src="https://github.com/user-attachments/assets/1655cb7c-a539-4b44-a823-9a0486e1e38c" />
---

## 📊 Reference Information

### Average TDEE (Ages 19–22)

- **Men**: 3000 kcal/day  
- **Women**: 2100 kcal/day  

### Standard BMR Ranges (Calories per Hour)

| Age   | Male | Female |
|-------|------|--------|
| 20–29 | 39.5 | 37.0   |
| 30–39 | 39.5 | 36.5   |
| 40–49 | 38.5 | 36.5   |
| 50–59 | 37.5 | 35.0   |
| 60–69 | 36.5 | 34.0   |
| 70–79 | 35.5 | 33.0   |

### Exercise Levels & Multipliers

| Exercise Level                            | Multiplier |
|-------------------------------------------|------------|
| No Exercise                               | 1.2        |
| Light Exercise (1–3 times per week)       | 1.375      |
| Normal Exercise (4–5 times per week)      | 1.55       |
| Hard Exercise (6–7 times per week)        | 1.725      |
| Extreme Exercise (harsh intensity)        | 1.9        |

---

## 🧩 Calculation Logic

### 1️⃣ Step 1 – Calculate BMR

All formulas use:

- **Height** in centimetres  
- **Weight** in kilograms  

**For Male:**

- BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)

**For Female:**

- BMR = 65.5 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

### 2️⃣ Step 2 – Apply Exercise Multiplier to Get TDEE

- No Exercise                         → tdee = bmr * 1.2

- Light Exercise (1–3 times/week)          → tdee = bmr * 1.375
  
- Normal Exercise (4–5 times/week)         → tdee = bmr * 1.55

- Hard Exercise (6–7 times/week)           → tdee = bmr * 1.725

- Extreme Exercise (harsh intensity)  → tdee = bmr * 1.9


