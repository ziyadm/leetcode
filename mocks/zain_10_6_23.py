import pdb

# Take in fact set, build conversion dictionary
# Then, take in queries, output converted value as floating point 
# If conversion is not available, throw an error
class conversion_library:
    def __init__(self, facts):
        self.unit_conversion_dictionary = {}
        for fact in facts:
            # Tuple: 0 = starting, 1 = ending, 2 = conversion
            self.unit_conversion_dictionary[(fact[0], fact[1])] = fact[2]

    def convert_units(self, query) -> float:
        # Tuple: 0 = starting, 1 = ending, 2 = quantity of starting unit
        try:
            conversion_factor = self.unit_conversion_dictionary[(query[0], query[1])]
            return query[2] * conversion_factor
        except KeyError as error_message:
            print(error_message)
            return 0.0

facts = [("inches", "cm", 2.5)]
query = ("cm", "inches", 5)
output = 2.0
test_conversion_cases = conversion_library(facts)
actual_return_value = test_conversion_cases.convert_units(query)
assert test_conversion_cases.convert_units(query) == output




# Facts: ‘inches’, ‘ft’, 12
#        'inches', ‘cm’, 2.5
# Query:
#        ‘in’, ‘cm’, 2



