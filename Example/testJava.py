from flask import Flask
from JTBrix.experiment.run_session import run_entire_test_config
from JTBrix.screen_config import flow_config

from JTBrix.utils.config import read_experiment_config
config, order = read_experiment_config("config.yml")
print("CONFIG:")
for item in config:
    print(item)

print("\nSELECTED ORDER:", order)
   
if __name__ == "__main__":


    flow_config.clear()
    flow_config.extend(config)
    results = run_entire_test_config(config, static_folder="/Users/amid/GitHub/JTBrix/Example/static/")
    print(results)
    print(results["answers"])
    print(results["times"])

