from extract import read_stations_csv, read_lines_csv, read_boroughs_csv, read_zones_csv, read_zones_csv, read_journeys_json, read_schedules_xml

if __name__ == "__main__":
    stations = read_stations_csv()
    lines = read_lines_csv()
    boroughs = read_boroughs_csv()
    zones = read_zones_csv()
    journeys = read_journeys_json()
    schedules = read_schedules_xml()

    print("Stations:", len(stations))
    print("Lines:", len(lines))
    print("Boroughs:", len(boroughs))
    print("Zones:", len(zones))
    print("Journeys:", len(journeys))
    print("Schedules:", len(schedules))