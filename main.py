Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import random
import time
import csv
from datetime import datetime

# --- Vitals Simulator ---
def generate_vitals():
    """Simulate patient vitals: HR (bpm), BP (systolic/diastolic)"""
    hr = random.randint(30, 120)          # Heart Rate
    bp_sys = random.randint(80, 140)      # Systolic BP
    bp_dia = random.randint(50, 90)       # Diastolic BP
    return hr, bp_sys, bp_dia

# --- Emergency Detection & Dosage Suggestion ---
def check_emergency(hr):
    """Check if bradycardia emergency exists (HR < 80) and recommend dosage."""
    if hr < 40:
        return True, "Severe bradycardia", "1.0 mg IV Atropine"
    elif hr < 60:
        return True, "Moderate bradycardia", "0.5 mg IV Atropine"
    elif hr < 80:
        return True, "Mild bradycardia", "0.25 mg IV Atropine"
    return False, "Normal", "No dose"

# --- Logging ---
def log_event(patient_name, ward, hr, bp_sys, bp_dia, severity, dose, decision):
...     """Log detailed vitals and doctor decision into CSV."""
...     with open("patient_log.csv", "a", newline="") as f:
...         writer = csv.writer(f)
...         writer.writerow([datetime.now(), patient_name, ward, hr, f"{bp_sys}/{bp_dia}", severity, dose, decision])
... 
... # --- Main Monitoring ---
... def run_monitoring(simulation_time=30, delay=5):
...     patient_name = "ABC"
...     ward = "Ward 1"
...     print("Starting AI Emergency Decision Support Simulation...")
...     print(f"Monitoring patient {patient_name} in {ward}...\n")
... 
...     start_time = time.time()
...     while time.time() - start_time < simulation_time:
...         hr, bp_sys, bp_dia = generate_vitals()
...         print(f"Vitals → HR: {hr} bpm, BP: {bp_sys}/{bp_dia} mmHg")
... 
...         emergency, severity, dose = check_emergency(hr)
...         if emergency:
...             print(f"\n⚠️ ALERT: {patient_name} in {ward} has {severity} (HR = {hr} bpm)")
...             decision = input(f"Doctor Approval → Give {dose}? (Y/N): ").strip().upper()
... 
...             if decision == "Y":
...                 action = f"Approved → Patch secreted {dose}"
...                 print(f"✅ Nurse notified. Patch secreted {dose}.\n")
...             else:
...                 action = "Rejected → Wait for further comment"
...                 print("❌ No drug secreted. Awaiting doctor input.\n")
... 
...             log_event(patient_name, ward, hr, bp_sys, bp_dia, severity, dose, action)
...         else:
...             log_event(patient_name, ward, hr, bp_sys, bp_dia, severity, dose, "No emergency")
...         
...         time.sleep(delay)
... 
...     print("Monitoring session ended. Logs saved to patient_log.csv.")
... 
... # Run
... if __name__ == "__main__":
...     run_monitoring(simulation_time=30, delay=5)
