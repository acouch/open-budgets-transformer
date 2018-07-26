# Flare Budget Generator

This project is adopted from [open-budget](https://github.com/cityofphiladelphia/open-budget). That tool has a couple of functional components. This took the ``flare/`` folder and added a configuration step.

The `flare` directory is meant to take two years worth of data (representing the
same cycle) and output a single `data.json` file, which can be put into the
open-budget application.

## Usage

### Configuration

Add an agency to the ``config.yml`` file. Next run:

```
python flare.py phl > data.json
```

## Config.yml

The configuration requires the following keys: sortyBy, nestedKeys, inputFiles. Example:

```yml
phl:
  sortBy: 2019
  nestKeys:
  - 'fund'
  - 'department'
  - 'class'
  inputFiles:
  - fiscal_year: 2017
    path: "../proposed-ordinance/output/FY2017-proposed.csv"
  - fiscal_year: 2019
    path: "../proposed-ordinance/output/FY19-proposed.csv"
```

