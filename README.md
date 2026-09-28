# SmartPrior

SmartPrior is a methodology for the rapid optimization of energy supply systems (EVS) using pre-trained Gaussian process regression (GPR) models. Instead of setting up a new MILP formulation or simulation for every application case, GPR models approximate purely energetic target quantities for typical combinations of boundary conditions ("drawers"). Economic and ecological evaluation (TAC, CO2) is performed afterwards and can be varied freely, without retraining the GPR models.

This repository contains:
- an open, rule-based merit-order dispatch simulator serving as the ground-truth reference
- the design-of-experiments (DoE) sampling pipeline used to generate training data
- GPR training and the downstream TAC/CO2 post-processing
- a custom particle swarm optimization (PSO) implementation operating on the GPR models
- the scripts used to reproduce the results shown in the associated paper

## Associated Paper

To be added upon publication (title, authors, DOI).

## Repository Structure

```
src/smartprior/simulator/     Merit-order dispatch simulator (ground truth)
src/smartprior/doe/           DoE sampling and drawer definitions
src/smartprior/gpr/           GPR training and evaluation
src/smartprior/optimization/  Custom PSO implementation
src/smartprior/config/        Central technology-typical constants
tests/                        Unit and plausibility tests
data/                         Open example data and external reference sources
experiments/                  Concrete simulation and comparison runs
paper/                        Scripts generating the paper's figures and tables
```

## Installation

Requires Python 3.10 or newer.

```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Quickstart

```python
from smartprior.simulator.runner import simulate

result = simulate(...)  # see src/smartprior/simulator/runner.py for the full parameter interface
```

A complete example is provided in `notebooks/01_dispatch_demo.ipynb`.

## Reproducing the Paper Results

All figures and tables shown in the paper can be reproduced from the scripts in `experiments/scripts/` and `paper/figures/` / `paper/tables/`. The parameter combinations used are documented in `experiments/configs/`.

## Data

`data/examples/` contains exclusively open or synthetic example data (load profiles, weather data) that are freely usable together with this repository. The origin and license of each file are documented in `data/README.md`.

Internal figures from the SmartPrior final project report are **not** part of this repository. For technology cost and efficiency parameters (CHP, heat pump, gas boiler, storage, PV, solar thermal), only openly accessible reference sources were used (details in `data/README.md`).

## Data and Code Availability Statement

The complete source code is publicly available under the MIT license at: https://github.com/MariusReichh/smartprior. All example data used are included in the repository under `data/examples/`. Internal, project-confidential parameter values were replaced with openly accessible reference values (see `data/README.md`).

## License

MIT, see [LICENSE](LICENSE).

## Citation

See [CITATION.cff](CITATION.cff).
