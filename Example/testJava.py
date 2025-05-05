from flask import Flask
from JTBrix.experiment.run_session import run_entire_test_config
from JTBrix.screen_config import flow_config


config_path = ""
static_folder="/Users/amid/GitHub/JTBrix/Example/static/"
from JTBrix.utils.config import read_experiment_config
config, order = read_experiment_config(config_path)
print("CONFIG:")


print("\nSELECTED ORDER:", order)
   



flow_config.clear()
flow_config.extend(config)
results = run_entire_test_config(config, static_folder=static_folder)
print(results)


