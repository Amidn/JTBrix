from JTBrix import run_test
from JTBrix.utils.results import build_full_structured_result


results, order = run_test("../src/JTBrix/data/config.yml", "../src/JTBrix/data/static/", timeout=300) 
print("Combined results:", results)
print("Execution order:", order)

structured_output = build_full_structured_result(results, "../src/JTBrix/data/config.yml", execution_order=order)
print ("Structured output:", structured_output)
print("Structured output keys:", structured_output.keys())
print("Structured output values:", structured_output.values())


