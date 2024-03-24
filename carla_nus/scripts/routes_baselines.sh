#!/bin/bash

set -e

cd ../scenario_runner

while IFS= read -r line; do
  python scenario_runner.py --route srunner/data/routes_nus.xml srunner/data/all_towns_traffic_scenarios.json "$line" \
  --agent srunner/autoagents/npc_agent.py \
  --lidar-params ../hyperparams/det_optimal.toml \
  --hyperparams ../hyperparams/det_optimal.toml \
  --split training --full_round &>> ../logs/routes_hyper_center.out
done < ../scripts/all_routes.txt

cd ../scripts

