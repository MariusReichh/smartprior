"""
One-time scaffolding script for the smartprior repository.
Run inside the target directory: python scaffold_repo.py
Creates directories and empty placeholder files. Does not overwrite existing files.
"""

from pathlib import Path

ROOT = Path(".")

DIRS = [
    "src/smartprior/simulator",
    "src/smartprior/doe",
    "src/smartprior/gpr",
    "src/smartprior/optimization",
    "src/smartprior/config",
    "tests/fixtures",
    "data/external",
    "data/examples",
    "experiments/configs",
    "experiments/scripts",
    "experiments/results/raw",
    "experiments/results/processed",
    "paper/figures/output",
    "paper/tables",
    "notebooks",
    "docs",
]

FILES = {
    "src/smartprior/__init__.py": "",
    "src/smartprior/simulator/__init__.py": "",
    "src/smartprior/simulator/pv.py": '"""PV generation: parameter object and calculation."""\n',
    "src/smartprior/simulator/battery.py": '"""Battery storage: parameter object and balancing logic."""\n',
    "src/smartprior/simulator/chp.py": '"""CHP unit: parameter object (incl. minimum part load, minimum runtimes, marginal cost) and dispatch behavior."""\n',
    "src/smartprior/simulator/heat_pump.py": '"""Heat pump: parameter object and dispatch behavior."""\n',
    "src/smartprior/simulator/boiler.py": '"""Gas boiler: parameter object and dispatch behavior."""\n',
    "src/smartprior/simulator/solar_thermal.py": '"""Solar thermal: fixed dispatch priority, sizing as an influencing variable."""\n',
    "src/smartprior/simulator/storage.py": '"""Thermal storage: state variable, not a sizing parameter."""\n',
    "src/smartprior/simulator/dispatch.py": '"""Merit-order state machine: marginal-cost sorting, minimum part load / minimum runtime logic."""\n',
    "src/smartprior/simulator/runner.py": '"""Public simulate() function: annual time-step loop, stable parameter interface for DoE."""\n',
    "src/smartprior/doe/__init__.py": "",
    "src/smartprior/doe/sampling.py": '"""DoE sampling (e.g. Latin Hypercube) over the parameter space."""\n',
    "src/smartprior/doe/schemas.py": '"""Definition of boundary-condition combinations ("drawers")."""\n',
    "src/smartprior/gpr/__init__.py": "",
    "src/smartprior/gpr/training.py": '"""GPR training on energetic target quantities."""\n',
    "src/smartprior/gpr/evaluation.py": '"""GPR evaluation including downstream TAC/CO2 post-processing."""\n',
    "src/smartprior/optimization/__init__.py": "",
    "src/smartprior/optimization/pso.py": '"""Custom particle swarm optimization implementation operating on the GPR models."""\n',
    "src/smartprior/config/__init__.py": "",
    "src/smartprior/config/defaults.py": '"""Central technology-typical constants: minimum part load, minimum runtimes. Single source of truth for these values."""\n',
    "tests/__init__.py": "",
    "tests/test_dispatch.py": "",
    "tests/test_storage.py": "",
    "tests/test_energy_balance.py": "",
    "tests/fixtures/minimal_case.py": '"""Hand-calculated minimal test case for plausibility checks."""\n',
    "data/README.md": "# Data Provenance\n\nEvery file under external/ and examples/ must be documented here with source and license.\n",
    "experiments/scripts/run_ground_truth.py": "",
    "experiments/scripts/run_smartprior.py": "",
    "experiments/scripts/compare_results.py": '"""Comparison metrics: ground truth vs. SmartPrior. Metric function (e.g. MAE on TAC, runtime) is passed as an argument, not hardcoded."""\n',
    "paper/figures/make_figures.py": "",
    "paper/tables/make_tables.py": "",
    "docs/methodology.md": "# Methodology\n",
    "README.md": "# SmartPrior\n\n(Outline to be filled in step 4)\n",
    "CITATION.cff": "",
    ".gitignore": (
        "__pycache__/\n*.pyc\n.venv/\n.ipynb_checkpoints/\n"
        "experiments/results/raw/\n*.egg-info/\ndist/\nbuild/\n"
    ),
}


def scaffold() -> None:
    for d in DIRS:
        (ROOT / d).mkdir(parents=True, exist_ok=True)

    for rel_path, content in FILES.items():
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            print(f"skip (exists): {rel_path}")
            continue
        path.write_text(content, encoding="utf-8")
        print(f"created: {rel_path}")


if __name__ == "__main__":
    scaffold()
