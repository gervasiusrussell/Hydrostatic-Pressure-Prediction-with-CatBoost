import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd
from DataPredict import DataPredict

app = FastAPI()
pickle_in = open("./catboost_model_final.pkl", "rb")
classifier = pickle.load(pickle_in)

original_column_names = {
    "measurement_id": "all_numerics__measurement_id",
    "water_temperature_50m": "all_numerics__water_temperature_50m",
    "salinity_50m": "all_numerics__salinity_50m",
    "oxygen_saturation_50m": "all_numerics__oxygen_saturation_50m",
    "perceived_water_density": "all_numerics__perceived_water_density",
    "sediment_deposition": "all_numerics__sediment_deposition",
    "seafloor_pressure": "all_numerics__seafloor_pressure",
    "plankton_density": "all_numerics__plankton_density",
    "microplankton_density": "all_numerics__microplankton_density",
    "mesoplankton_density": "all_numerics__mesoplankton_density",
    "macroplankton_density": "all_numerics__macroplankton_density",
    "dissolved_gas_pressure": "all_numerics__dissolved_gas_pressure",
    "current_velocity_near_surface": "all_numerics__current_velocity_near_surface",
    "current_velocity_deep": "all_numerics__current_velocity_deep",
    "current_direction_near_surface": "all_numerics__current_direction_near_surface",
    "current_direction_deep": "all_numerics__current_direction_deep",
    "current_turbulence": "all_numerics__current_turbulence",
    "sediment_temperature_0_to_10cm": "all_numerics__sediment_temperature_0_to_10cm",
    "sediment_temperature_10_to_30cm": "all_numerics__sediment_temperature_10_to_30cm",
    "sediment_temperature_30_to_100cm": "all_numerics__sediment_temperature_30_to_100cm",
    "sediment_temperature_100_to_250cm": "all_numerics__sediment_temperature_100_to_250cm",
    "sediment_porosity_0_to_10cm": "all_numerics__sediment_porosity_0_to_10cm",
    "sediment_porosity_10_to_30cm": "all_numerics__sediment_porosity_10_to_30cm",
    "sediment_porosity_30_to_100cm": "all_numerics__sediment_porosity_30_to_100cm",
    "sediment_porosity_100_to_250cm": "all_numerics__sediment_porosity_100_to_250cm",
    "blue_light_penetration": "all_numerics__blue_light_penetration",
    "downwelling_light": "all_numerics__downwelling_light",
    "scattered_light": "all_numerics__scattered_light",
    "perpendicular_light_intensity": "all_numerics__perpendicular_light_intensity",
    "thermal_emissions": "all_numerics__thermal_emissions",
    "is_photic_zone": "all_numerics__is_photic_zone",
    "photoperiod_intensity": "all_numerics__photoperiod_intensity",
    "chlorophyll_a_concentration": "all_numerics__chlorophyll_a_concentration (mg m-3)",
    "nitrate_concentration": "all_numerics__nitrate_concentration (µmol L-1)",
    "phosphate_concentration": "all_numerics__phosphate_concentration (µmol L-1)",
    "silicate_concentration": "all_numerics__silicate_concentration (µmol L-1)",
    "total_alkalinity": "all_numerics__total_alkalinity (µmol kg-1)",
    "dissolved_inorganic_carbon": "all_numerics__dissolved_inorganic_carbon (µmol kg-1)",
    "ph": "all_numerics__pH",
    "partial_pressure_co2": "all_numerics__partial_pressure_CO2 (µatm)",
    "aragonite_saturation_state": "all_numerics__aragonite_saturation_state",
    "sea_surface_height_anomaly": "all_numerics__sea_surface_height_anomaly (cm)",
    "significant_wave_height": "all_numerics__significant_wave_height (m)",
    "bottom_current_shear_stress": "all_numerics__bottom_current_shear_stress (Pa)",
    "sound_speed_water": "all_numerics__sound_speed_water (m s-1)",
    "acoustic_backscatter_intensity": "all_numerics__acoustic_backscatter_intensity (dB)",
    "turbidity": "all_numerics__turbidity (NTU)",
    "light_attenuation_coefficient_kd": "all_numerics__light_attenuation_coefficient_Kd (m⁻¹)",
    "bioluminescence_intensity": "all_numerics__bioluminescence_intensity (photons cm-2 s-1)",
    "brunt_vaisala_frequency_squared": "all_numerics__Brunt_Vaisala_frequency_squared (s-2)",
    "mixed_layer_depth": "all_numerics__mixed_layer_depth (m)",
    "year": "all_numerics__year",
    "month": "all_numerics__month",
    "day": "all_numerics__day",
    "hour": "all_numerics__hour"
}

@app.get("/")
def index():
    return{"message": "Hello, Student"}

@app.post("/predict")
def predict(data:DataPredict):
    data = data.dict()
    
    mapped_input = {
        original_column_names[key]: value
        for key, value in data.items()
    }

    df = pd.DataFrame([mapped_input])
    prediction = classifier.predict(df)

    return {"prediction": prediction[0]}