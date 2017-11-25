Feature: Group CRUD
    Description

    Scenario Outline: Add new group
        Given a group list on app
        Given a new group with <name>, <header>, <footer>
        When I add this group
        Then a new group list is equal to old group list with this new group

        Examples:
        | name | header | footer |
        | Ahdf | dfjdkf | TRFC   |
        | Пе ев| ррпрп  | ККВЛАП |
        | hfdhf|        |        |