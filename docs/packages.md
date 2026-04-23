---
title: Packages
card_title: Packages
card_description: "The Python packages included in Honeybee-REVIVE and what each one does."
---

# Packages

Honeybee-REVIVE is distributed as a single PyPI package (`honeybee-revive`) containing
five sub-packages. Each extends a different part of the Ladybug Tools ecosystem with
Phius REVIVE resilience and lifecycle carbon-cost data.

## honeybee_revive

The core REVIVE data model. Extends Honeybee with lifecycle cost and embodied carbon
elements including:

- **CO2 measures** — reduction measures with cost and carbon data
- **Fuels** — electricity and natural gas pricing
- **Grid regions** — NREL Cambium region codes for hourly grid emissions factors
- **National emissions** — country-level embodied carbon intensity factors (kg CO2/USD GDP)

Attaches `.revive` properties to Honeybee Model, Room, Face, Aperture, and Shade objects.

[PyPI](https://pypi.org/project/honeybee-REVIVE/) |
[Source](https://github.com/PH-Tools/honeybee_REVIVE/tree/main/honeybee_revive)

## honeybee_energy_revive

Extensions to Honeybee-Energy for REVIVE-style embodied carbon, cost, and lifecycle data.
Adds `.revive` properties to:

- Materials and constructions (kg CO2/m², cost/m², labor fraction, lifetime)
- Loads (people, lighting, equipment, process)
- HVAC systems (AllAir, DOAS, HeatCool, IdealAir)
- Hot water, generators, and schedule rulesets

[Source](https://github.com/PH-Tools/honeybee_REVIVE/tree/main/honeybee_energy_revive)

## honeybee_revive_standards

Reference datasets shipped as JSON files:

- Program types and occupancy schedules
- Appliance load definitions
- CO2 reduction measure libraries
- National emissions factors
- Cambium grid region data (27 regions)

[Source](https://github.com/PH-Tools/honeybee_REVIVE/tree/main/honeybee_revive_standards)

## honeybee_revive_measures

OpenStudio / EnergyPlus measures for REVIVE-specific building physics:

- **set_revive_people_eplus** — adds resilience-specific behavioral schedules
  (work efficiency, seasonal clothing) for thermal comfort modeling during
  extended power outages

[Source](https://github.com/PH-Tools/honeybee_REVIVE/tree/main/honeybee_revive_measures)

## ladybug_revive

Weather morphing utilities for resilience analysis:

- **Adjustment factors** — sinusoidal temperature morphing for extreme-week generation
  (adapted from the Phius Research Committee algorithm)
- **Resiliency EPW** — creates morphed EPW weather files with return-period extreme
  temperatures for summer heat and winter cold scenarios

[Source](https://github.com/PH-Tools/honeybee_REVIVE/tree/main/ladybug_revive)
