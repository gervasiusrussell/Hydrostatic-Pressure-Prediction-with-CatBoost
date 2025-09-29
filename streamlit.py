import streamlit as st
import json
import requests

st.title("🌊 Hydrostatic Pressure")
st.info("Input the values one by one to predict")

# Updated feature caps based on training dataset
feature_caps = {
    "measurement_id": (2,21888),
    'water_temperature_50m': (290.35, 307.45),
    'salinity_50m': (10.0, 29.2),
    'oxygen_saturation_50m': (13.1, 26.5),  
    'perceived_water_density': (17.1, 38.6),  
    'sediment_deposition': (0.0, 207.0), 
    'seafloor_pressure': (0.981, 0.9943),
    'plankton_density': (0.0, 100.0),
    'microplankton_density': (0.0, 100.0),
    'mesoplankton_density': (0.0, 100.0),
    'macroplankton_density': (0.0, 100.0),
    'dissolved_gas_pressure': (0.0, 3.46),  
    'current_velocity_near_surface': (0.0, 16.875),
    'current_velocity_deep': (0.0, 24.075),
    'current_direction_near_surface': (2.0, 360.0),
    'current_direction_deep': (2.0, 360.0),
    'current_turbulence': (1.1, 47.5),  
    'sediment_temperature_0_to_10cm': (290.95, 310.65),
    'sediment_temperature_10_to_30cm': (295.45, 302.65),
    'sediment_temperature_30_to_100cm': (297.15, 300.35),
    'sediment_temperature_100_to_250cm': (297.85, 299.45),
    'sediment_porosity_0_to_10cm': (0.06, 0.403),  
    'sediment_porosity_10_to_30cm': (0.0, 1.0),
    'sediment_porosity_30_to_100cm': (0.0, 1.0),
    'sediment_porosity_100_to_250cm': (0.0, 1.0),
    'blue_light_penetration': (0.0, 1029.0),
    'downwelling_light': (0.0, 930.0),
    'scattered_light': (0.0, 481.0),
    'perpendicular_light_intensity': (0.0, 943.5), 
    'thermal_emissions': (0.0, 1387.3), 
    'is_photic_zone': (0, 1),
    'photoperiod_intensity': (0.0, 60.0),
    'chlorophyll_a_concentration': (0.01, 4.933),
    'nitrate_concentration': (1.9103, 8.172),
    'phosphate_concentration': (0.1005, 0.5175),
    'silicate_concentration': (2.6027, 7.6098),
    'total_alkalinity': (2110.7617, 2276.9129),
    'dissolved_inorganic_carbon': (1915.6340, 2163.9688),
    'ph': (7.7, 8.3),
    'partial_pressure_co2': (331.8969, 488.9326),
    'aragonite_saturation_state': (1.7393, 3.3468),
    'sea_surface_height_anomaly': (-23.5803, 22.7490),
    'significant_wave_height': (0.1, 3.0441),
    'bottom_current_shear_stress': (0.0001173, 0.1402),
    'sound_speed_water': (1463.7565, 1535.7759),
    'acoustic_backscatter_intensity': (-91.4354, -53.0455),
    'turbidity': (0.5151, 9.9506),
    'light_attenuation_coefficient_kd': (0.0680, 1.0028),
    'bioluminescence_intensity': (0.8117, 138050871.783),
    'brunt_vaisala_frequency_squared': (3.03315e-07, 0.0007896),
    'mixed_layer_depth': (10.0, 104.3793),
    'year': (2020, 2024),
    'month': (1, 12),
    'day': (1, 31),
    'hour': (0, 23)
}

inputs = {}

for i, (feature, (min_val, max_val)) in enumerate(feature_caps.items()):
        is_int = isinstance(min_val, int) and isinstance(max_val, int)
        if is_int:
            value = st.number_input(
                f"Enter {feature}", 
                min_value=int(min_val),
                max_value=int(max_val),
                value=int((min_val + max_val) // 2),
                step=1,
                format="%d"
            )
        else:
            value = st.number_input(
                f"Enter {feature}",
                min_value=float(min_val),
                max_value=float(max_val),
                value=float((min_val + max_val) / 2),
                step=0.01,
                format="%.5f"
            )
        inputs[feature] = value


# Submit button
if st.button("🚀 Predict"):
    try:
        res = requests.post(
            "http://127.0.0.1:8000/predict",
            data=json.dumps(inputs),
            headers={"Content-Type": "application/json"}
        )
        
        # # Print status code and text for debugging
        # st.write(f"Status code: {res.status_code}")
        # st.write(f"Response text: {res.text}")

        # Only parse JSON if status code is 200
        if res.status_code == 200:
            prediction = res.json().get('prediction')
            st.success(f"✅ Prediction Result: {prediction}")
        else:
            st.error(f"❌ API returned error code: {res.status_code}")
    except Exception as e:
        st.error(f"❌ API call failed: {e}")