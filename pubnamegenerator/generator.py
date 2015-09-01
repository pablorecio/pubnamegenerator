import random

from .consts import THINGS, ADJECTIVES, TITLES, TUBE_STOPS


def generate_pub_name():

    def _the_thing():
        return 'The %s' % random.choice(THINGS)

    def _the_adjective_thing():
        return 'The %s %s' % (random.choice(ADJECTIVES), random.choice(THINGS))

    def _the_thing_arms():
        return 'The %s Arms' % random.choice(THINGS)

    def _the_thing_and_thing():
        return 'The %s and %s' % (random.choice(THINGS), random.choice(THINGS))

    def _the_title_of_somewhere():
        return 'The %s of %s' % (random.choice(TITLES), random.choice(TUBE_STOPS))

    generator_function = random.choice([
        _the_thing,
        _the_adjective_thing,
        _the_thing_arms,
        _the_thing_and_thing,
        _the_title_of_somewhere,
    ])

    return generator_function()
