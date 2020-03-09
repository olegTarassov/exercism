class Allergies:
    def __init__(self, score: int):

        self._allergies_inventory = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats",
        }

        self._allergic = []

        keys = sorted(self._allergies_inventory.keys(), reverse=True)

        for x in keys:
            test_score = score
            test_allergic = list()

            for y in keys[keys.index(x)::]:

                if test_score - y >= 0:
                    test_allergic.append(self._allergies_inventory[y])
                    test_score -= y

                # when allergy score is depleted, we have a matched series
                if test_score == 0:
                    self._allergic = test_allergic.copy()
                    break

            # Break when we have list of matched allergies
            if self._allergic:
                break

    def allergic_to(self, item):
        return True if item in self._allergic else False

    @property
    def lst(self):
        return self._allergic
