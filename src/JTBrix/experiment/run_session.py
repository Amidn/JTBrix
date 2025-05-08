# from JTBrix.ui.main import ui, submitted_results
# from flask import Flask
# import os
# import webbrowser
# from pathlib import Path
# import JTBrix
# from JTBrix.questionnaire.screens import screens
# from JTBrix.utils import find_free_port
# from JTBrix import screen_config
# from JTBrix.utils.results import get_combined_results
# import time
# #from JTBrix.app import app  



# def get_app():
#     from JTBrix.app import app
#     return app


# # jtbrix_root = Path(JTBrix.__file__).parent
# # template_path = jtbrix_root / "templates"  # Now points to JTBrix/templates

# import threading

# def run_entire_test_config(config: dict, static_folder: str, timeout: int = 600) -> dict:
#     screen_config.flow_config = config
#     submitted_results.clear()



#     #port = find_free_port()
#     # port = 5600
#     # print (f"Using port {port} for Flask app")  
#     # def run_app():
#     #     app = get_app()
#     #     app.run(port=port, debug=False, use_reloader=False)

#     # thread = threading.Thread(target=run_app)
#     # thread.daemon = True
#     # thread.start()
#     #print (f"Flask app running on port {port}")
#     # time.sleep(1)
#     # 
#     # webbrowser.open(f"http://127.0.0.1:{port}/experiment")

    
#     # Wait until any submission is marked as finished
#     print("Waiting for experiment to finish...")
#     stop_time = time.time()

#     while time.time() - start_time < timeout:
#         if any(entry.get("finished") for entry in submitted_results):
#             break
#         time.sleep(1)  # Check every second
#     #thread.join()  # Or implement your own wait logic

#     duration_seconds = int(time.time() - stop_time)
#     results = get_combined_results(submitted_results)
#     results["experiment_start"] = start_timestamp
#     results["experiment_duration_sec"] = duration_seconds
#     return results