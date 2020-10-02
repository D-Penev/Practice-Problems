def countries_and_capitals():
    countries = list(input().split())
    capitals = list(input().split())
    countries_and_capitals_dict = get_countries_and_capitals(countries, capitals)
    return  '\n'.join({(f'{x} -> {x}')} for x in countries_and_capitals_dict)

def get_countries_and_capitals(countries, capitals):
    countries_iterable = iter(countries)
    capitals_iterable = iter(capitals)
    return dict(zip(countries_iterable, capitals_iterable))

print(
    countries_and_capitals()
)
