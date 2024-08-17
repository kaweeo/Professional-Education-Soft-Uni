import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, Sum, F, Avg
from main_app.models import Astronaut, Mission, Spacecraft

# Django Queries I

def get_astronauts(search_string=None) -> str:
    if not search_string:
        return ""

    if search_string == "":
        astronauts = Astronaut.objects.order_by('name')
    else:
        search_string = search_string.lower()
        astronauts = Astronaut.objects.filter(
            Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
        ).order_by('name')

    if not astronauts.exists():
        return ""

    result_lines = []
    for astronaut in astronauts:
        status = 'Active' if astronaut.is_active else 'Inactive'
        result_lines.append(
            f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {status}"
        )

    result = "\n".join(result_lines)

    return result


def get_top_astronaut() -> str:
    if not Astronaut.objects.exists():
        return "No data."

    top_astronaut = (
        Astronaut.objects.get_astronauts_by_missions_count().first()
    )

    if not top_astronaut:
        return "No data."

    if top_astronaut.missions_count == 0:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.missions_count} missions."


def get_top_commander() -> str:
    top_commander = (
        Astronaut.objects
        .annotate(commanded_missions_count=Count('missions_as_commander'))
        # .filter(commanded_missions_count__gt=0)  # Only consider astronauts with at least one commanded mission
        .order_by('-commanded_missions_count',
                  'phone_number')  # Sort by number of commanded missions descending, then by phone number ascending
        .first()
    )

    if not top_commander:
        return "No data."

    if top_commander.commanded_missions_count == 0:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.commanded_missions_count} commanded missions."


# Django Queries II
def get_last_completed_mission() -> str:
    last_completed_mission = (
        Mission.objects
        .filter(status="Completed")
        .order_by('-launch_date')
        .first()
    )

    if not last_completed_mission:
        return "No data."

    mission_name = last_completed_mission.name
    commander = last_completed_mission.commander
    spacecraft_name = last_completed_mission.spacecraft.name

    commander_name = commander.name if commander else "TBA"

    astronauts = last_completed_mission.astronauts.all().order_by('name')
    astronaut_names = [astronaut.name for astronaut in astronauts]

    total_spacewalks = astronauts.aggregate(Sum('spacewalks'))['spacewalks__sum'] or 0

    astronaut_names_str = ', '.join(astronaut_names)


    result = (
        f"The last completed mission is: {mission_name}. "
        f"Commander: {commander_name}. "
        f"Astronauts: {astronaut_names_str}. "
        f"Spacecraft: {spacecraft_name}. "
        f"Total spacewalks: {total_spacewalks}."
    )

    return result


def get_most_used_spacecraft() -> str:
    most_used_spacecraft = (
        Spacecraft.objects
        .annotate(num_missions=Count('mission'))
        .order_by('-num_missions', 'name')
        .first()
    )

    if not most_used_spacecraft:
        return "No data."

    spacecraft_name = most_used_spacecraft.name
    manufacturer = most_used_spacecraft.manufacturer
    num_missions = most_used_spacecraft.num_missions

    num_astronauts = (
        Astronaut.objects
        .filter(mission__spacecraft=most_used_spacecraft)
        .distinct()
        .count()
    )

    result = (
        f"The most used spacecraft is: {spacecraft_name}, manufactured by {manufacturer}, "
        f"used in {num_missions} missions, astronauts on missions: {num_astronauts}."
    )

    return result


def decrease_spacecrafts_weight() -> str:
    spacecrafts_with_planned_missions = Spacecraft.objects.filter(
        mission__status='Planned',
        weight__gte=200.0
    ).distinct()

    if not spacecrafts_with_planned_missions.exists():
        return "No changes in weight."

    updated_count = spacecrafts_with_planned_missions.update(
        weight=F('weight') - 200.0
    )

    avg_weight = Spacecraft.objects.aggregate(Avg('weight'))['weight__avg']
    avg_weight = round(avg_weight, 1) if avg_weight is not None else 0.0

    result = (
        f"The weight of {updated_count} spacecrafts has been decreased. "
        f"The new average weight of all spacecrafts is {avg_weight}kg"
    )

    return result
