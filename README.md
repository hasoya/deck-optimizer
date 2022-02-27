# deck-optimizer

[![PyPI version](https://badge.fury.io/py/dkopt.svg)](https://badge.fury.io/py/dkopt)
[![Python Versions](https://img.shields.io/pypi/pyversions/dkopt.svg)](https://pypi.org/project/dkopt/)
[![DockerPublish](https://github.com/hasoya/deck-optimizer/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/hasoya/deck-optimizer/actions/workflows/docker-publish.yml)
[![pytest](https://github.com/hasoya/deck-optimizer/actions/workflows/python-app.yml/badge.svg)](https://github.com/hasoya/deck-optimizer/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/hasoya/deck-optimizer/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/hasoya/deck-optimizer/actions/workflows/pypi-publish.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9cd9ee6c310947029719e7c22af67cb2)](https://www.codacy.com/gh/hasoya/deck-optimizer/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hasoya/deck-optimizer&amp;utm_campaign=Badge_Grade)

**deck-optimizer** is a Python module to support TCG deck building especially Yu-Gi-Oh!. This module suggest the best combination of cards under given conditions.

## Dependency

Use [Docker](https://www.docker.com/) or see [requirements.txt](https://github.com/hasoya/deck-optimizer/blob/main/requirements.txt).

## Usage

Make config yaml file to describe the ideal hand. For example, if you want to draw at least one PSY-Framegear Gamma and keep PSY-Frame Driver in deck, your config file will be written as below.

```yaml:config.yaml
num_hand: 5
num_deck:
  min: 40
  max: 60
condition:
  - name: Gamma
    min: 2
    max: 3
    require: 1
    exact: False
    in_hand: True
  - name: Driver
    min: 1
    max: 1
    require: 1
    exact: True
    in_hand: False
```

Then, run the app by following command.

```bash
docker pull ghcr.io/hasoya/deck-optimizer:v0.0.1
docker run -v /absolute/path/to/config/file:/config.yaml ghcr.io/hasoya/deck-optimizer:v0.0.1 -f /config.yaml
```

You will get the suggestion of deck composition and the probability of the ideal hand.

```bash
The best deck
  Total Num Deck: 40 Num Gamma in deck: 3 Num Driver in deck: 1
The probability of the ideal hand
  30.21%
```
