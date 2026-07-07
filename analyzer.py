import json
import os

from modules.benchmark import run_benchmark
from modules.analyzer import benchmark_analysis
from modules.deepscan import run_deepscan
from modules.scorer import score_results
from modules.report import build_report

print()

print("===================================")
print("CF Auto Optimizer")
print("Version 1.0")
print("===================================")
print()

with open("config.json","r",encoding="utf8") as f:
    config=json.load(f)

os.makedirs("results",exist_ok=True)
os.makedirs("cache",exist_ok=True)

print("[1/6] Benchmark")
run_benchmark(config)

print()

print("[2/6] Analyze")
benchmark_analysis(config)

print()

print("[3/6] Deep Scan")
run_deepscan(config)

print()

print("[4/6] Score")
score_results(config)

print()

print("[5/6] HTML Report")
build_report(config)

print()

print("[6/6] Done")
print()
print("BestIPs.txt generated.")