"""
Einmaliges Scaffolding-Skript fuer das smartprior-Repository.
Ausfuehren im gewuenschten Zielverzeichnis: python scaffold_repo.py
Legt Ordner und leere Platzhalterdateien an. Ueberschreibt nichts Vorhandenes.
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
    "src/smartprior/simulator/pv.py": '"""PV-Erzeugung: Parameterobjekt und Berechnung."""\n',
    "src/smartprior/simulator/battery.py": '"""Batteriespeicher: Parameterobjekt und Bilanzierung."""\n',
    "src/smartprior/simulator/chp.py": '"""BHKW: Parameterobjekt (inkl. MPL, Mindestlaufzeiten, Grenzkosten) und Dispatch-Verhalten."""\n',
    "src/smartprior/simulator/heat_pump.py": '"""Waermepumpe: Parameterobjekt und Dispatch-Verhalten."""\n',
    "src/smartprior/simulator/boiler.py": '"""Gaskessel: Parameterobjekt und Dispatch-Verhalten."""\n',
    "src/smartprior/simulator/solar_thermal.py": '"""Solarthermie: fixe Prioritaet, Dimensionierung als Einflussgroesse."""\n',
    "src/smartprior/simulator/storage.py": '"""Waermespeicher: Zustandsgroesse, kein Dimensionierungsparameter."""\n',
    "src/smartprior/simulator/dispatch.py": '"""Merit-Order-Zustandsautomat: Grenzkosten-Sortierung, MPL/Mindestlaufzeit-Logik."""\n',
    "src/smartprior/simulator/runner.py": '"""Oeffentliche Simulate-Funktion: Jahres-Loop, stabile Parameterschnittstelle fuer DoE."""\n',
    "src/smartprior/doe/__init__.py": "",
    "src/smartprior/doe/sampling.py": '"""LHS/DoE-Sampling ueber den Parameterraum."""\n',
    "src/smartprior/doe/schemas.py": '"""Definition der Grenzwertkombinationen (Schubladen)."""\n',
    "src/smartprior/gpr/__init__.py": "",
    "src/smartprior/gpr/training.py": '"""GPR-Training auf energetischen Zielgroessen."""\n',
    "src/smartprior/gpr/evaluation.py": '"""GPR-Auswertung inkl. nachgelagerter TAC/CO2-Verrechnung."""\n',
    "src/smartprior/optimization/__init__.py": "",
    "src/smartprior/optimization/pso.py": '"""Eigene PSO-Implementierung fuer die Optimierung auf Basis der GPR-Modelle."""\n',
    "src/smartprior/config/__init__.py": "",
    "src/smartprior/config/defaults.py": '"""Zentrale technologietypische Konstanten: MPL, Mindestlaufzeiten. Einziger Ort fuer diese Werte."""\n',
    "tests/__init__.py": "",
    "tests/test_dispatch.py": "",
    "tests/test_storage.py": "",
    "tests/test_energy_balance.py": "",
    "tests/fixtures/minimal_case.py": '"""Handrechnungs-Testfall fuer Plausibilitaetspruefung."""\n',
    "data/README.md": "# Datenherkunft\n\nJede Datei in external/ und examples/ muss hier mit Quelle und Lizenz dokumentiert werden.\n",
    "experiments/scripts/run_ground_truth.py": "",
    "experiments/scripts/run_smartprior.py": "",
    "experiments/scripts/compare_results.py": '"""Vergleichsmetriken GT vs. SmartPrior. Metrik-Funktion (z.B. MAE auf TAC, Rechenzeit) als Argument uebergeben, nicht hartkodiert."""\n',
    "paper/figures/make_figures.py": "",
    "paper/tables/make_tables.py": "",
    "docs/methodology.md": "# Methodik\n",
    "README.md": "# SmartPrior\n\n(Gliederung folgt in Schritt 4)\n",
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
