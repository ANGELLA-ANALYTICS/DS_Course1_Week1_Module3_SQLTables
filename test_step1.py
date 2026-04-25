import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# Check Step 1 query
result = pd.read_sql('''
SELECT e.firstName, e.lastName, e.jobTitle
FROM employees e
INNER JOIN offices o ON e.officeCode = o.officeCode
WHERE o.city = "Boston"
''', conn)

print('Step 1 Results:')
print(result)
print(f'\nNumber of rows: {len(result)}')
print(f'Columns: {list(result.columns)}')

conn.close()
