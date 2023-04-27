company = {
    'employees': [ 
        # Employees List
        {'name': 'Mary', 'age': 20},
        {'name': 'Adriana', 'age': 25},
        {'name': 'Steffany', 'age': 24}
    ],
    'cars': [
        # cars list - submodels list
        {'brand': 'Ford', 'model': 'Wrangler', 'submodels': ['Sport', 'Sport S']},
        {'brand': 'Mustang', 'model': 'Macth', 'submodels': ['The Shelby', 'GT']},
        {'brand': 'Chevrolet', 'model': 'Camaro', 'submodels': ['ZL1 1LE', 'SS 1LE']}
    ]
}

print('Employee 3 Age:', company['employees'][2]['age'])
print('Submodel 2 Mustang:', company['cars'][1]['submodels'][1]) 