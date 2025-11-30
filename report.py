def main():
    spacecraft = {"name":"James Webb Space Telescope"} # Distance in Astronomical Units (AU)
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    =========Report=========
    Name: {spacecraft.get("name", "Unkown")}
    Distance: {spacecraft.get("distance", "Unkown")} AU
    Orbit: {spacecraft.get("orbit", "Unkown")}
    ========================
"""

main()

