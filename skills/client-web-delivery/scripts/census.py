"""Local numbers for stat cards, from the U.S. Census Bureau (references/hype-set.md, "The numbers").

    python census.py find "Hidalgo County, Texas"
    python census.py county 48 215 [--year 2023] [--json out.json]

`find` lists the state and county codes for a name. `county` prints the
figures a stat card can use, each with the Census's own label for it (read
live, so a renumbered table is caught) and the source line to print on the card.

The data API needs a free key. Put it in the builder profile
(~/.client-site-pipeline/builder.json, "census_api_key") or in CENSUS_API_KEY.
Get one at https://api.census.gov/data/key_signup.html (the builder signs up;
an agent never does it for them). Without a key this stops and says so:
it never guesses a number.

Figures are American Community Survey 5-year estimates: survey estimates with a
margin of error, not a head count. Say "about" on the card when rounding.
"""
import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.census.gov/data/{year}/acs/acs5/profile"
# What a local business card can use. The label is read from the API each run and printed beside the value.
FIGURES = [
    ("DP05_0001E", "People living here"),
    ("DP02_0114PE", "Speak a language other than English at home (percent, age 5 and over)"),
    ("DP02_0116PE", "Speak Spanish at home (percent, age 5 and over)"),
    ("DP02_0154PE", "Households with a broadband internet subscription (percent)"),
    ("DP03_0062E", "Median household income (dollars)"),
]


def key():
    found = os.environ.get("CENSUS_API_KEY")
    profile = pathlib.Path.home() / ".client-site-pipeline" / "builder.json"
    if not found and profile.exists():
        found = (json.loads(profile.read_text(encoding="utf-8")) or {}).get("census_api_key")
    if not found:
        sys.exit("No Census API key. The builder gets a free one at https://api.census.gov/data/key_signup.html and puts it in\n"
                 f"{profile} as \"census_api_key\". Until then, open https://www.census.gov/quickfacts in a browser and read the figure there.")
    return found


def get(url):
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        sys.exit(f"The Census API answered {err.code} for {url.split('?')[0]}")
    if body.lstrip().startswith("<"):
        sys.exit("The Census API did not accept the key (it returned a web page instead of data). Check \"census_api_key\".")
    return json.loads(body)


def find(a):
    name = a.name.lower()
    state_part = name.split(",")[-1].strip() if "," in name else ""
    states = get(BASE.format(year=a.year) + "?" + urllib.parse.urlencode({"get": "NAME", "for": "state:*", "key": key()}))
    hits = 0
    for state_name, state in states[1:]:
        if state_part and state_part not in state_name.lower():
            continue
        rows = get(BASE.format(year=a.year) + "?" + urllib.parse.urlencode({"get": "NAME", "for": "county:*", "in": f"state:{state}", "key": key()}))
        for county_name, st, county in rows[1:]:
            if name.split(",")[0].strip() in county_name.lower():
                print(f"{county_name}: python census.py county {st} {county}")
                hits += 1
    if not hits:
        sys.exit("No county by that name. Try it as \"Name County, State\".")


def county(a):
    api_key = key()
    codes = ",".join(code for code, _ in FIGURES)
    rows = get(BASE.format(year=a.year) + "?" + urllib.parse.urlencode(
        {"get": "NAME," + codes, "for": f"county:{a.county}", "in": f"state:{a.state}", "key": api_key}))
    header, values = rows[0], rows[1]
    place = values[header.index("NAME")]
    source = f"U.S. Census Bureau, American Community Survey 5-year estimates, {a.year}"
    out = {"place": place, "source": source, "year": a.year, "figures": []}
    print(f"{place}\n{source}\n")
    for code, plain in FIGURES:
        label = get(BASE.format(year=a.year) + f"/variables/{code}.json").get("label", "").replace("!!", " > ")
        value = values[header.index(code)]
        print(f"  {value:>12}  {plain}\n{'':16}Census label: {label}")
        out["figures"].append({"code": code, "value": value, "meaning": plain, "census_label": label})
    print("\nThese are survey estimates. Print the source line on the card, and open the table once before it goes out:")
    print(f"  https://data.census.gov/table?q=DP02&g=050XX00US{a.state}{a.county}")
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(f"wrote {a.json}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("find")
    f.add_argument("name")
    f.add_argument("--year", type=int, default=2023)
    c = sub.add_parser("county")
    c.add_argument("state")
    c.add_argument("county")
    c.add_argument("--year", type=int, default=2023)
    c.add_argument("--json")
    a = ap.parse_args()
    {"find": find, "county": county}[a.cmd](a)


if __name__ == "__main__":
    main()
