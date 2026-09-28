# SmartPrior

SmartPrior ist eine Methodik zur schnellen Optimierung von Energieversorgungssystemen (EVS) mittels vorab trainierter Gaussprozessregressions-Modelle (GPR). Statt für jeden Anwendungsfall eine neue MILP-Formulierung oder Simulation aufzusetzen, approximieren die GPR-Modelle rein energetische Zielgroessen fuer typische Randbedingungs-Kombinationen ("Schubladen"). Oekonomische und oekologische Bewertung (TAC, CO2) erfolgt nachgelagert und variabel, ohne Neutraining.

Dieses Repository enthaelt:
- einen offenen, regelbasierten Merit-Order-Dispatch-Simulator als Ground-Truth-Referenz
- die DoE-Sampling-Pipeline zur Erzeugung der Trainingsdaten
- das GPR-Training und die nachgelagerte TAC/CO2-Verrechnung
- eine eigene Partikelschwarmoptimierung (PSO) auf Basis der GPR-Modelle
- die Skripte zur Reproduktion der im zugehoerigen Paper gezeigten Ergebnisse

## Zugehoeriges Paper

Wird nach Veroeffentlichung ergaenzt (Titel, Autoren, DOI).

## Repository-Struktur

```
src/smartprior/simulator/     Merit-Order-Dispatch-Simulator (Ground Truth)
src/smartprior/doe/           DoE-Sampling und Schubladen-Definitionen
src/smartprior/gpr/           GPR-Training und -Auswertung
src/smartprior/optimization/  Eigene PSO-Implementierung
src/smartprior/config/        Zentrale technologietypische Konstanten
tests/                        Unit- und Plausibilitaetstests
data/                         Offene Beispieldaten und externe Referenzquellen
experiments/                  Konkrete Simulations- und Vergleichslaeufe
paper/                        Skripte zur Erzeugung der Paper-Abbildungen und -Tabellen
```

## Installation

Voraussetzung: Python 3.10 oder neuer.

```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Quickstart

```python
from smartprior.simulator.runner import simulate

result = simulate(...)  # Parameterschnittstelle siehe src/smartprior/simulator/runner.py
```

Ein vollstaendiges Beispiel folgt in `notebooks/01_dispatch_demo.ipynb`.

## Reproduktion der Paper-Ergebnisse

Alle im Paper gezeigten Abbildungen und Tabellen lassen sich aus den Skripten in `experiments/scripts/` und `paper/figures/` bzw. `paper/tables/` reproduzieren. Die verwendeten Parameterkombinationen sind in `experiments/configs/` dokumentiert.

## Daten

`data/examples/` enthaelt ausschliesslich offene bzw. synthetische Beispieldaten (Lastgaenge, Wetterdaten), die mit diesem Repository frei nutzbar sind. Herkunft und Lizenz jeder Datei sind in `data/README.md` dokumentiert.

Interne Kennwerte aus dem SmartPrior-Schlussbericht sind **nicht** Teil dieses Repositories. Fuer technologische Kosten- und Wirkungsgradkennwerte (BHKW, Waermepumpe, Gaskessel, Speicher, PV, Solarthermie) wurden ausschliesslich offen zugaengliche Referenzquellen verwendet (Details in `data/README.md`).

## Data and Code Availability Statement

Der vollstaendige Quellcode ist unter der MIT-Lizenz oeffentlich verfuegbar unter: https://github.com/MariusReichh/smartprior. Alle verwendeten Beispieldaten sind im Repository unter `data/examples/` enthalten. Interne, projektvertrauliche Kennwerte wurden durch offen zugaengliche Referenzwerte ersetzt (siehe `data/README.md`).

## Lizenz

MIT, siehe [LICENSE](LICENSE).

## Zitation

Siehe [CITATION.cff](CITATION.cff).
