class StableMatcher:
    def __init__(self, a_preferences_list, b_preferences_list):
        """
        a_preferences_list: list(list(int)) - a list of lists with length
        all equal to len(a_preferences_list) that represents the preferences
        that the "a" population has for the "b" population; the ints in the
        lists are indexes
        """
        self.a_preferences_list = [*a_preferences_list]
        self.b_preferences_list = [*b_preferences_list]

        self.a_statuses = [0] * len(a_preferences_list)
        self.b_front_doors = [[] for _ in range(len(b_preferences_list))]

    def terminated(self):
        return all(len(b_front_door) == 1 for b_front_door in self.b_front_doors)

    def start(self):
        # all "a"s go to most preferable "b"
        for i, preferences in enumerate(self.a_preferences_list):
            self.b_front_doors[preferences[0]].append(i)

    def most_preferable(self, front_door, i):
        # find the most preferable "a" in a group
        for a in self.b_preferences_list[i]:
            if a in front_door:
                return a

    def step(self):
        # if multiple at any "b", move the less desired "a"s
        for i, front_door in enumerate(self.b_front_doors):
            if len(front_door) > 1:
                for a in front_door:
                    if a != self.most_preferable(front_door, i):
                        self.a_statuses[a] += 1
                        front_door.remove(a)
                        print(self.a_statuses[a])
                        self.b_front_doors[self.a_preferences_list[a][self.a_statuses[a]]].append(a)

    def match(self):
        self.start()
        while not self.terminated():
            self.step()

        return list(zip(
            [front_door[0] for front_door in self.b_front_doors],
            [i for i in range(len(self.b_front_doors))],
        ))