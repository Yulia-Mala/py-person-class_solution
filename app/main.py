class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances_ls = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        name = person["name"]
        if person.get("wife"):
            Person.people[name].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[name].husband = Person.people[person["husband"]]
    return instances_ls
