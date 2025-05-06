from JTBrix import run_test


results, order = run_test("../src/JTBrix/data/config.yml", "../src/JTBrix/data/static/") 
print("Combined results:", results)
print("Execution order:", order)


