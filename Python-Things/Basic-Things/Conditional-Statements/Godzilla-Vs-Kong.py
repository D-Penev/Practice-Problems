def godzilla_vs_kong():
    film_budget = float(input())
    walk_on_count = float(input())
    walk_on_cost = float(input())
    film_decor = film_budget * 0.10
    walk_on_total = walk_on_cost * walk_on_count
    if walk_on_count > 150:
        walk_on_total -= (walk_on_total * 0.10)

    total_film_cost = film_decor + walk_on_total
    if total_film_cost <= film_budget:
        print('Action!')
        print("Wingard starts filming with {:.2f} leva left.".format(film_budget - total_film_cost))
    else:
        print('Not enough money!')
        print('Wingard needs {:.2f} leva more.'.format(total_film_cost - film_budget))


godzilla_vs_kong()